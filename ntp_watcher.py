import time
import subprocess
import select
import re

import mail

filename = "/export/ntp_bot_survey/tcpdump_ntpport_log_eth1"

# format example
# 23:39:00.854602 IP 10.24.128.63.ntp > ntp-a3.nict.go.jp.ntp: NTPv4, Client, length 48
# This regular expression should match IPv4 and the number of length.
# In above example, this regex extract 10.24.128.63 and 48.
REGEX_PARSE_LINE="\S+ \S+ ((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)).\S+ \S+ \S+ \S+ \S+ \S+ ([0-9]+)"


def is_ntp_bot(line):
    m = re.search(REGEX_PARSE_LINE, line)
    if m:
        ip = m.group(1)
        size = int(m.group(2))
        if size > 48:
            if re.match("10.24.*", ip):
                return True


def main():
    f = subprocess.Popen(['tail','-F',filename],\
            stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)

    while True:
        if p.poll(1):
            line = f.stdout.readline()
            if is_ntp_bot(line):
                mail.send(line)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
