FROM python:3.6
RUN apt-get update -y
RUN apt-get install vim  net-tools telnet nmap traceroute -y
WORKDIR /usr/src/app/pilares

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000 5001

#CMD [ "python", "./app.py" ]
