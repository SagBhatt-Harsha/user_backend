from rest_framework import serializers
from apps.users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    def validate_gender(self, value):
        value = value.upper()

        if value not in ['M','F','O']:
            raise serializers.ValidationError("Please Input m/M, f/F or o/O for gender")
        
        return value
    
    def validate_age(self, value):
        if value > 100:
            raise serializers.ValidationError("Please Input Correct Age")
        return value
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ["unique_id", "created_on"]
