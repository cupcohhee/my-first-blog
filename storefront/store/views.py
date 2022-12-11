from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from django.db.models import Count


from .models import Product,Collection,OrderItem
from .serializers import ProductSerializers,CollectionSerializers

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get_serializer_context(self):
        return {'request':self.request} 

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id = kwargs['pk']).count() > 0:
            return Response({'error':"Product can not be delete"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count = Count('products'))
    serializer_class = CollectionSerializers
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id = kwargs['pk']).count() > 0:
            return Response({'error':'Collection can not be delete'})
        return super().destroy(request, *args, **kwargs)



  # def delete(self, request,pk):
    #     collection = get_object_or_404(
    #     Collection.objects.annotate(
    #     products_count=Count('products')
    # )
    # ,pk = pk)
        
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    


# class ProductList(ListCreateAPIView):

    # def get_queryset(self):                # override  get querysets
    #     return Product.objects.select_related('collection').all()

    # def get_serializer(self, *args, **kwargs):
    #     return ProductSerializers
        
  

    # def get(self,request):
    #     query_set = Product.objects.select_related('collection').all()            # pir load collection field  
    #     serlizer = ProductSerializers(query_set,many = True,context ={'request':request})              # Ouput all product into website
    #     return Response(serlizer.data)  
    # def post(self,request):
    #     serializer = ProductSerializers(data = request.data)                     
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     print(serializer.validated_data)
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)

        



# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         query_set = Product.objects.select_related('collection').all()            # pir load collection field  
#         serlizer = ProductSerializers(query_set,many = True,context ={'request':request})              # Ouput all product into website
#         return Response(serlizer.data)                                                              # context need for hpyer link
#     elif request.method =='POST':
#         serializer = ProductSerializers(data = request.data)                     
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer.validated_data)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)






# class Prodcutdetail(RetrieveUpdateDestroyAPIView):               # Use generic view to simplize operation APIs
#     # product = get_object_or_404(Product,pk = id)
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers

#     # def get(self,request,id):
#     #     product = get_object_or_404(Product,pk = id)
#     #     serializer = ProductSerializers(product,context ={'request':request})      
#     #     return Response(serializer.data)
#     # def put(self,request,id):
#     #     product = get_object_or_404(Product,pk = id)
#     #     serializer = ProductSerializers(product, data= request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#     #     return Response(serializer.data)
#     def delete(self,request,pk):
#         product = get_object_or_404(Product,pk = pk)
#         if product.orderitem.count() >0:
#             return Response({'error':"product can not be delete"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        




# @api_view(['GET','PUT','DELETE'])
# def product_detail(request,id):

#     product = get_object_or_404(Product,pk = id)        # This will show if the product is not found will return error
#     if request.method =='GET':
#         serializer = ProductSerializers(product,context ={'request':request})      
#         return Response(serializer.data)
#     elif request.method =="PUT":                  # this will update data using query.
#         serializer = ProductSerializers(product, data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method =='DELETE':
#         if product.orderitem.count() >0:
#             return Response({'error':"product can not be delete"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
 





# class CollectionList(ListCreateAPIView):
   

# @api_view(['GET','POST'])
# def collection_list(request):
#     if request.method =='GET':
#         quer_set = Collection.objects.annotate(products_count = Count('products')).all()
#         serailzer = CollectionSerializers(quer_set,many =True)
#         return Response(serailzer.data)
#     elif request.method =='POST':
#         serailzer = CollectionSerializers(data=request.data)
#         serailzer.is_valid(raise_exception= True)
#         serailzer.save()
#         print(serailzer.validated_data)
#         return Response(serailzer.data,status=status.HTTP_201_CREATED)


# class CollectionDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.annotate(products_count = Count('products')).all()

#     serializer_class = CollectionSerializers
#     def delete(self, request,pk):
#         collection = get_object_or_404(
#         Collection.objects.annotate(
#         products_count=Count('products')
#     )
#     ,pk = pk)
#         if collection.products.count() > 0:
#             return Response({'error':'Collection cannot be delete have more realated product'})
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','PUT','DELETE'])
# def collection_detail(request,pk):
#     collection = get_object_or_404(
#         Collection.objects.annotate(
#         products_count=Count('products')
#     )
#     ,pk = pk)
#     if request.method =='GET':

#         serializer = CollectionSerializers(collection)
#         return Response(serializer.data)
#     elif request.method =='PUT':
#         serializer = CollectionSerializers(collection, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if collection.products.count() > 0:
#             return Response({'error':'Collection cannot be delete have more realated product'})
#         collection.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
