from typing import Optional
from ml.IDateTimeConverter import IDateTimeConverter

import datetime
import sutime
import re

class DateTimeConverter(IDateTimeConverter):
    """Interface for a converter that converts dates, times and datetimes."""
    def __init__(self) -> None:
        self.parser = sutime.SUTime()

    def convertDateTime(self, dateTime: str) -> Optional[datetime.datetime]:
        """Convert a date, time or datetime to a date and time."""
        date = self._parseDateTime(dateTime)
        if date is None:
            return None
        # expected formats:
        # yyyy-mm-ddThh:mm
        if re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$', date):
            parsed_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
            return parsed_date
        else:
            print("Warning: unknown date format detected: " + date)
            return None
    
    def convertDate(self, date: str) -> Optional[datetime.date]:
        """Convert a date to a date."""
        dateParsed = self._parseDateTime(date)
        if dateParsed is None:
            return None
        # expected formats:
        # yyyy-mm-dd
        if re.match(r'^\d{4}-\d{2}-\d{2}$', dateParsed):
            parsed_date = datetime.datetime.strptime(dateParsed, '%Y-%m-%d')
            return parsed_date.date()
        # yyyy-mm
        if re.match(r'^\d{4}-\d{2}$', dateParsed):
            parsed_date = datetime.datetime.strptime(dateParsed, '%Y-%m')
            return parsed_date.date()
        # yyyy-Www
        if re.match(r'^\d{4}-W\d{2}$', dateParsed):
            todayNumber = datetime.datetime.today().weekday()
            parsed_date = datetime.datetime.strptime(dateParsed + '-' + str(todayNumber), '%Y-W%W-%w')
            return parsed_date.date()
        # yyyy
        if re.match(r'^\d{4}$', dateParsed):
            parsed_date = datetime.datetime.strptime(dateParsed, '%Y')
            return parsed_date.date()
        else:
            print("Warning: unknown date format detected: " + dateParsed)
            return None
    
    def convertTime(self, time: str) -> Optional[datetime.time]:
        """Convert a time to a time."""
        date = self._parseDateTime(time)
        if date is None:
            return None
        # expected formats:
        # hh:mm:ss
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date): 
            parsed_date = datetime.datetime.strptime(date, '%Y-%m-%d')
            return parsed_date.time()
        # hh:mm
        if re.match(r'^\d{2}-\d{2}$', date):
            parsed_date = datetime.datetime.strptime(date, '%H:%M')
            return parsed_date.time()
        # hh
        if re.match(r'^\d{2}$', date):
            parsed_date = datetime.datetime.strptime(date, '%H')
            return parsed_date.time()
        # PTxxHxxM
        if re.match(r'^PT\d{2}H\d{2}M$', date):
            current_time = datetime.datetime.now()
            parsed_date = current_time + datetime.timedelta(hours=int(date[2:4]), minutes=int(date[5:7]))
            return parsed_date.time()
        # PTxxH
        if re.match(r'^PT\d{2}H$', date):
            current_time = datetime.datetime.now()
            parsed_date = current_time + datetime.timedelta(hours=int(date[2:4]))
            return parsed_date.time()
        # Try parsing as a datetime
        parsed_date = self.convertDateTime(date)
        if parsed_date is not None:
            return parsed_date.time()
        else:  
            print("Warning: unknown time format detected: " + date)
            return None  
        
    def _parseDateTime(self, dateTime: str) -> Optional[str]:
        """Parse a date, time or datetime using the parser"""
        parser_out = self.parser.parse(dateTime)

        if len(parser_out) == 0:
            return None
        if len(parser_out) > 1:
            print("Warning: multiple date/time values detected, using first one")
        return parser_out[0]['value']
