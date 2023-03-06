from celery import shared_task
from celery.utils.log import get_task_logger
from foodapp.celery import app
logger = get_task_logger(__name__)
from time import sleep

@app.task()
def send_email_reservation_async(mail_details):
    logger.info('Sending email for the reservation on: "{}" '.format(mail_details))
    #sleep(0.3)