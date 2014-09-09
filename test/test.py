import os

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values

@environment({
    "default": {},
    #"AmazonEC2_CentOS_63": {
    #    "policies": [{
    #        "action": "provisionVms",
    #        "parameter": "imageId",
    #        "value": "us-east-1/ami-eb6b0182"
    #    }, {
    #        "action": "provisionVms",
    #        "parameter": "vmIdentity",
    #        "value": "root"
    #    }]
    #}
})
class ClouderaHadoopComponentTestCase(BaseComponentTestCase):
    name = "component-hadoop"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]
    @classmethod
    def timeout(cls):
        return 60
    @instance(byApplication=name)
    @values({"Management.Manager": "hosts"})
    def test_port(self, instance, hosts, port=7180):
        import socket
        import time
        time.sleep(60)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hosts, int(port)))

        assert result == 0
