from  rest_framework import serializers
from base.models import item


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = "__all__"  
        extra_kwargs = {'std_code': {'required': False},'uni_code': {'required': False},'last_name': {'required': False},'first_name': {'required': False}}