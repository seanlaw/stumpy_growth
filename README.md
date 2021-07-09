# stumpy_growth

A small script for gathering STUMPY download information using Github Actions and cron-job.org

# Getting Started

Install dependencies for local testing

```
./setup.sh
```

# Create a Slack Webhook

1. Go to `api.slack.com`
2. Create an app
3. From scratch
4. Choose an App Name
5. Choose a Workspace
6. Create app
7. Incoming Webhooks
8. On
9. Add New Webhook to Workspace
10. Choose a channel/user
11. Allow
12. Copy the Webhook URL

# Store Wehbhook URL in Github Secrets

1. Navigate to this repo
2. Settings (for this repo)
3. Secrets
4. New repository secret
5. Set the name as "SLACK_WEBHOOK"
6. Paste the copied Webhook URL as the value

# Generate a Github Personal Access Token

1. Go to `https://github.com/settings/profile`
2. Developer Settings
3. Personal access tokens
4. Generate new token
4. Copy personal access token

# Setting Up Cron Job

1. Go to `console.cron-job.org`
2. Cronjobs
3. CREATE CRONJOB
4. COMMON Tab
5. Choose a title
6. Use `https://api.github.com/repos/seanlaw/stumpy_growth/dispatches` for the URL
7. Choose an execution schedule
8. ADVANCED Tab
9. Key=Accept
10. Value=application/vnd.github.v3+json
11. +ADD
12. Key=Authorization
13. Value=token {personal access token}
14. POST request method
15. {"event_type":"run_stumpy_growth"} request body. The event type must match the `types` found in the `.github/workflows/schedule.yml` file.
