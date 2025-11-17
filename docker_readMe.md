## First create docker file named as

Dockerfile

## build image

docker build -t fastapi_a .

## for checking images

docker images

## going inside container bash (to exit: ctrol+d)

docker run --rm -it -p 8000:8000 fastapi_a bash

## Under bash we can run like below 
uvicorn app.main:app --host 0.0.0.0

## to check container
docker ps -a

## to remove images 
docker rmi fastapi_a

## to remove all images
docker rmi $(docker images -q) -f


## to build and run directly from compose.yml 
docker compose up --build

