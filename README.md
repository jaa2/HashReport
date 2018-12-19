# HashReport
Python interface/script for generating reports of the hashes of files in a directory and any subdirectories.

# Usage
usage: hashreport [-h] [--absolute-paths] [--hashalgo HASHALGO]
                  [--start-at START_AT]
                  directory report_filename

Generate a report of file hashes for a specified directory.

positional arguments:
  directory             Directory whose files will be hashed
  report_filename       Filename of the report to be generated

optional arguments:
  -h, --help            show this help message and exit
  --absolute-paths, -a  Absolute paths will be used instead of relative paths
  --hashalgo HASHALGO, -ha HASHALGO
                        Hash algorithm to use. Examples: sha256, sha512, md5
  --start-at START_AT   Start at a given index in the file list of the
                        directory. Change this if you need to resume a report
                        that already started.
