from rest_framework import viewsets
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer 

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
