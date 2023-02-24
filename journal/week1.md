# Week 1 — App Containerization

```
FROM python:3.10-slim-buster

#Inside Container
#Make a new folder inside the container
WORKDIR /backend-flask

#Outside container -> Inside Container
# this contains the libraries you want to install to the app
COPY requirements.txt requirements.txt

#Inside Container
#Install the python libraries used for the app
RUN pip3 install -r requirements.txt

#Outside Container -> Inside Container
# . Means everything in the current directory
# first period . - / everything in /backend-flask (outside container)
# second period . - /backend-flask (inside container)
COPY . .

# Set Environment Variables (Env Vars)
#Set inside container and remain set when container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD (COMMAND)
#m = module to run flask
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```
