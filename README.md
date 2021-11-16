# lenovo-watchdpg
This is an application for checking stock availability on a Lenovo laptop :). It connects to an affinity portal webpage, logs in using a promotional code. If there's stock, it will send an email notification.
Some of the main technologies used: ```Python```, ```SendGrid``` _(for email notifications)_ and ```Selenium```_(for webpage automation)_.

## How to run

1. Set up your [environment variables](https://github.com/agustinkoszczej/lenovo-watchdog/blob/master/.env) _(you can choose wheter to edit the .env file for local tests or set up them as env variables in your container)_
2. Just run the following command and get notified:
```bash
python3 lenovo_watchdog.py
```

# Notes
 
- There's a [Procfile](https://github.com/agustinkoszczej/lenovo-watchdog/blob/master/Procfile) for deploying it on Heroku cloud platform.