import time
from instagram_private_api import Client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = 'my username which im not gonna share lol'
password = 'certainly not my password too'
client_id = 'your crush id here dont worry they wont know'
client_secret = 'Im good with naming conventions so read the variable names you lazy'
access_token = 'your api token here dont spam'

sender_email = 'a dummy account that we will use to send email or notifications'
sender_password = 'password of that dummy account'
receiver_email = 'email that you want to receive notifications'
smtp_server = 'smtp server if you are using gmail then it is smtp.gmail.com'
smtp_port = 587     # 587 is the default port for gmail

api = Client(username, password, client_id=client_id, client_secret=client_secret, access_token=access_token)


previous_photo = api.current_user()['user']['profile_pic_url']
previous_followers = api.current_user()['user']['follower_count']
previous_following = api.current_user()['user']['following_count']

while True:
    # Get current values
    current_photo = api.current_user()['user']['profile_pic_url']
    current_followers = api.current_user()['user']['follower_count']
    current_following = api.current_user()['user']['following_count']

    # Compare values with previous values
    if current_photo != previous_photo:
        subject = 'Profile Photo Changed'
        message = 'Your Instagram profile photo has been changed.'
        send_email(subject, message)

    if current_followers != previous_followers:
        subject = 'Followers Changed'
        message = f'Your number of followers has changed: {current_followers}'
        send_email(subject, message)

    if current_following != previous_following:
        subject = 'Following Changed'
        message = f'Your number of following has changed: {current_following}'
        send_email(subject, message)

    # Update previous values
    previous_photo = current_photo
    previous_followers = current_followers
    previous_following = current_following

    # time you want to check in seconds
    time.sleep(300)

def send_email(subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # This will start our email server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
