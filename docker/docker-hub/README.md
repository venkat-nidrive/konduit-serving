# Steps to run 
1. Copy konduit.jar into konduit.serving/docker/docker-hub
2. Build the docker image with the command  
`
docker build -t konduit-serving .
`
3. Run the docker with the command  
`
docker run -it --rm konduit-serving  
`  
Parameters: 
    -d: detached mode
    -p portTo:portFrom Example: 


Note:  
1. To enter the file system of the docker image, enter the following command
`
docker run -it --rm konduit-serving bash
`
2. To remove the docker image, enter the following command  
`
docker rmi konduit-serving -f 
`