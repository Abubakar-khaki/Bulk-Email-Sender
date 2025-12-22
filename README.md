# 📧 Bulk Email Sender

Send one email to many people at once!

## What it does

- Sends the same email to multiple people
- Uses Gmail to send
- Simple to customize!

## How to install

Nothing to install! Uses built-in Python libraries.

## ⚠️ IMPORTANT: Get Gmail App Password

Gmail won't let you use your normal password. You need an "App Password":

1. Go to: https://myaccount.google.com/apppasswords
2. Sign in to your Google account
3. Click "Select app" → choose "Mail"
4. Click "Select device" → choose "Windows Computer"
5. Click "Generate"
6. Copy the 16-character password
7. Paste it in the code where it says `my_password = ""`

## How to use

1. Open `bulik email sender.py`
2. Change `my_email` to your Gmail
3. Paste your App Password in `my_password`
4. Add email addresses to the `send_to` list
5. Write your `subject` and `message`
6. Run it!

```
python "bulik email sender.py"
```

## Example

```python
my_email = "john@gmail.com"
my_password = "abcd efgh ijkl mnop"  # Your app password

send_to = [
    "friend1@gmail.com",
    "friend2@gmail.com"
]

subject = "Party invitation!"
message = "Hey! You're invited to my party!"
```

## Need help?

- Make sure 2-Step Verification is ON in your Google account
- Use App Password, NOT your normal Gmail password
- Check that email addresses are correct
