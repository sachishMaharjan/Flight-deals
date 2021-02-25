import os
from twilio.rest import Client
import smtplib


class NotificationManager:

    def send_sms(self, message):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=message,
            from_='+12028755996',
            to=os.environ.get('MY_NUMBER')
        )

        print(message.status)

    def send_emails(self, users_details, message, google_flight_link):
        for user in users_details:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=os.environ.get("MY_EMAIL"), password=os.environ.get("PASSWORD"))
                connection.sendmail(
                    from_addr=os.environ.get("MY_EMAIL"),
                    to_addrs=user['email'],
                    msg=f"Subject:New Low Price Flight!\n\nHi {user['firstName']},\n{message}\n{google_flight_link}".encode('utf-8')
                )

