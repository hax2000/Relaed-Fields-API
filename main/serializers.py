from rest_framework import serializers
from main.models import MainTable, RelatedField1, RelatedField2, RelatedField3


class MainTableRelatedFields(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return self.queryset.model.objects.get(name=data)


class MainTableSerializerList(serializers.ListSerializer):

    def create(self, validated_data):
        records = [MainTable(**item) for item in validated_data]
        return self.child.Meta.model.objects.bulk_create(records)


class MainTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTable
        fields = '__all__'
        list_serializer_class = MainTableSerializerList

    id = serializers.IntegerField(write_only=False, required=False)
    owner = serializers.ReadOnlyField(source='owner.username')
    relfield3 = MainTableRelatedFields(queryset=RelatedField3.objects.all())
    relfield2 = MainTableRelatedFields(queryset=RelatedField2.objects.all())
    relfield1 = MainTableRelatedFields(queryset=RelatedField1.objects.all())

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
