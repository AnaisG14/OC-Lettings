# syntax=docker/dockerfile:1

# base image
FROM python:3.8-alpine3.14

# create a directory and place into it
WORKDIR /app

# edd environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# copy the requirements.txt into app
COPY requirements.txt requirements.txt

# launch installation of requirements
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copy all content in the work directory /app
COPY . .

EXPOSE 8000

# run the application
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
# CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
