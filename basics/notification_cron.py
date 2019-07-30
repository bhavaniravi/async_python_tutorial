import os


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


notify("Take a break", "You are sitting for too long")


# > crontab -e
# In the editor paste the following
# > */20 * * * * python /Users/bhavani/apps/schedulers/basics/notification_cron.py
