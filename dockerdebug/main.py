"""
Debug a docker container.
"""

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from docker.client import Client

from dockerdebug.run import RunCommand
from dockerdebug.tail import TailCommand


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
    run_parser.set_defaults(func=RunCommand.build)

    tail_parser = subparsers.add_parser("tail",
                                        formatter_class=ArgumentDefaultsHelpFormatter,
                                        help="tail docker container stdout/stderr log")
    tail_parser.add_argument("container",
                             help="Container name to tail")
    tail_parser.set_defaults(func=TailCommand.build)

    args, extra = parser.parse_known_args()

    # connect to Docker
    client = Client()

    # build the command for the container
    command = args.func(client, args, extra)

    # execute the command
    command.execute()
