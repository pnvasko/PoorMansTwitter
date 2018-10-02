from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Twitters
from .serializers import TwittersSchema


def index(request):
    return render(request, 'index.html')


class TwittersView(generics.ListAPIView):
    queryset = Twitters.objects.all()
    serializer_class = TwittersSchema
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('id', 'tweetdate', 'nick')


@api_view(['POST'])
def twitters_add(request):
    if request.method == 'POST':
        schema = TwittersSchema(data=request.data)
        if schema.is_valid():
            schema.save()
            return Response(schema.data, status=status.HTTP_201_CREATED)
        return Response(schema.errors, status=status.HTTP_400_BAD_REQUEST)
