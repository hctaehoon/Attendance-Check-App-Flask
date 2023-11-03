# Python 3.9 이미지를 기반으로 한다
FROM python:3.9

# 작업 디렉토리를 설정한다
WORKDIR /myapp

# 필요한 모듈이 설치된 requirements.txt를 Docker 컨테이너 내부로 복사한다
COPY requirements.txt requirements.txt

# requirements.txt에 명시된 패키지들을 설치한다
RUN pip install -r requirements.txt

# 현재 디렉토리의 모든 파일과 폴더를 Docker 컨테이너의 /myapp 디렉토리에 복사한다
COPY . .

# Gunicorn을 이용하여 Flask 애플리케이션을 실행한다
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]
