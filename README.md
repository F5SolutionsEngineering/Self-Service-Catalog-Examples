# Self Service Catalog UDF Example

This is the simplest example provided. 
This example uses the following components from the UDF blueprint and requires the cooresponding variables:
- phpIPAM
- CFSSL
- BIG-IP Cluster

The following roles from the f5solutionsengineering/ss-cat collection are used:
- ipam_phpIPAM
- cert_cfssl
- bigip_as3_deploy
- summary

Based on the roles used for this example, you will need to describe your infrastructure.
This is done by declaring the following variables:
```yaml
---
# Required Job Variables (pass at job runtime)
deployment_state:
application_fqdn:
---
# IPAM provider Variables
ipam_url:
ipam_user:
ipam_password:
ipam_subnet:
ipam_section:
---
# CloudFlare SSL Variables
cfssl_url:
cfssl_names:
---
# BIG-IP variable
bigip_host:
bigip_user:
bigip_password:
---
# Variables that describe BIG-IP's application services
application_lb_mode:
application_pool_monitor:
application_template:
```

Variables that are sensitive in nature, such as passwords, should be encrypted.
In this simple example we've place such variables in ``secrets.yml`` and encrypted this file using Ansible Vault.




