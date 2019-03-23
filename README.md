## NOAA Satellite Automated Decode using Raspberry PI and RTL-SDR

This is fully automated raspbian platform decoding system for wx satellite. This is headless raspbian, it doesn't need screen or monitor. Once you're done setting this up, you just leave it there connected to the internet to download TLE/keps daily. And it will do everything automatically without any supervision, from scheduling of satellites to get exact EPOC time and running WXToIMG and sox simultenously. Recorded apt wav audio is also available for each pass.

- Schedule and create cron job for each satellite that meets requirements (set minimum elevation, default is 20)
- Jobs will be created for the day at exactly 1 minute after midnight. (Check crontab -e)
- Timestamp and satellite name over every image. Imagemagick annotate tool.
- WXToIMG configured to create several images (HVC,HVCT,MCIR, etc).
- Python script that calculate sun elevation for each satellite pass to decide image enhancement done.
- .noaa.conf universal file path and configuration settings
- No auto-delete of raw files (wxmap and apt wav)
