from typing import Tuple

from rest_framework import serializers

from assignment.models import Boss, Employee


class BossSerializer(serializers.ModelSerializer):

    class Meta:
        model = Boss
        fields = Tuple = (
            '__all__'
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields: Tuple = (
            '__all__'
        )
