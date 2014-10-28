class RunCommand(object):
    """
    Builder for a docker run command.
    """
    def __init__(self, inspection, command=None):
        """
        :param inspection: docker inspect output for a container.
        :param command: command to execute at runtime (optional).
        """
        self.inspection = inspection
        self.command = command
        self.args = ["docker", "run", "--rm", "-it"]

    def add_volumes(self):
        for src, dst in self.inspection["Volumes"].items():
            self.args.append("--volume={}:{}".format(src, dst))
        return self

    def add_ports(self):
        for port, bindings in self.inspection["HostConfig"]["PortBindings"].items():
            for binding in bindings:
                self.args.append("--publish={}:{}".format(binding["HostPort"], port))
        return self

    def add_image(self):
        self.args.append(self.inspection["Config"]["Image"])
        return self

    def add_command(self):
        if self.command:
            self.args.append(self.command)
        return self

    @classmethod
    def for_container(cls, docker_client, container, command=None):
        """
        Build the docker run command arguments for the given container name or ID.
        """
        inspection = docker_client.inspect_container(container)
        return (cls(inspection, command)
                .add_volumes()
                .add_ports()
                .add_image()
                .add_command())
