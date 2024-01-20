# wonderfitP

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
python -m venv myenv       # 가상환경 생성
source myenv/bin/activate  # 가상환경 활성화 (윈도우에서는 'myenv\Scripts\activate')

pip install django

django-admin startproject myproject

cd myproject
python manage.py runserver
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<jwt 토큰>
pip install djangorestframework

pip install djangorestframework-simplejwt
-> djangorestframework-jwt도 있지만 업데이트가 진행되지 않아서 simplejwt를 사용한다.

pip install django-allauth

pip install dj-rest-auth
-> 소셜 로그인 및 유저 관리 패키지에 관한 django-rest-auth에서 따로 fork된 패키지이다. 이것 또한 더이상 업데이트가 되지 않는다.

![Alt text](image.png)
