from rest_framework import serializers
from RED.models import articles

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = articles
        fields = '__all__'
        
        # title = serializers.CharField(max_length=220)
        # content = serializers.TextField(blank=True,null=True)
        # description = serializers.TextField(blank=True,null=True)

    # def create(self, validated_data):
    #     return articles.objects.create(validated_data)