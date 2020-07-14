# Adir-Miler-Notifier
sends a mail when a new show of Adir Miler has came out
## Getting started
1. run "get_old_row_count.py"
2. change the config.py file to your details.
```python
config = {
	"sender": "me@example.com",
	"recipients": ["john.doe@example.com, john.smith@example.co.uk"],
	"password": "123",
	"body": "bla",
	"subject": "subject line"
	}
```
 3. set "check_show.py" to run every now and then in Task Scheduler.
