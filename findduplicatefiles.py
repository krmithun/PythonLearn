'''
Test cases for finding duplicate files in a directory

Case1:
Check if the file size of 2 or more files are same,
compare checksum for those files with same size, if same mark it as duplicate.

Case2:
Verify all files including hidden files are considered.

Case3:
Verify the files within the sub folders too are considered.

Case4:
Verify two files having same file size but only content differing, such files
should not be considered as duplicate.

Case5:
Verify two files with different extension but same content, such files
should be marked as duplicates.
'''


import hashlib
import logging
import os
import sys
from collections import defaultdict
from time import strftime

logger = logging.getLogger()
timestamp = strftime("%Y%m%d_%H%M%S")
log_file = __file__.split('.')[0] + '_' + timestamp + '.log'
hdlr = logging.FileHandler(log_file)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


def get_folder_name_from_command_line():
    if len(sys.argv) < 2:
        print('Base folder name is not passed hence current folder will be '
              'considered as base folder')
        print('Usage: %s <base folder>'% sys.argv[0])
        folder = os.getcwd()
    else:
        folder = sys.argv[1]
    return folder


def find_duplicate_size(parent_dir):
    dups = {}
    for dirName, subdirs, fileList in os.walk(parent_dir):
        logging.info('Looking in dir %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Check to make sure the path is valid.
            if not os.path.exists(path):
                continue
            # Calculate sizes
            file_size = os.path.getsize(path)
            # Add or append the file path
            if file_size in dups:
                dups[file_size].append(path)
            else:
                dups[file_size] = [path]
    return dups


def checksum(fname, chunk_size=1024):
    """
    Function which takes a file name and returns md5-checksum of the file
    """
    hash = hashlib.md5()
    # hash = hashlib.sha256()
    with open(fname, "rb") as f:
        # Read the 1st block of the file
        chunk = f.read(chunk_size)
        # Keep reading the file until the end and update hash
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    # Return the hex checksum
    # print(hash.hexdigest())
    return hash.hexdigest()


def main():
    # read base folder path from command line
    base_folder = get_folder_name_from_command_line()
    logging.info('Looking for duplicate files in folder {}'.format(base_folder))

    # create a dictionary with file size as the key and file name as value
    dict_size = find_duplicate_size(base_folder)
    # Identify keys (file size) having more than one values (file names)
    dup_size_list = (val for val in dict_size.values() if len(val) > 1)
    logging.info('\n\nFiles with the same size...\n====================')

    dict_checksum = defaultdict(list)
    for file_list in dup_size_list:
        # logging.info('  > {}'.format(file_list))
        dup = ''
        for file_path in file_list:
            dup += file_path + ',\t'
            # find checksum for file having same size to find the actual duplicates
            dict_checksum[checksum(file_path)].append(file_path)
        logging.info('Same size files  > {} '.format(dup))

    # Identify keys (checksum) having more than one values (file names)
    duplicate_files = (val for val in dict_checksum.values() if len(val) > 1)

    logging.info('\n\nDuplicate files...\n====================')
    for file_name in duplicate_files:
        dup = ''
        for file in file_name:
            dup += file + ',\t'
        logging.info('Duplicate files  > {} '.format(dup))

    print('Script log file {}'.format(log_file))


if __name__ == '__main__':
    main()

'''
[Usage]
python findduplicatefiles.py <base directory>

ex: 
python findduplicatefiles.py C:\Files_Dump

If <base directory> is not specified then current working directory
will be considered 
'''
