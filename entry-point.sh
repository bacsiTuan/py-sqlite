#!/bin/sh
#uvicorn manage:app --host 0.0.0.0 --port 8000 --reload
#uvicorn manage:app --host 0.0.0.0 --port 8000 --workers 4
#supervisord -n
#pyinstaller --name pythonsqlit --onefile manage.py
#pyinstaller --onefile manage.py
#set DB=pg
python manage.py