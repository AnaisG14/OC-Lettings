# syntax=docker/dockerfile:1

# base image
FROM python:3.8-alpine3.14

# create a directory and place into it
WORKDIR /app

# edd environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT 8000

# copy the requirements.txt into app
COPY requirements.txt requirements.txt

# launch installation of requirements
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copy all content in the work directory /app
COPY . .
VOLUME /app

# collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# run the application
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
