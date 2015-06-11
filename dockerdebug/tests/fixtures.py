class Args(object):
    pass


def make_args(**kwargs):
    args = Args()
    for key, value in kwargs.iteritems():
        setattr(args, key, value)
    return args


INSPECTION = {
    u'HostsPath': u'/var/lib/docker/containers/ebd564e818c5c320828e4ff0c19079dcbfe509c438ce0e273a6962cd16b56fbe/hosts',  # noqa
    u'Created': u'2014-10-22T23: 47: 58.969872756Z',
    u'Image': u'f2fac5e93165b7cd208d2860391aa6bdc266f12bc23be8d68dc7311a151d8426',
    u'Args': [
        u'uwsgi',
        u'--ini',
        u'/opt/peoples/etc/uwsgi.ini'
    ],
    u'Driver': u'aufs',
    u'HostConfig': {
        u'CapDrop': None,
        u'PortBindings': {
            u'5562/tcp': [
                {
                    u'HostPort': u'5562',
                    u'HostIp': u''
                }
            ]
        },
        u'NetworkMode': u'bridge',
        u'Links': None,
        u'LxcConf': [
        ],
        u'ContainerIDFile': u'',
        u'Devices': [
        ],
        u'CapAdd': None,
        u'Binds': [
            u'/etc/peoples: /etc/peoples'
        ],
        u'RestartPolicy': {
            u'MaximumRetryCount': 0,
            u'Name': u''
        },
        u'PublishAllPorts': False,
        u'Dns': None,
        u'ExtraHosts': None,
        u'DnsSearch': None,
        u'Privileged': False,
        u'VolumesFrom': [
            u'log-data'
        ]
    },
    u'MountLabel': u'',
    u'VolumesRW': {
        u'/etc/peoples': True,
        u'/opt/log': True
    },
    u'State': {
        u'Pid': 3229,
        u'Paused': False,
        u'Running': True,
        u'FinishedAt': u'2014-10-23T01: 32: 34.504295513Z',
        u'Restarting': False,
        u'StartedAt': u'2014-10-23T21: 57: 52.24757222Z',
        u'ExitCode': 0
    },
    u'ExecDriver': u'native-0.2',
    u'ResolvConfPath': u'/var/lib/docker/containers/ebd564e818c5c320828e4ff0c19079dcbfe509c438ce0e273a6962cd16b56fbe/resolv.conf',  # noqa
    u'Volumes': {
        u'/etc/peoples': u'/etc/peoples',
        u'/opt/log': u'/opt/log'
    },
    u'Path': u'/opt/peoples/bin/run.sh',
    u'HostnamePath': u'/var/lib/docker/containers/ebd564e818c5c320828e4ff0c19079dcbfe509c438ce0e273a6962cd16b56fbe/hostname',  # noqa
    u'ProcessLabel': u'',
    u'Config': {
        u'Env': [
            u'PATH=/usr/local/sbin: /usr/local/bin: /usr/sbin: /usr/bin: /sbin: /bin',
            u'HOME=/root',
            u'PEOPLES_SETTINGS=/etc/peoples/peoples.conf'
        ],
        u'Hostname': u'ebd564e818c5',
        u'Entrypoint': [
            u'/opt/peoples/bin/run.sh'
        ],
        u'PortSpecs': None,
        u'Memory': 0,
        u'OnBuild': None,
        u'OpenStdin': False,
        u'Cpuset': u'',
        u'User': u'',
        u'CpuShares': 0,
        u'AttachStdout': True,
        u'NetworkDisabled': False,
        u'WorkingDir': u'',
        u'Cmd': [
            u'uwsgi',
            u'--ini',
            u'/opt/peoples/etc/uwsgi.ini'
        ],
        u'StdinOnce': False,
        u'AttachStdin': False,
        u'MemorySwap': 0,
        u'Volumes': None,
        u'Tty': False,
        u'AttachStderr': True,
        u'Domainname': u'',
        u'Image': u'docker-images.locationlabs.com/locationlabs/peoples:latest',
        u'SecurityOpt': None,
        u'ExposedPorts': {
            u'5562/tcp': {
            }
        }
    },
    u'Id': u'ebd564e818c5c320828e4ff0c19079dcbfe509c438ce0e273a6962cd16b56fbe',
    u'NetworkSettings': {
        u'MacAddress': u'02: 42: ac: 11: 00: 11',
        u'Bridge': u'docker0',
        u'PortMapping': None,
        u'IPPrefixLen': 16,
        u'IPAddress': u'172.17.0.17',
        u'Gateway': u'172.17.42.1',
        u'Ports': {
            u'5562/tcp': [
                {
                    u'HostPort': u'5562',
                    u'HostIp': u'0.0.0.0'
                }
            ]
        }
    },
    u'Name': u'/peoples'
}
