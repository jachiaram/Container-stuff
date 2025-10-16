# Container-stuff
Repository for comparing and contrasting Docker and Podman, as well as putting together tutorials for how to deploy applications on these services. For basic Docker and Podman applications the process is the same, but the commands to build and run the images are different.

## Step-by-Step Guide:
1. Create your application
2. Select a base image and create a ```Dockerfile``` to build your application and make an image off fo the selected base image that contains everything needed to run your application.
3. Run the following Docker or Podman commands below to build the image and run the container.

## Commands for Docker and Podman
These commands are the same but either run with ```docker``` or ```podman``` depending on which you are using. I will be replacing these with ```platform``` to convey that they are the same for both platforms for the following examples.

### Image Commands:
- To build the image run: ```<platform> build -t <image-name> <directory-containing-code-and-Dockerfile>```
- List images: ```<platform> images```

### Container Commands:
- To run the container run: ```<platform> run <image-name>```
- To map ports add this flag to the run command: ```-p <host-port>:<container-port>```
- Example: ```<platform> run -p 8000:5000 <image-name>```
- To list containers: ```<platform> ps```
