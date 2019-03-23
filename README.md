## NOAA Satellite Automated Decode using Raspberry PI and RTL-SDR

- Schedule and create cron job for each satellite that meets requirements (set minimum elevation, default is 20)
- Jobs will be created for the day at exactly 1 minute after midnight. (Check crontab -e)
- Timestamp and satellite name over every image. Imagemagick annotate tool.
- WXToIMG configured to create several images (HVC,HVCT,MCIR, etc).
- Python script that calculate sun elevation for each satellite pass to decide image enhancement done.
- .noaa.conf universal file path and configuration settings
