# stumpy_growth

A small script for gathering STUMPY download information

# Getting Started

Install dependencies


```
./setup.sh
```

# Setting Up Cron Job

1. Update the `PYTHON` variable `run.sh` script so that it points to your local python executable
2. Add `0 9 * * * /path/to/stumpy_growth.git/run.sh` to your cron jobs

# Slack Webhook

To find the Webhook URL, visit `api.slack.com`, select your app, and click on "Install App" under "Settings" along the left-hand-side menu. In the new screen, you should see the "Webhook URL" near the bottom of your screen.
