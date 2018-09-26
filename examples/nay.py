// START NAYHEADER OMIT
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Sergi Jimenez <sjr@redhat.com>
# Apache License, Version 2.0
# (see LICENSE or http://www.apache.org/licenses/LICENSE-2.0)

ANSIBLE_METADATA = {"metadata_version": "1.1",
                    "status": ["preview"],
                    "supported_by": "community"}
// END NAYHEADER OMIT

// START NAYBLOCKS OMIT
DOCUMENTATION = '''
module: nay
short_description: The nay module.
description: Say nay to any question passed.
version_added: "2.7"
author: Sergi Jimenez (@tripledes)
options:
    question:
        description: Question being asked to the nay module.
        required: true
'''
EXAMPLES = '''
- name: Emacs
  nay:
      question: Do you like Emacs?
'''
RETURN = '''
question:
    description: user's question
    returned: always
    sample: "Do you like Emacs?"
answer:
    description: the naysayer answer
    returned: success
    sample: "humf...Nay!!!"
'''
// END NAYBLOCKS OMIT

from ansible.module_utils.basic import AnsibleModule


// START NAYCODE OMIT
argument_spec=dict(
    question=dict(type='str', required=True),
)

def setup_module_object():
    module = AnsibleModule(argument_spec=argument_spec)
    return module

def main():
    ''' module entry point '''
    module = setup_module_object()

    res = dict()

    res["answer"] = "humf...Nay!!!"
    res["question"] = module.params.get("question")

    if not res.get("question"):
        # This is just for reference, not really needed as question is declared
        # as required
        module.fail_json(
            msg="That ain't a question mate!"
        )

    module.exit_json(**res)
// END NAYCODE OMIT


if __name__ == '__main__':
    main()
