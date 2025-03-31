from rest_framework import serializers
from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 
                    'titulo', 
                    'descricao', 
                    'status',
                    'data_criacao', 
                    'data_atualizacao', 
                    'data_conclusao'
                ]

    def update(self, instance, validated_data):
        # Atualiza data_conclusao se status mudar para concluído
        if validated_data.get('status') == 'C' and instance.status != 'C':
            validated_data['data_conclusao'] = timezone.now()
        elif validated_data.get('status') != 'C' and instance.status == 'C':
            validated_data['data_conclusao'] = None
            
        return super().update(instance, validated_data)