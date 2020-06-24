# UDF-Example1

This is the simplest example provided. 
This example uses the following components from the UDF blueprint and requires the cooresponding variables:
- phpIPAM
- CFSSL
- BIG-IP Cluster

The following roles from the f5solutionsengineering/ss-cat collection are used:
- ipam_phpIPAM
- cert_cfssl
- bigip_as3_deploy

Based on the roles used, the following variables are required:
```yaml
---
ipam_url
ipam_user
ipam_password
ipam_subnet
ipam_section
---
nios_host
nios_ipv4_network
nios_user
nios_password
---
cfssl_url
cfssl_names
---
bigip_host
bigip_user
bigip_password
bigip_as3_template
```

Note that different variables will be required depending on what roles are required by your playbook.


  phpipam_freeip:
    username: admin
    password: secret
    url: 'http://ipam.domain.tld/api/app/'
    subnet: '192.168.10.0/24'
    section: ansible-section
    description: 'Optional description'
  register: new_ip