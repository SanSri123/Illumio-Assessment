'''
Illumio Take-Home Assessment by Sanjay Garimella

This script generates mock flow log data and mock lookup table mappings. Arbitrary values correspodngin
to the default Version 2 format are used for the flow log data.
'''

import socket
import random

version = "2"
account_number = "123456789012"
interface_id = "eni-4h5i6j7k"
src_addr = ["172.16.0.2", "192.168.1.6", "192.168.1.12", "203.0.113.12"]
dest_addr = ["198.51.100.4", "203.0.113.102", "201.0.114.12", "195.51.100.5"]
src_port = ""
dest_port = ""
protocol = []
num_packets = "45"
num_bytes = "29000"
start = "1620140761"
end = "1620140721"
action = "ACCEPT"
log_status = "OK"
protocol_name = []

for name,num in vars(socket).items():
            if name.startswith("IPPROTO"):
                protocol.append(str(num))
                protocol_name.append(name[8:])

#Writing flow log data to text file.
with open("mock_flow_log_data.txt", "w") as mock_data:
        for i in range(1,80000):
            mock_data.write(version + " " + account_number + " " + interface_id + " " + src_addr[random.randint(0,3)] + " " + dest_addr[random.randint(0,3)]
                            + " " + str(random.randint(20, 5000)) + " " + str(random.randint(20, 5000)) + " " + protocol[random.randint(0,31)]
                            + " " + num_packets + " " + num_bytes + " " + start + " " + end + " " + action + " " + log_status + "\n")

print("Completed Logs")

tags = "sv_p"

#Writing lookup table mapping to text file.
with open("mock_lookup_table.txt", "w") as mock_lookup:
    mock_lookup.write("dstport,protocol,tag\n\n")
    for i in range(1,10000):
          mock_lookup.write(str(random.randint(20, 5000)) + "," + protocol_name[random.randint(0,31)].lower() + "," + tags + str(random.randint(0,15)) + "\n")

print("Completed lookup")
