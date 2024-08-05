import shutil
import logging
import schedule
logging.basicConfig(filename="logs.txt", level="INFO",)
def check_disk():#How much space available in your system
    disk = shutil.disk_usage("/")
    per_used = (disk.total - disk.free)/disk.total*100
    print(per_used)
    if per_used > 75:
        logging.warning("disk full")
    elif per_used > 95:
        logging.critical("Crititcal disk full")
    else:
        print("Used space is less than 75%")

   
#check_disk()

schedule.every(10).seconds.do(check_disk) #cron setup

while True:
    schedule.run_pending()
"""
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents$ /home/gauravmtwt1/Documents/git-demo/.venv/bin/python "/home/gauravmtwt1/Documents/Python for DevOps/Class9_Final_Project/scheduler_proj/schedule_disk_utils.py"
23.07871316108286
Used space is less than 75%
23.07871316108286
Used space is less than 75%
23.07871316108286
Used space is less than 75%
23.07871420444253
Used space is less than 75%

"""