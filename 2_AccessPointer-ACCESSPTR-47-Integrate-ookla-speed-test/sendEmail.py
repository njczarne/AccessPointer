import win32com.client

def send_outlook_email(recipient, subject, body, attachment_path=None):
    try:
        outlook = win32com.client.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)

        mail.To = recipient
        mail.Subject = subject
        mail.Body = body

        mail.Send()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")


