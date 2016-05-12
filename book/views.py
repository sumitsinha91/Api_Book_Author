from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.

class AuthorView(generics.ListAPIView):

    """

    """

    queryset = Author.objects.all()
    model = Author
    serializer_class = AuthorSerializer


class BookView(generics.ListAPIView):

    """

    """

    model = Book
    serializer_class = BookSerializer

class AuthorInstanceView(generics.RetrieveAPIView):
    """
    
    """
    model = Author
    serializer_class = AuthorSerializer

    
    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset =Author.objects.filter(pk=pk)
        return queryset

    def index_View(request):
        response = {'Authors': Author.object.all()}
        return render(request, 'index.htm', response)

####################





