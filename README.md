# Docker Scheduler V1.0 BETA

## Concept: 
Build an API and CLI that interfaces with Docker to assist in scheduling helper tasks in a cron like way.

### Current Status 

Using python and the docker python library I have started a building out the API and CLI for this project. 

In the current build of Docker Scheduler we have following commands available (the below output can be seein the help as well.):

    list images - to list all the images available
    list containers - to list all the cointainers running
    run <image_type> <command> - to run an image with a specific command
    help - displays this output.             
    Example :
    
    python docker_scheduler_cli.py run 'ubuntu:latest' 'echo hello world'

## Future Releases
The plan for this project is to elaborate on controlling the containers once they have been started, allowing the containers to be restarted  rerunning their command just like a cron task on a linux machine. Another feature I would like to add is to being able to delete containers once created. 

Below are few Ideas I have for implementing the scheduling feature for this project. 

#### Possible Solution 1 : Docker Containers within a Docker container.
Constructing a docker container that runs and controls the recurring containers. The hope with this approach is to encapsulate all processing inside of a massive docker container. My initial thoughts on devising a system to keep track of the recurring containers was building a process that is constantly running and keeps track of each container possibly using a database.

I'll be the first to admit this solution may work but may have too much overhead. 

A better solution might be using the "outer" containers crontab to control when a container is relaunched, using the CLI already built.

#### Possible Solution 2 :   Kubernetes or Docker Swarm

While working on this project I did some research on how kubernetes could help me orchestrate these containers. A quick search showed that kubernetes natively handles scheduling of jobs with the use rof "Cron Jobs" (https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/). Given a little extra time I think I could have used something like this to facilitate the short lived tasks feature of this project.

Alternatively I could also use Docker Swarm's Scheduling services. Similar to kubernetes Docker Swarm is Docker's container orchestration system. It's possible this might be a better solution, as my current application already works with docker.

### Testing

Given more time I would have liked to implemented much more unittesting. Especially with regards to the CLI, and the data being sent to the API. It is quite easy to input the wrong parameters into the CLI the CLI will break.



## Setup

First steps in setting up this application is to install the necessary packages and libraries. 

****NOTE: You may want to create a virtual environment for this repo****

    pip install -r requirements.txt
    
You will need to also install  docker desktop, you can download it here : https://www.docker.com/products/docker-desktop

Following the instructions on the website for which ever operating system you have.

When Docker is finished installed  we should be all set to start using the Docker Scheduler! 

To get a list of all images try :

    python docker_scheduler_cli.py list images

Your output may look like this :

    [<Image: 'alpine:latest'>, <Image: 'hello-world:latest'>, <Image: 'ubuntu:latest'>]
    
To run a new container :

    python docker_scheduler_cli.py run 'ubuntu:latest' 'echo hello world'
    

Your output should look like :
 
    hello world

Lastly to see all running containers:

    python docker_scheduler_cli.py list containers

Your output should look like this (If you have containers still running):

    [<Container: e599e9513a>]
       


    

    
   
    

