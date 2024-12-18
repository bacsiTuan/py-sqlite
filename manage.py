#!/usr/bin/env python
# coding: utf8
import os
import uvicorn
from dotenv import load_dotenv
from fast_api_app import create_app, scheduler
from app.schedule.update_env import update_env

load_dotenv(override=False)

application = app = create_app()


# Register an event for application startup
@application.on_event("startup")
async def startup_event():
    scheduler.start()
    await update_env()


@application.on_event("shutdown")
async def shutdown_event():
    scheduler.shutdown()

if __name__ == '__main__':
    print(os.getenv("DB"))
    uvicorn.run("fast_api_app:app", host="0.0.0.0", port=8000, reload=False, workers=1, log_level="warning")
