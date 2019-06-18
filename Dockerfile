FROM python:3

MAINTAINER Teslenko Denis <teslenkoden@gmail.com>

EXPOSE 5002

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER nobody

CMD ["python3", "retrieval_web.py"]
