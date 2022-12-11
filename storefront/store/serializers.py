from rest_framework import serializers
from store.models import Product,Collection
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