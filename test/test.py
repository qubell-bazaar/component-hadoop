import os

from qubell.api.testing import *

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
    #meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml'))
    destroy_interval = int(os.environ.get('DESTROY_INTERVAL', 1000*60*60*2))
    apps = [
       {"name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../component-hadoop.yml')),
        "settings": {"destroyInterval": destroy_interval}},
       {"name": "Cloudera Flume",
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-flume.yml')),
        "launch": False},
       {"name": "Cloudera Hadoop",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-hadoop.yml')),
       "launch": False
       },
       {"name": "Cloudera Hive",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-hive.yml')),
       "launch": False
       },
       {"name": "Cloudera Hue",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-hue.yml')),
       "launch": False
       },
       {"name": "Cloudera Impala",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-impala.yml')),
       "launch": False
       },
       {"name": "Cloudera Manager",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-manager.yml')),
       "launch": False
       },
       {"name": "Cloudera Oozie",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-oozie.yml')),
       "launch": False
       },
       {"name": "Cloudera Pig",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-pig.yml')),
       "launch": False
       },
       {"name": "Cloudera Solr",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-solr.yml')),
       "launch": False
       },
       {"name": "Cloudera Sqoop",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-sqoop.yml')),
       "launch": False
       }
    ]
    @classmethod
    def timeout(cls):
        return 90 
    @instance(byApplication=name)
    def test_check_user_login(self, instance):
      import socket
      import requests 

      timeout = 10
      socket.setdefaulttimeout(timeout)
      url = instance.returnValues['Cloudera.manager']
      response = requests.get(url, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
      self.assertEqual(200, response.status_code)
