# Author: John Carter
# Created: 2021/07/04 17:57:02
# Last modified: 2021/08/10 21:16:50

GRN=$'\e[1;32m'
END=$'\e[0m'

echo "[${GRN}INFO${END}] Pulling new code from git"
cd django_website
git pull

echo "[${GRN}INFO${END}] Copying data..."
cd ..
cp -r django_website/ /home/john/

echo "[${GRN}INFO${END}] Restarting service..."
systemctl restart website.service
systemctl status website.service

echo "[${GRN}COMPLETE${END}] Website restarted"