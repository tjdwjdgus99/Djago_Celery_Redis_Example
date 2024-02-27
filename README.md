# Djago_Celery_Redis_Example
Djago_Celery_Redis 예제 소스코드

## Reference link : https://velog.io/@tjdwjdgus99/Django-Celery-Redis%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%B9%84%EB%8F%99%EA%B8%B0%EC%8B%9D-%EC%9E%91%EC%97%85

### 실행순서<br>
1.Redis 실행<br>
2.Celery Worker 실행<br>
3.Django 실행<br>

## For Windows10

### (1) Redis 실행
(Redis 설치 후)

	redis-server

### (2) Celery Worker 실행

(새 CMD 창 실행 및 가상환경 접속 후)

	celery -A config worker --pool=solo -l info

### (3) Django 실행

(새 CMD 창 실행 및 가상환경 접속 후)

	python manage.py runserver


## For Linux(Ubuntu)


### (1) Redis 실행
(Redis 설치 후)

	redis-server

### (2) Celery Worker 실행

(새 CMD 창 실행 및 가상환경 접속 후)

	celery -A config worker -l info

### (3) Django 실행

(새 CMD 창 실행 및 가상환경 접속 후)

	python manage.py runserver
