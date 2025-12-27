from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

EMAIL_ADDRESS = os.environ.get("mm8032155@gmail.com")
EMAIL_PASSWORD = os.environ.get("jwuccytdhjkoqroj")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        print("USER:", EMAIL_ADDRESS)
        print("PASS SET:", EMAIL_PASSWORD is not None)

        receiver = request.form['email']
        message = request.form['message']

        msg = EmailMessage()
        msg['Subject'] = "Reminder"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = receiver
        msg.set_content(message)

        with smtplib.SMTP('smtp.gmail.com', 465, timeout=10) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return "Email sent successfully ✅"

    except Exception as e:
        print("EMAIL ERROR:", e)
        return "Email failed ❌"

if __name__ == '__main__':
    app.run()
