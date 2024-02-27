# api/tasks.py

from celery import shared_task
import time

@shared_task
def process_number(number):
    for i in range(1, number + 1):
        print(i)
        time.sleep(1)  # 1초 동안 대기

    return f"Processed {number} numbers"
