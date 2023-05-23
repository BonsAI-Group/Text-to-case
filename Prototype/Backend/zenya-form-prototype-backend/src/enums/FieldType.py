from enum import Enum

class FieldType(Enum):
    TEXT = "text"
    MULTI_SELECT = "multi_select"
    RADIO_BUTTON = "radio_button"
    DATE = "date"
    TIME = "time"
    DATE_TIME = "date_time"