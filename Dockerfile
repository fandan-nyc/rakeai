FROM public.ecr.aws/amazonlinux/amazonlinux:2023

COPY ./rakeai /rakeai

RUN yum install -y java-1.8.0-amazon-corretto-1:1.8.0_362.b08-1.amzn2023.x86_64 \
    python3-3.9.16-1.amzn2023.0.3.x86_64 \
    python-pip

RUN cd /rakeai \
    && pip install -r requirements.txt

WORKDIR  /rakeai

CMD ["/usr/bin/python3","test.py"]
