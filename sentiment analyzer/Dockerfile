FROM python:3.7

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["setup.py"]
#CMD ["python", "setup.py"]

