import datetime

class Datetime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        
        if year is None or month is None or day is None:
            self.date_time = datetime.datetime.now()
        else:
            self.date_time = datetime.datetime(year, month, day, hour, minute, second)

    @staticmethod
    def date_from_string(date_string):
        
        return Datetime(*map(int, date_string.split('-')))

    @staticmethod
    def validate_date(day, month, year):
        
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def date_difference(date1, date2, unit='days'):
        
        delta = date2.date_time - date1.date_time
        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return date2.date_time.month - date1.date_time.month + 12 * (date2.date_time.year - date1.date_time.year)
        else:
            raise ValueError(f"Invalid unit: {unit}")

    def iso_format(self):
        
        return self.date_time.isoformat()

    def human_readable_format(self):
        
        return self.date_time.strftime("%A, %B %d, %Y %I:%M %p")
