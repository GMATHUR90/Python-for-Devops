#Using Regular expression

#1. Extracting the IP address
#Regular expression are used for matching patterns
#\d+: matches one or more digit
#'\.': matches a literal dot
#\d+\.\d+\.\d+\.\d+ : matches an IP address
#?P<IP>: named group. part inside paranthesis(?P<IP>...) will be accsesible
#by the name IP.

import re

line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'
ip_pattern = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
match = re.search(ip_pattern, line) #re.search for pattern
if match:
    print(match.group('IP'))
"""
#O/P: 127.0.0.1
"""


#2. Extracting the time
#'\[': matches opening square bracket
#\d\d: matches exactly two digit(representing date)
#\w{3}: matches 3 word character(represent month such as Nov)
#\d{4}: matches 4 digit(representing year)
#\d{2}:\d{2}:\d{2}: hours: minutes: seconds
#'\]': closing square bracket
#(?P<Time>): is a named group, the part inside the parenthesis
# will be accessible by the name 'Time'

import re
line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'
time_pattern =  r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
match =  re.search(time_pattern,line)
if match:
    print(match.group('Time'))
"""
#O/P:13/Nov/2019:14:43:30
"""

#3. Extracting Multiple elments(IP, User, Time, and Request):

import re
line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'
full_pattern = (
    r'(?P<IP>\d+\.\d+\.\d+\.\d+)' #IP address 
    r' - (?P<User>\w+)'      #User 
    r' \[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]' #Time 
    r' (?P<Request>".+")'
)
match =re.search(full_pattern,  line)
if match:
    print(match.group('IP'))
    print(match.group('Time'))
    print(match.group('User'))
    print(match.group('Request')) 

"""
O/P: 127.0.0.1
13/Nov/2019:14:43:30
rj
"GET HTTP/1.0"
"""

#4. Extracting all IP addresses for GET requests on a specific date

import re
log_data = """
127.0.0.1 - swills [08/Nov/2019:14:43:30 -0800] "GET /assets/234 HTTP/1.0" 200 2326
192.168.1.1 - john [08/Nov/2019:15:12:34 -0800] "GET /index.html HTTP/1.1" 200 3421
10.0.0.1 - jane [08/Nov/2019:16:22:10 -0800] "POST /login HTTP/1.1" 200 532
342.3.2.33 - doe [08/Nov/2019:17:45:50 -0800] "GET /home HTTP/1.0" 404 231
"""

get_request_pattern = (
        r'(?P<IP>\d+\.\d+\.\d+\.\d+)' #IP address
        r' - (?P<User>\w+)'
        #r' \[(?P<Time>08/Nov/2019:\d{2}:\d{2}:\d{2} [-+]\d{4})\] '
        r' \[(?P<Time>08/Nov/2019:\d{2}:\d{2}:\d{2} [-+]\d{4})\] '
        r'"(?P<Request>GET .+?)"'
)
matches = re.finditer(get_request_pattern,log_data)
for match in matches:
    print(match.group('IP'))
    print(match.group("User"))  
    print(match.group('Time'))
    
    print(match.group('Request'))


"""
#O/P:
127.0.0.1
swills
08/Nov/2019:14:43:30 -0800
GET /assets/234 HTTP/1.0
192.168.1.1
john
08/Nov/2019:15:12:34 -0800
GET /index.html HTTP/1.1
342.3.2.33
doe
08/Nov/2019:17:45:50 -0800
GET /home HTTP/1.0
"""


#Dealing with Large File

#Processing Large Text Files line by line
source_file=r'/home/gauravmtwt1/Downloads/log.txt'
with open(source_file,'r') as source_doc:
    with open('source_file_corrected.txt', 'w') as target_file:
        for line in source_doc  :
            target_file.write(line)

#Process large binary file in chunk(Useful for image/video)
#ab: append in binary

#Define a sample process data function that writes chunk to a new file
def process_data(chunk):
    with open('processed_image.png','ab') as target_file:
        target_file.write(chunk)

#Reading the image file in chunks and processing each chunk
with open('Processs_image_using_python.png','rb') as source_file:
    while True:
        chunk = source_file.read(1024)
        if chunk:
            process_data(chunk)
        else:
            break
