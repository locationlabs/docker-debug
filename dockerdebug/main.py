"""
Debug a docker container.
"""

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from os import execv

from docker.client import Client

from dockerdebug.run import RunCommand


def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers()

    run_parser = subparsers.add_parser("run",
                                       formatter_class=ArgumentDefaultsHelpFormatter,
                                       help="run a new docker container based on an existing one")
    run_parser.add_argument("container",
                            help="Container name to debug")
    run_parser.add_argument("--command",
                            default="/bin/bash",
                            help="command to execute at runtime")

    args, extra = parser.parse_known_args()

    # connect to Docker
    client = Client()

    # build the run command for the container
    command = RunCommand.for_container(client, args.container, args.command)

    print "DOCKER-DEBUG:", " ".join(command.args)

    # execute the command
    execv("/usr/bin/docker", command.args)
