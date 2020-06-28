FROM python:3.7
WORKDIR /user/src/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
VOLUME ["/external_mount"]
CMD [ "python", "app.py"]