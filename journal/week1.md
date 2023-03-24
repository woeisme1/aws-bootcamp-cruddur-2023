# Week 1 — App Containerization

## Using Docker
###Creating a Backend
To create a dock config for backend-flask I created a file called Dockerfile and copied the following code
```
FROM python:3.10-slim-buster

# Inside Container
# Make a new folder insde container
WORKDIR /backend-flask

# Outside Container -> Inside Container
# This contains the libraries we want to install to run the app
COPY requirements.txt requirements.txt

# Inside Container
# Install the python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside Container -> Inside Container
# . means everything in current directory
# First period . - everything in /backend-flask (outside container)
# Second period . /backend-flask (inside container)
COPY . .

# Sent Environment Variables (Env Vars)
# Inside container and will remain set when the container is run
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD = Command
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

```
Next I needed to be in the project directory in order to build the container image so I did the following:
```
# This is to go back to project directory
# cd ..
```

I needed a code to run the container. The following is the easiest code that also sets the environment variables (env vars) for the container
```
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
```

This still gave a 404 error in the preview. But by adding 
```
/api/activities/home
```
at the end of the ```https://4567-woeisme1-awsbootcampcru-k6wc7tb1jid.ws-eu92.gitpod.io/``` address, I was able to get the preview to work.

This is what it looked like:
<img width="500" alt="Dockerfile build 1" src="https://user-images.githubusercontent.com/122380818/227604174-7f8ac9a3-b62a-4d57-992a-b819314f7aab.png">

###Creating a frontend
kk
