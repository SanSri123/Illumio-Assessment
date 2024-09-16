# Illumio-Assessment by Sanjay Garimella

This repository contains the files needed to run my solution to the Illumio Assessment.

## How to Run Code
python3 parse_flow_log.py "lookup table mappings text file" "flow log data text file"

e.g. `python3 parse_flow_log.py mock_lookup_table.txt mock_flow_log_data.txt`

Must provide both files as arguments for code to run.

Assumptions Made:
- Program only support default log format (only version supported is 2)
- Lookup table mappings input file is comma separated
- Assumption is flow log data has all fields from Version 2
  - Will work even if field has default '-' character, but all fields must be present
- Both input files contain data and are formatted correctly

Testing:
- Program was tested with up to 10MB flow log file and up to 10000 lookup mappings
- Program will accept "-" characters in data in case data was not recorded during aggregation
