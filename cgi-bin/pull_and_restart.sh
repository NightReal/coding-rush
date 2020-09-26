#!/bin/bash
repo_path=/web/coding_rush/coding_rush

echo 'Refresh repo...'
cd $repo_path
sudo /usr/bin/git stash
sudo /usr/bin/git pull origin master

echo 'Restart service...'
sudo /bin/systemctl restart gunicorn.coding_rush.service

echo 'Print logs...'
sudo /bin/journalctl -u gunicorn.coding_rush.service --since "1 hour ago" | tail -n 10
