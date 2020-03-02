from rest_framework import serializers

from .models import Book, Journal


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'price', 'description', 'created_at', 'num_pages',)

    def validate_num_pages(self, num_pages):
        if num_pages < 0:
            raise serializers.ValidationError('Number of pages can not be negative number!')
        return num_pages


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('name', 'price', 'description', 'created_at', 'publisher', 'type',)

    def validate_type(self, type):
        if 1 > type or type > 4:
            raise serializers.ValidationError('Type must be in interval between 1 and 4!')
        return type
