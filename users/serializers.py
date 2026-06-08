from rest_framework import serializers

from .models import User
from .models import Department
from .models import Role

class DepartmentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Department
        
        fields = [
            "id",
            "name"
        ]
    
class RoleSerializer(serializers.ModelSerializer):
     class Meta:
        model = Role
        
        fields = [
            "id",
            "name"
        ]    
    
class UserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    roles = RoleSerializer(many=True, read_only=True)
    
    class Meta:
        model = User

        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "roles",
            "is_active",
            "created_at",
        ]