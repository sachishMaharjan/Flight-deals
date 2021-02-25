import os
from twilio.rest import Client


class NotificationManager:

    def send_notification(self, flight ):
        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Low Price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                 f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date} ",
            from_='+12028755996',
            to='+61405852198'
        )

        print(message.status)
