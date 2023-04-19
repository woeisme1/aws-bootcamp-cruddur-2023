# Week 1 — App Containerization

## Using Docker
### Creating a Backend
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
docker build -t  backend-flask ./backend-flask
```
```
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
```

This still gave a 404 error in the preview. But by adding 
```/api/activities/home``` at the end of the ```https://4567-woeisme1-awsbootcampcru-k6wc7tb1jid.ws-eu92.gitpod.io/``` address, I was able to get the preview to work.

This is what it looked like:
<img width="500" alt="Dockerfile build 1" src="https://user-images.githubusercontent.com/122380818/227604174-7f8ac9a3-b62a-4d57-992a-b819314f7aab.png">

### Creating a frontend
Andy had us open up a new terminal and run ```docker ps```, this gave back:
```
gitpod /workspace/aws-bootcamp-cruddur-2023 (main) $ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                       NAMES
40af6ab9ff51   backend-flask   "python3 -m flask ru…"   21 minutes ago   Up 21 minutes   0.0.0.0:4567->4567/tcp, :::4567->4567/tcp   epic_shannon
```
Which is very cool. This shows us that we can have containers running in the background.

I went back to the original termincal, stopped the container by using CTRL^C and moved the the frontend file by doing: ```cd frontend-react-js```
Here I did a npm install ```npm i```. We have to run an  NPM Install before building the container since it needs to copy the contents of node_modules

Similar to how I did in the backend, to create the docker config for the frontend-react-js, I created a file called Dockerfile but I then copied the following code:
```
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
```

### Creating a docker-compose file
I created a file called docker-compose.yml in the main root of the project and copied the following code:
```
version: "3.8"
services:
  backend-flask:
    environment:
      FRONTEND_URL: "https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
      BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./backend-flask
    ports:
      - "4567:4567"
    volumes:
      - ./backend-flask:/backend-flask
  frontend-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js

# the name flag is a hack to change the default prepend folder
# name when outputting the image names
networks: 
  internal-network:
    driver: bridge
    name: cruddur
```
 
Docker compose allows us to run multiple containers. It does a docker build and a docker run on both of the containers we had before, whilst also config the env vars etc. To run the container you can use the command in the terminal ```docker compose up```
    or to make life super easy, right click on the docker-compose file and click "compose up"
    
Once everything was done, I check to see if it worked by clicking the public port 3000 ```https://3000-woeisme1-awsbootcampcru-k6wc7tb1jid.ws-eu92.gitpod.io```
<img width="1216" alt="Dockerfile build 2" src="https://user-images.githubusercontent.com/122380818/227614313-6cdb1f45-6290-424c-84f3-31740c46633a.png">
I played about with '''home_activites.py''' under services and changed some things to see if the compose reflected changes straight away and they did!

<img width="1113" alt="Dockerfile build 3" src="https://user-images.githubusercontent.com/122380818/227616992-60311c28-0563-4766-9607-53cdc68c8de2.png">

Of course Snopp Dogg is on my app - we will take over the world!

## Chirag Nayyar - Spending Considerations
I will not use Cloud9 or cloudtrail within this bootcamp in an effort to remain within the free tier. I set it up in week 0 and been charged a dollar for the month!

I have plenty of free hours on gitpod and codespaces that I am confident I won't go over the free tier.

## Ashish Rajan - Docker Container Security Best Practices
**What is Container Security?** The practice of protecting your applications hosted on compute services like containers. Common application examples are Single Page Applications (SPas), Microservices, APIs etc
 
**Why care about container security**
- Container First Strategy - Most apps developed as containers and easier to use and send to others without any additional needs.
- Most apps are cloud native and developed with cntainers
- reduce impact of a breach as applications and services are segregated
- Managed Container Services means that security responsibility is focussed on few things (AWS ECS & ECR)
- Automation can reduce recovery times to good state fairly easily.

**Why Container Security requires practice**
-Complexity with Containers
Relying on CSPs for features
Unmanaged requires alot more hours of work vs managed and needs you keeping updated on everything containers.


----
<img width="473" alt="Docker Components" src="https://user-images.githubusercontent.com/122380818/232757210-4f486a6f-775b-4c24-9f5b-7f979230a614.png">
![docker](https://user-images.githubusercontent.com/122380818/232829550-7c6c8eed-4314-4161-a849-4a0477937e95.svg)

**Container Security Components**


**Best Practices 0 Security**
- Keep Host and Docker updated to latest security patches
- Docker daemon and containers should run in non-root user mode
- Image Vulnerability Scanning
- Trusting a private vs public image registry
- No sensitive data in Docker files or images
- Use Secret Management Services to share secrets
- Read only File system and Volume for Docker
- Separate databases for long term storage
- Use DevSecOps practices while building app security
- Ensure all code is tested for vulnerabilities before production use.

**How to check my docker compose is secure?** 
- Use Synk and add to your Github. Import your project and scan to test for vulnerabilities in your dockerfiles (NOT images).
- AWS Secret Manager / Hashicorp Vault

**Image vulnerablities**
- Image vulnerability scanning - Amazon Inspector / Clair
