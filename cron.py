from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command="/usr/local/bin/python3 /Users/admin/Workspace/DomainTools/main.py")
job.minute.every(1)
cron.write()
print(job.is_enabled())
print(job.is_valid())