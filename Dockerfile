FROM python:3.8.5
ENV PORT 8081
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./app/*.py /app/
ENTRYPOINT ["python"]
CMD ["app.py"]
