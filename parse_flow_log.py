'''
Illumio Take-Home Assessment by Sanjay Garimella

This program reads aws vpc flow log data from a text file and uses a lookup table to count
the number of lines that could be tagged. The lookup table is also provided in the format
of a text file to be read in.

To run the program:
python3 parse_flow_log.py <lookup_table txt file> <flow log data file>

'''

import sys
import socket

class ParseFlowLog:
    def __init__ (self, lookup_table, flow_log):
        self.lookup_table_file = lookup_table
        self.flow_log_file = flow_log
        self.lookup_table = {}
        self.tags_count = {}
        self.port_protocol_count = {}
        self.ip_protocol_table = {}

        print("Building Lookup Table \n\n")
        self.build_lookup_table()
        self.build_protocol_table()
        print("Parsing Flow Log Data\n\n")
        self.parse_flow_log_data()
        print("Writing Output\n\n")
        self.print_output()

    '''
    This function opens the lookup table text file, parses each line, and builds the lookup
    table to be used during log parsing. The Lookup Table is a dictionary where they key is
    a tuple of (dstport,protocol) and the value is the tag associated with it.
    '''
    def build_lookup_table(self):
        with open(self.lookup_table_file, "r") as lookup_file:
            next(lookup_file)
            next(lookup_file)
            for line in lookup_file:
                data = line.split(',')
                data[2] = data[2].strip()

                self.lookup_table[(data[0],data[1])] = data[2].lower() #data[0] = dst port, data[1] = protocol, data[2] = tag

    '''
    This function generates an ip protocol table to be used for interpreting the protocol numbers
    provided in the flow log data. It uses the inbuilt python socket library to build the table.
    '''   
    def build_protocol_table(self):
        for name,num in vars(socket).items():
            if name.startswith("IPPROTO"):
                self.ip_protocol_table[str(num)] = name[8:]


    '''
    This function opens the flow log data file, reads each line, and parses the dstport and protocol
    fields found in each line. It then updates the dictionaries used for counting number of tags and 
    the number of (dstport,protocol) combinations found across the log file.
    '''
    def parse_flow_log_data(self):
        with open(self.flow_log_file, "r") as flow_log_data:
            for line in flow_log_data:
                data = line.split(' ')
                dstport = data[6]
                protocol = self.ip_protocol_table[data[7]].lower()
                tag = "untagged"

                if (dstport, protocol) not in self.port_protocol_count:
                    self.port_protocol_count[(dstport, protocol)] = 1
                else:
                    self.port_protocol_count[(dstport, protocol)] += 1
                
                if (dstport, protocol) in self.lookup_table:
                    tag = self.lookup_table[(dstport, protocol)]
                
                if tag not in self.tags_count:
                    self.tags_count[tag] = 1
                else:
                    self.tags_count[tag] += 1
    
    '''
    This function writes the output in the expected format to a text file call parsed_output.txt
    '''
    def print_output(self):
        with open("parsed_output.txt", "w") as output:
            output.write("Tag Counts \n\nTag,Count\n\n")

            for tag, count in self.tags_count.items():
                output.write(tag + "," + str(count) + "\n")
            
            output.write("\n\nPort/Protocol Combination Counts\n\nPort,Protocol,Count\n\n")
            for port_protocol, count in self.port_protocol_count.items():
                output.write(port_protocol[0] + "," + port_protocol[1] + "," + str(count) + "\n")
        print("Output Written")

if not sys.argv[1] and not sys.argv[2]:
    print("Invalid input")
else:
    pfl = ParseFlowLog(sys.argv[1], sys.argv[2])








                
                
