
from .gmail_smtplib_micro import GmailSMTPLib
from ._examples import ExampleConfiguration, ExampleEmail
from ._email import Email

GmailSMTPLib
ExampleConfiguration
ExampleEmail
Email

VERSION = (0, 1, 0)

VERSION_STRING = '.'.join(map(str, VERSION))
