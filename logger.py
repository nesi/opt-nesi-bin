#!/usr/bin/env python
import logging
from logging.handlers import SysLogHandler
import sys
import socket
import os

if (len(sys.argv) >= 2):
    sh = logging.FileHandler(sys.argv[1])
else:
    sh = logging.StreamHandler()

l = logging.getLogger()
l.addHandler(sh)

#SysLogHandler.append_nul = False
SYSLOG_HOST = "192.168.95.139"
try: 
    h = SysLogHandler(address=(SYSLOG_HOST,514), 
        socktype = socket.SOCK_STREAM, 
        facility = logging.handlers.SysLogHandler.LOG_LOCAL1)
    user = os.environ["USER"]
    job_id = os.environ.get("SLURM_JOB_ID","-1")
    f = logging.Formatter('jupyter_client: %(message)s')
    h.setFormatter(f)
    h.setLevel(logging.DEBUG)
    l.addHandler(h)
except:
    l.error(f"Cannot reach syslog server on {SYSLOG_HOST}");


for line in sys.stdin:
    l.error(f"{user} {job_id} {line.rstrip()}")
    h.flush()
    sh.flush()
