import schedule
import time
import smtplib
from email.message import EmailMessage
from decouple import config


def job():
    import datetime

    # sendig mail with csv file
    msg = EmailMessage()
    msg["Subject"] = "Latest DateTime"
    msg["From"] = config("FROM_EMAIL")
    msg["To"] = config("TO_EMAIL")

    msg.set_content(f"Hi, Present time {datetime.datetime.now()} ")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(config("FROM_EMAIL"), config("PASSWORD"))
            server.send_message(msg)
            print("email sent......")
    except Exception as e:
        print(e)


schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at('13:58').do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)  # wait one minute
