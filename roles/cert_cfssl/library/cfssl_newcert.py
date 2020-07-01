#!/usr/bin/python

# Copyright: (c) 2020, Kevin Reynolds<k.reynolds@f5.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# TBD:
# handle formatting
# add key algo and bit length


ANSIBLE_METADATA = {
    'metadata_version': '0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: cfssl_newcert

short_description: Obtain a cert and key from a running CFSSL instance.

version_added: "2.9"

description:
    - "This module requires a running CFSSL instance with the REST API running (ie. `serve` command). "

options:
    names:
      description: 
        - The Subject Alternate Names (SANs) for the certificate.
    common_name:
      description:
        - The Common Name for the certificate
    hosts:
      description:
        - something
    cfssl_url:
      description:
        - Protocol and URL for the CFSSL instance
    validate_certs:
      description:
        - If using https, 
author:
    - Kevin Reynolds (@kreynoldsf5)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_test:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
    returned: always
message:
    description: The output message that the test module generates
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import requests

def run_module():
    module_args = dict(
        names=dict(type='list', required=True),
        common_name=dict(required=True),
        hosts=dict(type='list', required=True),
        cfssl_url=dict(required=True),
        response_format=dict(default='cfssl', choices=['cfssl', 'as3']), #newline char or not?
        validate_certs=dict(type='bool', default=True),
        state=dict(default='present', choices=['present', 'absent'])
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    names = module.params['names']
    common_name = module.params['common_name']
    hosts = module.params['hosts']
    cfssl_url = module.params['cfssl_url']
    response_format = module.params['response_format']
    validate_certs = module.params['validate_certs']
    state = module.params['state']

    url = cfssl_url + '/api/v1/cfssl/newcert'

    payload = {
        'request': {
            'CN': common_name,
            'names': names,
            'hosts': hosts,
        }
    }

    if state is 'absent':
        module.exit_json(**result)

    try:
        response = requests.post(url, json=payload, verify=validate_certs)
        if response.status_code != 200 and not response.json()['success']:
            module.fail_json(msg='Module execution failed: {0}'.format(response['errors']), **result)
        jresponse = response.json()
        result['cert'] = jresponse['result']['certificate'].encode("unicode_escape").decode("utf-8")
        result['key'] = jresponse['result']['private_key'].encode("unicode_escape").decode("utf-8")
        result['cert_request'] = jresponse['result']['certificate_request'].encode("unicode_escape").decode("utf-8")
        result['sums'] = jresponse['result']['sums']
        result['messages'] = jresponse['messages']
        result['changed'] = True
        module.exit_json(**result)
    except Exception as e:
        module.fail_json(msg='Module execution failed: {0}'.format(e), **result)

def main():
    run_module()

if __name__ == '__main__':
    main()