from mock import Mock
from nose.tools import eq_

from dockerdebug.run import RunCommand
from dockerdebug.tests.fixtures import INSPECTION


class TestRunCommand(object):

    def setup(self):
        self.docker_client = Mock(inspect_container=Mock(return_value=INSPECTION))

    def test_build(self):
        command = RunCommand.for_container(self.docker_client, "foo", "/bin/bash")

        expected = " ".join(["docker run --rm -it",
                             "--volume=/etc/peoples:/etc/peoples",
                             "--volume=/opt/log:/opt/log",
                             "--publish=5562:5562/tcp",
                             "docker-images.locationlabs.com/locationlabs/peoples:latest",
                             "/bin/bash"])

        actual = " ".join(command.args)

        eq_(actual, expected)
