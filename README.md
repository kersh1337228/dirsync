# directories_synchronizer
Python script which synchronizes the replica-directoty with the original-one.


Automatically detects all changes when script is on and synchronize directories,
logging all steps of synchronization into the log file and outputting the same steps to the terminal.

To start using the next script you have to know the following features:

1) Data format should be next:
py/python app.py <original_path> <replica_path> <sync_interval> <log_path>

2) original_path, replica_path and log_path can be either absolute paths
or relative ones (<Local_disk>:\folder\...\ or folder\...\);
3) sync_interval must be able to convert to float;

4) To exit the program use standard: Ctrl + Break or Ctrl + C;
