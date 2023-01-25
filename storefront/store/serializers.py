from rest_framework import serializers
from store.models import Product,Collection,Review,CartItem,Cart
from decimal import Decimal

class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length = 255)


class ProductSerializers(serializers.ModelSerializer):                      #Directly use modelSerializer 
    class Meta:
        model = Product
        fields = ['id','title','slug','description','inventory','unit_price','price_after_tax','collection']     # do not use '__all__' that could output all field in models product
    price_after_tax = serializers.SerializerMethodField(method_name= 'cal_tex')


    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length = 255)
    # price = serializers.DecimalField(max_digits=6,decimal_places=2,source = 'unit_price')


    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),                                   # Build link that will made collection to product
    #     view_name = 'collection-detail'
    
    # )


    def cal_tex(self,product:Product):
        return product.unit_price * Decimal(2.1)

class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','products_count']
    products_count = serializers.IntegerField(read_only = True)

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description']
    def create(self, validated_data):
        product_id = self.context['product_id']                 # self.context were used to collect data from ViewSets method get_seralizer_context
        return Review.objects.create(product_id = product_id,**validated_data)            # validated_ data is the JSON content

class SimpleProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price']



class CartItemSerializers(serializers.ModelSerializer):
    
    product = SimpleProductSerializers(read_only = True)
    total_price = serializers.SerializerMethodField()
    
    def get_total_price(self,cart_item:CartItem):
        return cart_item.quantity * cart_item.product.unit_price
    
    class Meta:
        model = CartItem

        fields = ['id','product','quantity','total_price']

class CartSerializers(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializers(many = True,read_only = True)
    cart_total_price = serializers.SerializerMethodField()

    def get_cart_total_price(self,cart:Cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])
    
    class Meta:
        model = Cart 
        fields = ['id','items','cart_total_price']

class AddItemSerializers(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk = value).exists():
            raise serializers.ValidationError('No product with such id')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id = cart_id, product_id = product_id, quantity = quantity)
            cart_item.quantity = quantity
            cart_item.save()
            self.instance = cart_item
            #if product exist add quantity number
        except CartItem.DoesNotExist:
            # if product did not exist 
            self.instance =  CartItem.objects.create(cart_id = cart_id, **self.validated_data)
        
        return self.instance

    class Meta:
        model = CartItem
        fields = ['id','product_id','quantity']

class UpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['quantity']
    