"""
Interface for generating reports of the hashes of files in a directory
and any subdirectories.
"""

import os
import hashlib

def get_file_list(directory):
    """
    Returns a list of all the files in "directory" and in any
    subdirectories of "directory".

    @param directory: Directory to walk.
    """
    file_list = []

    # Walk the directory and add any files to the list
    for dirpath, _dirnames, filenames in os.walk(directory):
        for current_file in filenames:
            file_list.append(str(os.path.join(dirpath, current_file)))
    return file_list

def save_hashes(file_list, out_filename, relative_dir=None, hash_algo="sha512", start_at=0):
    """
    Finds the hashes of files in file_list and outputs
    the hashes in a report to out_file.

    @param file_list: List of files for creating the hashes.
    @param out_filename: File used to output the hashes of these files.
    @param relative_dir: Directory to use in calculating a relative path,
        or None if the output paths should be absolute.
    @param hash_algo: Hashing algorithm to use.
    @param start_at: Index in the list to start at.
    """
    with open(out_filename, "w") as outfile:
        for file_id in range(start_at, len(file_list)):
            this_filename = file_list[file_id]
            this_hash = hashlib.new(hash_algo)

            # Find the display filename
            display_filename = this_filename
            if relative_dir is not None:
                display_filename = os.path.relpath(display_filename, relative_dir)

            try:
                with open(this_filename, "rb") as file:
                    chunk = file.read(4096)
                    while chunk:
                        this_hash.update(chunk)
                        chunk = file.read(4096)

                # Write the results to the output file
                file_line = (display_filename + "\t" + str(os.path.getsize(this_filename)) +
                             "\t" + this_hash.hexdigest() + "\n")
                outfile.write(file_line)
            except FileNotFoundError:
                outfile.write(display_filename + "\t" + "ERROR - File not found\n")

def save_hashes_rel(directory, out_filename, start_at=0):
    """
    Finds the hashes of the files in directory "dir" and saves them
    in file "out_filename" using relative paths from directory "dir."

    @param dir: Directory whose files will be included in the report.
    @param out_filename: Report filename.
    @start_at: First index in the file list to start at.
    """
    file_list = get_file_list(directory)
    save_hashes(file_list, out_filename, directory, "sha512", start_at)
