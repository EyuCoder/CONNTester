import os
with open("IP.txt") as textFile:
        lines = [line.split() for line in textFile]
for ip in lines:
        res = os.popen(f"ping {ip[0]}").read()
        if "Received = 4" in res:
                print(f"UP {ip[1]} Ping Successful")
        else:
                print(f"DOWN {ip[1]} Ping Unsuccessful")
