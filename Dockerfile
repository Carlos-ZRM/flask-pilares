FROM python:3.6
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY pilares/ .

EXPOSE 5000 5001

CMD [ "python", "./app.py" ]
