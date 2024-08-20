#!/usr/bin/env bash

redshift &
keepassxc &
discord &
# rclone mount oneunipd: /home/salem/UniPD/ --vfs-cache-mode full &
# rclone mount oneunipd: /home/salem/UniPD/ --vfs-cache-mode writes --vfs-cache-poll-interval 10m --vfs-cache-max-size 32G --vfs-cache-max-age 10h --vfs-write-back 1h --cache-chunk-total-size 32G & disown
rclone mount oneunipd: /home/salem/UniPD/ --vfs-cache-mode full --vfs-cache-poll-interval 1m --vfs-cache-max-size 128G --vfs-cache-max-age 10h --vfs-write-back 5m --cache-chunk-total-size 64G & disown
