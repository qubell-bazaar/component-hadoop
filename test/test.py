import os

from qubell.api.testing import *
from qubell.api.tools import retry

def eventually(*exceptions):
    """
    Method decorator, that waits when something inside eventually happens
    Note: 'sum([delay*backoff**i for i in range(tries)])' ~= 580 seconds ~= 10 minutes
    :param exceptions: same as except parameter, if not specified, valid return indicated success
    :return:
    """
    return retry(tries=50, delay=0.5, backoff=1.1, retry_exception=exceptions)

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
    destroy_interval = int(os.environ.get('DESTROY_INTERVAL', 1000*60*60*2))
    #meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml'))
    apps = [
       {"name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../component-hadoop.yml')),
        "settings": {"destroyInterval": 14400000}},
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
       {"name": "Cloudera Yarn",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-yarn.yml')),
       "launch": False
       },
       {"name": "Cloudera Spark",
       "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../cloudera-spark.yml')),
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
      
      @eventually(AssertionError)
      def eventually_assert():
        response = requests.get(url, auth=requests.auth.HTTPBasicAuth('admin', 'admin'))
        self.assertEqual(200, response.status_code)
      eventually_assert()
