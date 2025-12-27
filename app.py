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
    try:
        receiver = request.form['email']
        message = request.form['message']

        msg = Message(
            "Reminder",
            sender=os.environ.get("EMAIL_USER"),
            recipients=[receiver]
        )
        msg.body = message

        mail.send(msg)

        return "Email sent successfully ✅"

    except Exception as e:
        print("EMAIL ERROR:", e)
        return "Email failed ❌", 500

if __name__ == '__main__':
    app.run(debug=True)