FROM python:3.7

MAINTAINER Yoge <ygguang1992@gmail.com>

ENV TZ Asia/Shanghai

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . .

EXPOSE 8088
WORKDIR /usr/src/app/src

ENTRYPOINT ["python", "manage.py"]
