# -*- coding: utf-8 -*-
#
# Copyright 2017 Riverbed Technology, Inc.
# All Rights Reserved. Confidential.

"""Script to email information regarding builds."""

# author - pthakkar

import argparse
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText


def main():
    """Run main execution."""
    import pdb;pdb.set_trace()
    parser = argparse.ArgumentParser()
    parser.add_argument("--recipient", type=str)

    args = parser.parse_args()
    # Open a plain text file which has the build info by jenkins
    fp = open('file.txt', 'r')

    # Create a text/plain message
    msg = MIMEText(fp.read())
    fp.close()

    me = "krmithun@gmail.com"
    # you = str(args.recipient).split(',')
    you = "krmithun@gmail.com"
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Orchestration-CAT certified latest stable builds'
    msg['From'] = me
    msg['To'] = ", ".join(you)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    # s = smtplib.SMTP('localhost')
    # s.sendmail(me, you, msg.as_string())
    # s.quit()


if __name__ == '__main__':
    main()
