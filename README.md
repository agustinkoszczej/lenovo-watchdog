# lenovo-watchdog
This is an application for checking stock availability on a Lenovo laptop sale:). 

It connects to an affinity portal webpage, logs in using a promotional code and will check with a given frequency _(set as environment variable)_ and if there's stock available, it will send an email notification.

Some of the main technologies used: ```Python```, ```SendGrid``` _(for email notifications)_ and ```Selenium```_(for webpage automation)_.

## How to run

1. Set your environment variables _(you can choose wheter to edit a ```.env``` file for local tests or set up them as environment variables in your container)_.
2. Run the following command and get notified:
```bash
python3 lenovo_watchdog.py
```

# Notes
 
- There's a [Procfile](https://github.com/agustinkoszczej/lenovo-watchdog/blob/master/Procfile) for deploying it on Heroku cloud platform.
- Your environment variables should look like:
  ```
  URL = https://www.lenovo.com/ar/es/araff/gatekeeper/showpage?toggle=PasscodeGatekeeper
  COUPON_CODE = CSTARHR
  TO_ADDRESS = <email-address>
  FROM_ADDRESS = <sendgrid-validated-email-address>
  SENDGRID_API_KEY = <sendgrid-api-key>
  LOGGING_LEVEL = INFO
  REFRESH_INTERVAL = 120
  GOOGLE_CHROME_BIN = C:\Program Files\Google\Chrome\Application\chrome.exe
  ```
