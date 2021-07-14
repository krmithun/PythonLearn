import pytest
import socket

test_ip = "192.168.1.257"
def test_ip_valid():
    """Verify an IP address is valid."""
    try:
        socket.inet_pton(socket.AF_INET, test_ip)
        print ("Valid IP")
    except socket.error:
        print ("Invalid IP")
