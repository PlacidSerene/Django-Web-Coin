from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import history_api

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(history_api.update_history, 'interval', minutes=1)
    scheduler.start()