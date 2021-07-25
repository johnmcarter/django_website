#!/bin/bash

# Author: John Carter
# Created: 2021/07/19 20:35:15
# Last modified: 2021/07/19 20:39:24
# Sync photos between local computer and remote server

GRN=$'\e[1;32m'
RED=$'\e[1;31m'
END=$'\e[0m'

if [[ $# -ne 1 ]]; then
    echo "[${RED}ERROR${END}] USAGE: $0 <remote directory>" 
    exit 1
fi

echo "[${GRN}INFO${END}] rsyncing photos to $1...."
rsync -azP static/img/ $1
echo "[${GRN}INFO${END}] rsync complete"