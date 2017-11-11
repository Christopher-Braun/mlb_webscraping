#!c:\users\mrcrb\documents\python\baseball\ll_env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'newrelic==2.96.0.80','console_scripts','newrelic-admin'
__requires__ = 'newrelic==2.96.0.80'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('newrelic==2.96.0.80', 'console_scripts', 'newrelic-admin')()
    )
