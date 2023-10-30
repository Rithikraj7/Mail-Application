import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = entry_sender.get()
    password = entry_password.get()
    receiver_email = entry_receiver.get()
    subject = entry_subject.get()
    body = text_body.get(1.0, tk.END)

    if not (sender_email and password and receiver_email and subject and body):
        messagebox.showerror("Error", "All fields must be filled.")
        return

    try:
        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Attach body
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.your-email-provider.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("Email Application")
        
# Email sender entry
tk.Label(root, text="Your Email:").pack()
entry_sender = tk.Entry(root)
entry_sender.pack()

# Password entry
tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Email receiver entry
tk.Label(root, text="To Email:").pack()
entry_receiver = tk.Entry(root)
entry_receiver.pack()

# Email subje   ct entry
tk.Label(root, text="Subject:").pack()
entry_subject = tk.Entry(root)
entry_subject.pack()

# Email body text
tk.Label(root, text="Body:").pack()
text_body = tk.Text(root, wrap="word", height=10)
text_body.pack(expand=True, fill="both")

# Send button
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

# Run the application
root.mainloop()
