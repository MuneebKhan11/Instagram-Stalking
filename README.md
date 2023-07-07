# Instagram Profile Monitor

The Instagram Profile Monitor is a Python script that monitors changes in your Instagram profile photo, number of followers, and following. It sends email notifications whenever any changes are detected. This script utilizes the Instagram Private API and the smtplib library in Python.

## Prerequisites

Before running the script, ensure you have the following requirements:

- Python 3.x installed on your machine.
- The `instagram-private-api` and `smtplib` libraries installed. You can install them using `pip`:

  ```bash
  pip install instagram-private-api smtplib

  
**Usage**
Clone the repository or download the script directly.

Open the script in a text editor and replace the following placeholders with your actual information:

* your_username: Your Instagram username.
* your_password: Your Instagram password.
* your_client_id: Your Instagram client ID.
* your_client_secret: Your Instagram client secret.
* your_access_token: Your Instagram access token.
* your_sender_email@example.com: The email address used as the sender.
* your_sender_password: The password for the sender email address.
* your_receiver_email@example.com: The email address where you want to receive notifications.
* your_smtp_server: The SMTP server address for sending emails.
* 587: The SMTP server port number.
Save the script with the changes.

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script using the following command:
```bash
python instagram_profile_monitor.py
