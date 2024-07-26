FROM quay.io/centos/centos:stream8

RUN "dnf install -y python3"
WORKDIR /myportfolio

COPY . .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"] 12
EXPOSE 5000