from mock import Mock
from nose.tools import eq_

from dockerdebug.tail import TailCommand
from dockerdebug.tests.fixtures import INSPECTION, make_args


class TestRunCommand(object):

    def setup(self):
        self.docker_client = Mock(inspect_container=Mock(return_value=INSPECTION))

    def test_build(self):
        args = make_args(container="foo")
        command = TailCommand.build(self.docker_client, args)

        expected = " ".join(
            ["tail",
             "-f",
             "/var/lib/docker/containers/ebd564e818c5c320828e4ff0c19079dcbfe509c438ce0e273a6962cd16b56fbe/ebd564e818c5c320828e4ff0c19079dcbfe509c438ce0e273a6962cd16b56fbe-json.log"],  # noqa
        )

        actual = " ".join(command.args)

        eq_(actual, expected)
