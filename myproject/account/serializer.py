from .models import CustomUser
from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'age', 'email')
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
            age = validated_data.get('age')
            
            # 여기서 age만 get을 사용하는 이유는 age 필드가 요청 데이터에 존재하지 않는 다면 username과 같이 가져오면 에러를 일으킬 수 있다. 그래서 get과 같이 사용하면 해당 키가 없을 때 기본값을 반환하거나 아무것도 반환하지 않기 때문에 안전하게 데이터를 가져올 수 있다.
        )
        return user
    