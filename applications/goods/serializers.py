from rest_framework import serializers

from applications.goods.models import GoodsImage, Goods
from applications.review.serializers import ReviewSerializer


class GoodsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) !=0:
            rep['total_rating'] = sum(total_rating) / len(total_rating)
        else:
            rep['total_rating'] = ''
        rep['images'] = GoodsImageSerializer(GoodsImage.objects.filter(goods=instance.id), many=True, context=self.context).data
        rep['reviews'] = ReviewSerializer(instance.review.filter(goods=instance.id), many=True).data
        return rep

