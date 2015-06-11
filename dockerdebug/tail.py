from os import execv


class TailCommand(object):
    """
    Tail docker container log.
    """
    def __init__(self, inspection, flags):
        """
        :param inspection: docker inspect output for a container.
        """
        self.inspection = inspection
        self.flags = flags
        self.args = ["tail"]

    def add_tail_flags(self):
        if self.flags:
            self.args.extend(self.flags)
        return self

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

        return (cls(inspection, extra)
                .add_tail_flags()
                .add_log_file())

    def execute(self):
        """
        Execute the command.
        """
        print "DOCKER-DEBUG:", " ".join(self.args)

        execv("/usr/bin/tail", self.args)
