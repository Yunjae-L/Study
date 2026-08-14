# 가장 가볍고 표준적인 파이썬 리눅스 공식 이미지를 사용합니다.
FROM python:3.11-slim

# 컨테이너 내부에 /app 이라는 작업 폴더를 만듭니다.
WORKDIR /app

# [추가된 부분] 리눅스 공부 및 개발에 유용한 기본 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 컨테이너가 꺼지지 않고 대기하도록 설정합니다. (개발용)
CMD ["tail", "-f", "/dev/null"]


