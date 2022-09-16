FROM python:3.9.12

WORKDIR /home/

RUN git clone https://github.com/akfangus/pycharmbegin.git

WORKDIR /home/pycharmbegin/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-=#67(@)o2s=d)l$c^kr$of8jkr7f^2)i#b+901fu%s)@1y2b6v" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn" , "pragmatic.wsgi" , "--bind" , "0.0.0.0:8000"]