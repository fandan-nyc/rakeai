FROM python:3.8

# ADD sources.list /etc/apt/sources.list
RUN apt update && apt install -y default-jre

RUN mkdir /api
COPY app /api/app
# COPY model /api/model # use s3 instead of local folder
COPY util /api/util
COPY __init__.py /api/__init__.py
# 
WORKDIR /api

# 
RUN pip install --upgrade pip
# RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir --upgrade -r app/requirements.txt --root-user-action=ignore
RUN pip install --upgrade -r app/requirements.txt --root-user-action=ignore

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
