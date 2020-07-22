FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# enabling shell to dyno
COPY heroku-exec.sh /app/.profile.d
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# collect static files
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate
# run gunicorn
RUN useradd -m sogeouser
USER sogeouser
CMD bash /app/.profile.d/heroku-exec.sh && gunicorn sogeo.wsgi:application --bind 0.0.0.0:$PORT