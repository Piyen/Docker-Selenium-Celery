# -*- coding: utf-8 -*-
from celery import Celery
CELERY_TIMEZONE = 'Asia/Shanghai'

app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
)

@app.task
def hello():
    print('Hello')


if __name__ == '__main__':
    app.worker_main()
