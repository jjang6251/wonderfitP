from django.shortcuts import render
# from rest_framework import viewsets
from .serializer import UserSerializer
from django.contrib.auth.models import AbstractUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# -> viewsets
# 간결한 코드: 비슷한 동작을 하는 API 엔드포인트들을 하나의 클래스로 묶어 관리할 수 있습니다.
# 일반적인 작업의 자동화: 표준적인 CRUD 작업이 자동으로 구현되어 개발자가 각각의 기능을 직접 작성할 필요가 없습니다.
# RESTful API의 쉬운 관리: HTTP 메서드(GET, POST, PUT, DELETE 등)에 대한 처리를 간소화하여 관리합니다.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = AbstractUser.objects.all() 
#     # -> 데이터베이스에서 모든 사용자 정보를 가져와 queryset에 저장합니다. 이 정보는 API 엔드포인트에 접근하여 사용됩니다.
#     serializer_class = UserSerializer
#     # -> UserSerializer 클래스를 지정하여 시리얼라이저로 사용합니다. 이는 데이터베이스의 사용자 정보를 JSON 또는 다른 형식으로 변환할 때 사용됩니다.

class SignUpAPIView(APIView):
        def post(self, request):
            # POST 요청을 통해 전달된 데이터로 UserSerializer를 초기화합니다.
            serializer = UserSerializer(data=request.data)
            
            # Serializer의 is_valid 메서드를 사용하여 데이터의 유효성을 검사합니다.
            if serializer.is_valid():
                # Serializer의 save 메서드를 호출하여 유효한 데이터로부터 사용자를 생성하고 저장합니다.
                user = serializer.save()
                
                # 회원가입이 성공적으로 이루어졌음을 나타내는 응답을 반환합니다.
                return Response({'message': '회원가입 성공!'}, status=status.HTTP_201_CREATED)
            
            # 유효성 검사에서 실패한 경우, Serializer의 errors를 반환하여 에러를 포함한 응답을 반환합니다.
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)