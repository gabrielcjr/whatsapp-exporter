
from dataclasses import dataclass
import re



@dataclass(frozen=True)
class Message:

    date: str
    phone_number: str
    text: str

    def validate_date(self):
        if not re.match(r'\+\d{2} \d{2} \d{4}-\d{4}', self.date):
            raise ValueError("Date format is wrong")
        
    def validate_phone_number(self):
        if not re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', self.phone_number):
            raise ValueError("Phone number format is wrong")
