import datetime
from typing import Optional

class IDateTimeConverter():
    """Interface for a converter that converts dates, times and datetimes."""
    def __init__(self) -> None:
        pass

    def convertDateTime(self, dateTime: str) -> Optional[datetime.datetime]:
        """Convert a date, time or datetime to a date and time."""
        raise NotImplementedError
    
    def convertDate(self, date: str) -> Optional[datetime.date]:
        """Convert a date to a date."""
        raise NotImplementedError
    
    def convertTime(self, time: str) -> Optional[datetime.time]:
        """Convert a time to a time."""
        raise NotImplementedError