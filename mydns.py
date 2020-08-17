import sys
import socket

# from: https://gist.github.com/DamnedFacts/5058978

"""
test multithreaded dns resolver
@filename mydns.py
"""

ip="1.1.1.1"

#
def getHost(ip):
    """
    This method returns the 'True Host' name for a
    given IP address
    """
    try:
        data = socket.gethostbyaddr(ip)
        host = repr(data[0])
        return host
    except Exception:
        # fail gracefully
        return False
#

hostname = getHost(ip)
print (hostname)