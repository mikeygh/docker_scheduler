import docker


class DockerScheduler (object):

    def __init__(self):
        self.client = docker.from_env()

    def list_images(self):

        return self.client.images.list()

    def list_containers(self):

        return self.client.containers.list()

    def run_container(self, image, command ):

        return self.client.containers.run(image, command)



