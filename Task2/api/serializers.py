from rest_framework import serializers

from .models import *



class TaskSerializer(serializers.ModelSerializer):
    class Meta:

        model=Task
        fields=['appname','subcategoryname','points','categoryname','appsubcategory']
        