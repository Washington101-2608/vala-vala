from rest_framework import serializers
from core.models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            url = obj.image.url
            # fix double /media/media/ issue
            if url.startswith('/media/media/'):
                url = url.replace('/media/media/', '/media/', 1)
            return url
        return ''

    class Meta:
        model = Product
        exclude = ['date_created']