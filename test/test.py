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
    name = "CDH Main"
    meta = "https://raw.githubusercontent.com/qubell-bazaar/component-hadoop/components/meta.yml"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../component-hadoop.yml'))
    }]
    @classmethod
    def timeout(cls):
        return 60
    @instance(byApplication=name)
    @values({"Cloudera.Manager_URL": "url"})
    def test_check_user_login(self, instance, url):
      import socket
      import requests 

      timeout = 10
      socket.setdefaulttimeout(timeout)
      response = requests.get(url, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
      self.assertEqual(200, response.status_code)
