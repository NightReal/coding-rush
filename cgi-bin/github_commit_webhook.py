#!/web/vmsh_tasks_bot/vmsh_tasks_bot_env/bin/python
# -*- coding: utf-8 -*-

import cgi
import os
import pwd
import sys
import json
import hmac
from hashlib import sha1
from subprocess import Popen, PIPE

import cgitb
cgitb.enable()


# some ideas
# https://github.com/carlos-jenkins/python-github-webhooks/blob/master/webhooks.py
cur_dir_path = os.path.dirname(os.path.realpath(__file__))
GITHUB_SECRET = "secret"
EVENT_REPO_BRANCH_TO_SCRIPT = {
    ('push', 'vmsh_tasks_bot', 'master'): 'pull_and_restart.sh',
}


# Implement ping
event = os.environ.get('HTTP_X_GITHUB_EVENT', 'ping')
if event == 'ping':
    print('Content-Type: application/json\n\n')
    print(json.dumps({'msg': 'pong'}))
    exit()

# Getting payload
raw_payload = ''
payload = {}
try:
    raw_payload = sys.stdin.read()
    payload = json.loads(raw_payload)
except Exception as ex:
    print(ex)

# Checking signature
header_signature = os.environ.get('HTTP_X_HUB_SIGNATURE', '')
sha_name, signature, *_ = header_signature.split('=') + ['']
mac = hmac.new(GITHUB_SECRET.encode('utf-8'), msg=raw_payload.encode('utf-8'), digestmod='sha1')
hexdigest = str(mac.hexdigest())
if not hmac.compare_digest(mac.hexdigest(), signature):
    print('Content-Type: application/json\n\n')
    print(json.dumps({'msg': 'pong'}))
    exit()

# Checking action, repo and branch
branch = (payload.get('ref', '') + '///').split('/', 3)[2]
name = payload['repository']['name'] if 'repository' in payload else None
script = EVENT_REPO_BRANCH_TO_SCRIPT.get((event, name, branch), None)
if not script:
    print('Content-Type: application/json\n\n')
    print(json.dumps({'msg': 'pong'}))
    exit()
else:
    script_fullpath = os.path.join(cur_dir_path, script)
    proc = Popen(script_fullpath, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    user = pwd.getpwuid( os.getuid() )[ 0 ]
    ran = {
        'user': user,
        'returncode': proc.returncode,
        'stdout': stdout.decode('utf-8'),
        'stderr': stderr.decode('utf-8'),
    }
    print('Content-Type: application/json\n\n')
    print(json.dumps(ran))
