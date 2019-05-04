from rest_framework import serializers
from .models import Category
from .models import Formula

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class FormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formula
        fields = ('id', 'name', 'description' , 'content' , 'category_id')