# API EMAIL SERVICE
# Python version
3.10

## Need .env file
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=user@domain.com
EMAIL_PASSWORD=secret
EMAIL_NAME=Custom Name

# Deploy in docker
- See .env and Dockerfile
  
- [OPTIONAL] Maybe create tar to upload in host server
````
tar -cvf mailing-service.tar --exclude='mailing-service/venv' --exclude='mailing-service/.git' mailing-service/
````
  
- [OPTIONAL] Create image specifying version x.x
````
docker build ../mailing-service/ -t mailing_service:x.x
````

- Create container
````
docker run --restart always --network network-pinnos --ip 172.124.0.12 --name mailing_service -p 9001:9001 -d mailing_service:x.x
````