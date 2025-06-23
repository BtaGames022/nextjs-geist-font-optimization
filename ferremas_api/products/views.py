from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Contact
from .serializers import ProductSerializer, ContactSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        code = self.request.query_params.get('code', None)
        brand = self.request.query_params.get('brand', None)
        
        if code:
            queryset = queryset.filter(code__icontains=code)
        if brand:
            queryset = queryset.filter(brand__icontains=brand)
            
        return queryset

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint for contact messages
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']  # Only allow POST requests
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Mensaje enviado exitosamente"},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
