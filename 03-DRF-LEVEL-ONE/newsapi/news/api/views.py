from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer


class ArticleListCreateAPIView(APIView):

    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)      

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistListCreateAPIView(APIView):
    
    def get(self, request):
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(journalists, 
                                          many=True,
                                          context={'request': request})
        return Response(serializer.data)      

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


# @api_view(["GET", "POST"])
# def article_list_create_api_view(request):

#     if request.method == "GET":
#         articles = Article.objects.filter(active=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def article_detail_api_view(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"error": {
#                             "code": 404,
#                             "message": "Article not found!"
#                         }}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)