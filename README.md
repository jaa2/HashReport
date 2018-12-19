# HashReport
HashReport is a Python3 interface/script for generating reports of the hashes of files in a directory and any subdirectories. It can be used for comparing directories on separate drives.

By default, it creates a text file containing the following components separated by tabs:
* Filename relative to the directory path
* Size of the file
* SHA-512 hash of the file

# Usage
hashreport [-h] [--absolute-paths] [--hashalgo HASHALGO] [--start-at START_AT] directory report_filename

For detailed usage information, run ```"python hashreport --help"```.
