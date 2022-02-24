from apscheduler.schedulers.background import BackgroundScheduler
from main import app 
scheduler = BackgroundScheduler(timezone= 'Asia/kolkata')
scheduler.start() 
job = scheduler.add_job(app.get("/api/todo"),'cron',hour="17",minute="0")
print(job)