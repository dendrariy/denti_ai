#### 1. Build docker image
``` bash
docker build -t test:latest .
```
#### 2. Run tests in docker container
``` bash
docker run --rm --platform linux/amd64 test:latest
```