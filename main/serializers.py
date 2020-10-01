from rest_framework import serializers
from main.models import MainTable, RelatedField1, RelatedField2, RelatedField3


class MainTableSerializerList(serializers.ListSerializer):

    def create(self, validated_data):
        r3_cache = {r3['name']: r3['id'] for r3 in list(RelatedField3.objects.all().values('name', 'id'))}
        r2_cache = {r2['name']: r2['id'] for r2 in list(RelatedField2.objects.all().values('name', 'id'))}
        r1_cache = {r1['name']: r1['id'] for r1 in list(RelatedField1.objects.all().values('name', 'id'))}

        data_objects = []
        for data in validated_data:
            data['relfield3_id'] = r3_cache.get(data['relfield3'])
            data['relfield2_id'] = r2_cache.get(data['relfield2'])
            data['relfield1_id'] = r1_cache.get(data['relfield1'])
            del data['relfield1'], data['relfield2'], data['relfield3']
            data_objects.append(MainTable(**data))
        bulk_created_list = MainTable.objects.bulk_create(data_objects)

        return MainTable.objects.filter(id__in=[record.id for record in bulk_created_list]).prefetch_related(
                                        'owner', 'relfield1', 'relfield2', 'relfield3')


class MainTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTable
        fields = '__all__'
        list_serializer_class = MainTableSerializerList

    id = serializers.IntegerField(write_only=False, required=False)
    owner = serializers.ReadOnlyField(source='owner.username')
    relfield3 = serializers.CharField()
    relfield2 = serializers.CharField()
    relfield1 = serializers.CharField()

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
