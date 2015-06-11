from mock import Mock
from nose.tools import eq_

from dockerdebug.run import RunCommand
from dockerdebug.tests.fixtures import INSPECTION, make_args


class TestRunCommand(object):

    def setup(self):
        self.docker_client = Mock(inspect_container=Mock(return_value=INSPECTION))

    def test_build(self):
        args = make_args(container="foo", command="/bin/bash")
        command = RunCommand.build(self.docker_client, args)

        expected = " ".join(["docker run --rm -it",
                             "--volume=/etc/peoples:/etc/peoples",
                             "--volume=/opt/log:/opt/log",
                             "--publish=5562:5562/tcp",
                             "docker-images.locationlabs.com/locationlabs/peoples:latest",
                             "/bin/bash"])

        actual = " ".join(command.args)

        eq_(actual, expected)
