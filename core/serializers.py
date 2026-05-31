from rest_framework import serializers
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ['date_created']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return ''