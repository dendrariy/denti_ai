#### 1. Build docker image
``` bash
docker build -t test:latest .
```
#### 2. Run tests in docker container
``` bash
sudo docker run -v $PWD/:/app/reports/ --rm --platform linux/amd64 test:latest
```
