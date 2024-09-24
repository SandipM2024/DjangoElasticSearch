from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from .documents import BlogDocument

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

class BlogSearchView(viewsets.ViewSet):
    def list(self, request):
        query = request.query_params.get('q')
        if query:
            search = BlogDocument.search().query("multi_match", query=query, fields=['title', 'content'])
            response = search.execute()
            books = [hit.to_dict() for hit in response.hits]
            return Response(books)
        return Response([])



def generate_random_data():
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-08-24&sortBy=publishedAt&apiKey=ff1f0d8bec9a47b8aaebe8b624d1a507'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    print(payload)
    for data in payload.get('articles'):
        print(count)
        Blog.objects.create(
            title = data.get('title'),
            content = data.get('content')
        )

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})


# ff1f0d8bec9a47b8aaebe8b624d1a507