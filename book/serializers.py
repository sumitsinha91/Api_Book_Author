from rest_framework import serializers

from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):

	"""
	Serializing all type the books
	"""
	search_url = serializers.SerializerMethodField('get_search_urls')

	class Meta:
		model = Book
		fields = ('id', 'title','isbn', 'search_url')

	def get_search_urls(self,obj):
		return "http://www.isbnsearch.org/{}".format(obj.isbn)

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all authors
    """
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')		