import django_filters
from .models import Author, Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    author = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    published_date = django_filters.DateFilter(lookup_expr='exact')
    isbn = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book 
        fields = ['title', 'author', 'published_date', 'isbn']
