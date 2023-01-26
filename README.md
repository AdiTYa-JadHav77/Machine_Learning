# Machine_Learning

Create simple flask app

create conda env 
```p
conda create -p venv python==3.7 -y
```
activate it 
```
conda activate venv/
```

Heroku email_id = 
Heroku api key = <>
Heroku app name = ml-app-reg

create docker Img
```
docker build -t <imgName>:<tagName(latest)> 
```
note : name of the mg should be in lowercase and docker desktop should be running in background

to list docker img
```
docker images
```
to run docker img 
```
docker run -p <port>:<port> -e PORT=<port> <port_ID>
docker run -p 5000:5000 -e PORT=5000 ID
```

to check running container in docker
```
docker ps
```

to stop a docker container
```
docker stop <container_ID>
```