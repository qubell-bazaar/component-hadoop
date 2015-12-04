component-hadoop
================

Version 2.5-40p
-------------

<img src="http://hadoop.apache.org/images/hadoop-logo.jpg" width="100px">
<img src="http://www.uk.capgemini.com/sites/default/files/en-gb/2014/07/cloudera-logo.png" width="100px">
<img src="http://www.cloudera.com/content/dam/cloudera/support/ungated/icons/highres_236245562.jpeg" height="50px">
<img src="http://www.cloudera.com/content/dam/cloudera/support/ungated/icons/SQOOP-99d7b6cb4cccb48e.png" width="100px"> <img src="http://www.cloudera.com/content/dam/cloudera/support/ungated/icons/impala-logo.png" height="50px">
<img src="http://www.cloudera.com/content/dam/cloudera/product-assets/cloudera_search_logo.png" width="100px">

Installs and configures Cloudera Hadoop

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-hadoop/2.5-40p/meta.yml)

Features
--------

 - Install and configure Cloudera Hadoop on multiple compute

Configurations
--------------
 - Cloudera Hadoop 4.4.0, CentOS 6.4 (us-east-1/ami-ee698586, us-west-1/ami-0e073d4b), AWS EC2 m3.large, root
 - Cloudera Hadoop 5.2.0, CentOS 6.4 (us-east-1/ami-ee698586, us-west-1/ami-0e073d4b), AWS EC2 m3.large, root

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
   - Cloudera CDH and CM distribution
   - S3 bucket with Chef recipes: qubell-starter-kit-artifacts
   - If Chef is not installed: please install Chef 10.16.2 using http://www.opscode.com/chef/install.sh ```bash <($WGET -O - http://www.opscode.com/chef/install.sh) -v $CHEF_VERSION```

Implementation notes
--------------------
 - Installation is based on Chef recipes from https://github.com/qubell-bazaar/cookbook-hadoop

Configuration parameters
------------------------
 - input.repository_url: URL to cloudera archive repo
 - input.cdh_ami: Amazon AMI ID
 - input.cookbooks_url: URL to chef cookbooks tarball
 - input.datanodes: Amount of datanodes to launch
 - input.master_hardware: Amazon instance type for master node
 - input.datanode_hardware: Amazon instance type for data nodes
 - input.cloudera_hadoop_version: Hadoop version to install
 - input.cloudera_manager_version: Cloudera Manager version to install
 - input.cloudera_search_version: Cloudera Search version to install
 - input.cloudera_impala_version: Cloudera Impala version to install
 - input.metastore_root_password: Password for metastore


