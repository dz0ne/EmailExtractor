
import re, pyperclip
import sys, time
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("copy text and u will find emails in emailDump.txt")

EmailDump = re.compile(r'[A-Z1-z0-9_.]+@[A-Z1-z0-9_.]+') 
copiedText = pyperclip.paste()
EmailExtract = EmailDump.findall(copiedText)
Emails= '\n'.join(EmailExtract)
EmailFile = open('emailsDump.txt', 'w')
EmailFile.write(Emails)
EmailFile.close()

