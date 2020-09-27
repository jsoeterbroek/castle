from rest_framework import serializers
from teylers_museum_api.scrape.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'illustrator', 'dating', 'material',
                  'measurements', 'location', 'publisher', 'url',
                  'object_number']
        #extra_kwargs = {
        #    "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        #}
