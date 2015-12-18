#!/bin/sh
NOW=$(date +%Y-%m-%d)
HOST=
USER=
PASS=
FOLDER=~/Dropbox/backups/minecraft-backups/$NOW-backup
echo "[*] Creating a directory..."
mkdir $FOLDER
echo "[*] The target directory for the backup is : $FOLDER"
echo "[*] Copying all files and directories..."
echo "[*] ----From : $HOST with username $USER"
echo "[*] ----To : $FOLDER"
wget -P $FOLDER -r ftp://$USER:$PASS@$HOST
echo "[*] DONE !"
echo "[*] Compressing..."
7za a $FOLDER.7z $FOLDER
echo "[*] Archive saved under $FOLDER.tar.gz"
echo "[*] Cleaning up..."
rm -rv $FOLDER
echo "[*] ...Done...Quitting"

