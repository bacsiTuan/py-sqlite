#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import gc
from loguru import logger

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.triggers.cron import CronTrigger

# Initialize a SQLAlchemyJobStore with SQLite database
job_stores = {"default": MemoryJobStore()}

# Initialize an AsyncIOScheduler with the job_stores
scheduler = AsyncIOScheduler(jobstores=job_stores)

trigger_per_min = CronTrigger(
    year="*", month="*", day="*", hour="*", minute="*", second="59"
)


@scheduler.scheduled_job(trigger_per_min)
async def update_env():
    try:
        logger.info(1)
    except Exception as e:
        logger.error(e)

