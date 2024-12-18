FROM python:3.12.3-slim as builder

RUN mkdir /install
WORKDIR /install

RUN apt-get update \
    && apt-get install git -y \
    && apt-get install -y --reinstall ca-certificates \
    && pip install pipenv
#    && pip install toml


COPY requirements.txt .
RUN pip install --prefix=/install --ignore-installed -r requirements.txt


FROM python:3.12.3-slim

ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /home/tuandc

WORKDIR /home/tuandc
COPY --from=builder /install /usr/local
COPY . .
#COPY supervisord.conf /etc/supervisor/supervisord.conf

RUN sed -i -e 's/\r$//' entry-point.sh
RUN chmod +x entry-point.sh


EXPOSE 8000

ENTRYPOINT ["./entry-point.sh"]
