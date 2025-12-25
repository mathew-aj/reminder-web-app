from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_ADDRESS = "mm8032155@gmail.com"      # un gmail
EMAIL_PASSWORD = "jwuc cytd hjko qroj"      # app password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    user_email = request.form['email']
    message = request.form['message']

    msg = EmailMessage()
    msg['Subject'] = "New Reminder Notification"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS   # unakku varanum na same mail
    msg.set_content(
        f"Name: {name}\n"
        f"User Email: {user_email}\n"
        f"Message: {message}"
    )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return "Email notification sent successfully!"

if __name__ == '__main__':
    app.run(debug=True)