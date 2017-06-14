from smtplib import SMTP
import getpass
import datetime

debuglevel = 0
smtp = SMTP()
smtp.set_debuglevel(debuglevel)
smtp.connect('smtp.office365.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login('', getpass.getpass())
from_addr = ""
to_addr = ""

subj = "hello"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
message_text = "Hello\nThis is a mail from your server\n\nBye\n"
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" %( from_addr, to_addr, subj, date, message_text )

smtp.sendmail(from_addr, to_addr, msg)
smtp.quit()


#not yet done