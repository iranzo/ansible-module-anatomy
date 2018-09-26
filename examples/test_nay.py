import json
import sys
import pytest

from ansible.module_utils._text import to_bytes
from ansible.module_utils import basic

// START UGLY IMPORT OMIT
# FIXME: paths/imports should be fixed before submitting a PR to Ansible
sys.path.append('lib/ansible/modules/misc')

import nay
// END UGLY IMPORT OMIT


// START TESTMOCKS OMIT
class AnsibleExitJson(Exception):
    """Exception class to be raised by module.exit_json and caught
    by the test case"""
    pass


def exit_json(*args, **kwargs):
    if 'changed' not in kwargs:
        kwargs['changed'] = False
    raise AnsibleExitJson(kwargs)

def set_module_args(args):
    # Not really mocking, injecting arguments
    args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
    basic._ANSIBLE_ARGS = to_bytes(args)
// END TESTMOCKS OMIT

// START TESTCODE OMIT
class TestNayModule(object):
    @classmethod
    @pytest.fixture(autouse=True)
    def setup_class(cls, monkeypatch):
        monkeypatch.setattr(
            nay.AnsibleModule, "exit_json", exit_json)
        args = dict(question="Do you like Emacs?")
        set_module_args(args)

    def test_run(self):
        with pytest.raises(AnsibleExitJson) as result:
            nay.main()
        assert result.value[0]["answer"] == "humf...Nay!!!"
        # nay module doesn't really change a thing :)
        assert not result.value[0]["changed"]
// END TESTCODE OMIT
