FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# collect static files
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
# run gunicorn
RUN useradd -m sogeouser
USER sogeouser
CMD gunicorn sogeo.wsgi:application --bind 0.0.0.0:$PORT