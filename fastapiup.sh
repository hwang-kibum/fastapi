#!/bin/bash
echo " " 
echo " "
ifconfig | grep inet | head -n 1
echo " " 
echo " "
echo "insert 1 gunicorn"
echo "insert 2. uvicorn" 
read -p "INPUT >>" SELECT

if [ ${SELECT} -eq 1 ];
then
	gunicorn --bind 0:8000 api:app --worker-class uvicorn.workers.UvicornWorker
else
	uvicorn api:app --host 0.0.0.0 --port 8000 --reload
fi
