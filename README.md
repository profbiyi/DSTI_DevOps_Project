# DSTI_DevOps_Project
This project is strictly about devops and it has different part. Each part has there own read me. There is a tree towards the end of this readme to give an idea about how each part of this project is structured.


 ## Project Structure

 ```

├───.circleci
├           └─── config.yml
├───src
├     └─── appy.py
├     └─── test.py
├     └─── README.md
├     └─── images
├               └─── post.PNG
├               └─── post2.PNG
├               └─── get_1.PNG
├               └─── get_all.PNG
├
├───docker_docker_compose
├                        └─── Dockerfile
├                        └─── docker-compose.yml
├
├───k8s
├    └─── flask_k8_service.yml
├    └─── flask-api-deployment.yml
├    └─── minikube_start.PNG
├    └─── minikube_status.PNG
├
├───istio
├
├───gitignore
├───gitattributes
├───Procfile
├───README.md
├───requirements.txt
└───runtime

 ```


### 1. Python Create, Read, Update and Delete (CRUD) API
A simple crud api built with (flask) python and mysql database. Initially, A docker image for mysql was used and port 3307 was opened.
But later an online free mysql database was provisioned using [Free Online MySQL](https://remotemysql.com/).


### 2. CI/CD pipeline with CircleCI and Heroku

CI was configure with [CirceCI](https://app.circleci.com/pipelines/github/profbiyi). and CD with [Heroku](https://dashboard.heroku.com/pipelines/2e419849-9de8-42c0-b07e-13eb980d4f27/). I went for this option as it gives me an opportunity to test out different tools. 

The home page of this api [Homepage](https://dstistudents.herokuapp.com/)



### 3. Docker and Docker Compose
A `Dockerfile` and `docker-compose.yml` to build the applciation and then to start it.

A docker image was created, tagged and successfully hosted on [profbiyi/mydstistudents_crud_api](https://hub.docker.com/repository/docker/profbiyi/mydstistudents_crud_api). To use the image, ensure that ports 5000, and 3306 are openned and connect to the app using localhost:5000


### 4. Kubernetes

1. Install Kubernetes cluster using Minikube
2. Create a Kubernetes Manifest yaml files:
  - deployments
  - services

### 5. Make a service mesh using Istio

1. Deploy your application using Istio
2. Create configuration:
  - route requests between 2 different versions of your app
  - traffic shifting between 2 different versions of your app

