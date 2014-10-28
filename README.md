# docker-debug

Docker container debugging tool

## Installation

    pip install docker-debug

## Usage

docker-debug is a command line tool to make it easy to debug docker containers.

The `run` command will inspect (using docker inspect) the given container name or ID
and run `docker run` with the correct arguments, mimicking the upstart run args for
the container, but drop to a shell so you can run debug commands, like running
your web server in debug/development mode.

    root@host:~# docker-debug run mycontainer
    [ root@97e9a00468e6:/ ]$
