# Bulk Email Sender
# Send one email to many people at once!

import smtplib
from email.mime.text import MIMEText

# === YOUR EMAIL SETTINGS ===
# Change these to your info!

my_email = "your-email@gmail.com"
my_password = ""  # Use Gmail App Password (see README)

# List of people to send email to
send_to = [
    "friend1@gmail.com",
    "friend2@gmail.com",
    "friend3@gmail.com"
]

# === YOUR MESSAGE ===

subject = "Hello from Python!"
message = """
Hi there!

This email was sent using Python.
Pretty cool, right?

Best,
Your Name
"""

# === SEND THE EMAIL ===

print("📧 Bulk Email Sender")
print("=" * 30)
print(f"📤 Sending to {len(send_to)} people...")

try:
    # Create the email
    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = my_email
    email["To"] = ", ".join(send_to)
    
    # Connect to Gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure connection
    server.login(my_email, my_password)
    
    # Send to everyone
    server.sendmail(my_email, send_to, email.as_string())
    server.quit()
    
    print("✅ Email sent to everyone!")
    
except Exception as error:
    print(f"❌ Oops! Something went wrong: {error}")
