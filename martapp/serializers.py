from rest_framework import serializers
class PostSerializers(serializers.Serializer):
    video=serializers.FileField()
  