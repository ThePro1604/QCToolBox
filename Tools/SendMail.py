<<<<<<< HEAD
def SendMail(text, subject, recipient):
    import win32com.client as win32
    import os
=======
import win32com.client as win32
import os


def SendMail(text, subject, recipient):
>>>>>>> 84b359e (Initial commit)

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    ###

    ###
    mail.Display(True)


MailSubject = "QC ToolBox Request"
MailInput = """
<p>What would you like to be added: 
<br />
</p>
<p>link (if exists): 
<br />
</p>
<p>preferred icon (Optional):
<br />
</p>
"""
MailAddress="Shahaf.Stossel@au10tix.com"

SendMail(MailInput, MailSubject, MailAddress) #that open a new outlook mail even outlook closed.
