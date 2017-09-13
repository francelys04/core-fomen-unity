from rest_framework import serializers
from services_uf.models import UnityFoment


class UnityFomentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateField(required=True)
    value = serializers.DecimalField(required=True, max_digits=19, decimal_places=4)

    def create(self, validated_data):
        return UnityFoment.objects.create(**validated_data)

    def update(self, unity_foment, validated_data):
        unity_foment.title = validated_data.get('date', unity_foment.date)
        unity_foment.code = validated_data.get('value', unity_foment.value)
        unity_foment.save()
        return unity_foment