FROM python:3.9.0

WORKDIR /home/

RUN echo '3wswAsrr'

RUN git clone https://github.com/kohsmic8/test33.git

WORKDIR /home/test33

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=test33.settings.deploy && python manage.py migrate --settings=test33.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=test33.settings.deploy test33.wsgi --bind 0.0.0.0:8000"]