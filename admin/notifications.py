from firebase_admin import messaging


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("sfs.json")
firebase_admin.initialize_app(cred)



from firebase_admin import messaging


def send_to_all_users(title, body):

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
        ),
        topic="sfs_all_users"
    )

    response = messaging.send(message)

    return response

def send_notification(fcm_token, title):

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
        ),
        token=fcm_token,
    )

    return messaging.send(message)