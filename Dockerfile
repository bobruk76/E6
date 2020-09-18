FROM python:3.8.5
ENV PORT 8081
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app/* /app/
COPY ./app/templates /app/templates
ENTRYPOINT ["python"]
CMD ["app.py"]
