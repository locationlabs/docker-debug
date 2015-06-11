from os import execv


class TailCommand(object):
    """
    Tail docker container log.
    """
    def __init__(self, inspection):
        """
        :param inspection: docker inspect output for a container.
        """
        self.inspection = inspection
        self.args = ["tail", "-f"]

    def add_log_file(self):
        self.args.append("/var/lib/docker/containers/{id}/{id}-json.log".format(
            id=self.inspection["Id"],
        ))
        return self

    @classmethod
    def build(cls, docker_client, args, extra=None):
        """
        Build the docker tail command arguments for the given container name or ID.
        """
        container = args.container

        inspection = docker_client.inspect_container(container)

        return (cls(inspection)
                .add_log_file())

    def execute(self):
        """
        Execute the command.
        """
        print "DOCKER-DEBUG:", " ".join(self.args)

        execv("tail", self.args)
