import os
import sys
import shutil
import time
import filecmp


'''
Synchronize 2 chosen catalogs, so the replica-catalog
copies the original catalog.
'''


def synchronize(original_path, replica_path, log_file):
    compare = filecmp.dircmp(original_path, replica_path)
    #Common subdirectories
    for direction in compare.common_dirs:
        #Recursive subdirectories synchronization
        synchronize(os.path.join(original_path, direction), os.path.join(replica_path, direction), log_file)
    #In both, different content
    for file in compare.diff_files:
        #File copy with replace
        shutil.copy2(os.path.join(original_path, file), os.path.join(replica_path))
        log = f'File {file} copied with replace from {original_path} to {replica_path}\n'
        log_file.write(log)
        print(log)
    #In original, not in replica
    for file in compare.left_only:
        #File copy
        try:
            shutil.copy2(os.path.join(original_path, file), os.path.join(replica_path))
            log = f'File {file} copied from {original_path} to {replica_path}\n'
            log_file.write(log)
            print(log)
        #Directory recursive copy
        except PermissionError:
            shutil.copytree(os.path.join(original_path, file), os.path.join(replica_path, file))
            log = f'Directory {file} copied from {original_path} to {replica_path}\n'
            log_file.write(log)
            print(log)
    #In replica, not in original
    for file in compare.right_only:
        #File delete
        try:
            os.remove(os.path.join(replica_path, file))
            log = f'File {file} removed from {replica_path}\n'
            log_file.write(log)
            print(log)
        #Direvtory recursive delete
        except PermissionError:
            shutil.rmtree(os.path.join(replica_path, file))
            log = f'Directory {file} removed from {replica_path}\n'
            log_file.write(log)
            print(log)


def main(*args):
    try:
        #Unpacking command line arguments
        original_path, replica_path, sync_interval, log_path = list(args)[1:]
        log_file = open(log_path, 'a')
        while 1:
            synchronize(original_path, replica_path, log_file)
            log_file.write('\n\n\n')
            time.sleep(float(sync_interval))
    except:
        exit('Wrong command line arguments')


if __name__ == '__main__':
    main(*sys.argv)
