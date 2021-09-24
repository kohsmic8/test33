FROM python:3.9.0

WORKDIR /home/

RUN echo '3wwdssrr'

RUN git clone https://github.com/kohsmic8/test33.git

WORKDIR /home/test33

RUN echo "SECRET_KEY=django-insecure-!(k1r4z^g=t0n!e+v4!98ihh1$bj2t+(u$mrie37!3w(1sulcp" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=test33.settings.deploy && python manage.py migrate --settings=test33.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=test33.settings.deploy test33.wsgi --bind 0.0.0.0:8000"]