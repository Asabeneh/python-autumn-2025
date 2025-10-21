'''

open('sample.txt', 'w')

'''

""" open('sample.txt', 'w')
for i in range(1, 6):
    f = open(f'sample-{i}.txt', 'w')
    f.write(f'This is the sample_{i}.txt file') """
    
log_data = [
    {
        "name": "User_Alice",
        "timestamp": "2025-10-21T10:01:15Z",
        "operation_type": "LOGIN_SUCCESS"
    },
    {
        "name": "System_Monitor",
        "timestamp": "2025-10-21T10:01:22Z",
        "operation_type": "CHECK_HEALTH"
    },
    {
        "name": "User_Bob",
        "timestamp": "2025-10-21T10:02:05Z",
        "operation_type": "FILE_READ"
    },
    {
        "name": "DB_Service",
        "timestamp": "2025-10-21T10:02:40Z",
        "operation_type": "QUERY_FAILURE"
    },
    {
        "name": "User_Charlie",
        "timestamp": "2025-10-21T10:03:11Z",
        "operation_type": "LOGIN_FAILURE"
    },
    {
        "name": "Network_Agent",
        "timestamp": "2025-10-21T10:03:55Z",
        "operation_type": "PING_SUCCESS"
    },
    {
        "name": "User_Alice",
        "timestamp": "2025-10-21T10:04:30Z",
        "operation_type": "FILE_WRITE"
    },
    {
        "name": "Backup_Script",
        "timestamp": "2025-10-21T10:05:01Z",
        "operation_type": "START_BACKUP"
    },
    {
        "name": "User_Bob",
        "timestamp": "2025-10-21T10:05:45Z",
        "operation_type": "LOGOUT_SUCCESS"
    },
    {
        "name": "System_Monitor",
        "timestamp": "2025-10-21T10:06:18Z",
        "operation_type": "REPORT_WARNING"
    }
]
    
with open('log.csv','a') as f:
    f.write(f'name,timestamp,operation\n')
    for log in log_data:
        name = log['name']
        timestamp = log['timestamp']
        operation = log['operation_type']
        f.write(f'{name},{timestamp},{operation}\n')
    