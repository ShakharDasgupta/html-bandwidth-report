"""A script which runs a server and gets the upload and dowload speeds."""
from subprocess import Popen, PIPE
import time

# Start the server
server_terminal = Popen("cd /home/chris/Documents/Code/html-bandwidth-report && python -m SimpleHTTPServer 8080", shell=True, stdin=PIPE, stdout=PIPE)

# Run the get speed command evey x minutes y times
x = 5
y = 120
i = 0
while i < y:
	Popen("cd /home/chris/Documents/Code/html-bandwidth-report && python speedtest_cli.py --csv bandwidth_report.csv", shell=True, stdin=PIPE, stdout=PIPE)
	print("Got time: " + str(x * (i + 1)))
	time.sleep(x * 60);
	i = i + 1
