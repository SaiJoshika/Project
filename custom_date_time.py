import datetime

class CustomDateTime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            current_datetime = datetime.datetime.utcnow()
            self._datetime = current_datetime.replace(hour=hour, minute=minute, second=second)
        else:
            self._datetime = datetime.datetime(year, month, day, hour, minute, second)

    @classmethod
    def from_iso_format(cls, iso_string):
        try:
            dt = datetime.datetime.fromisoformat(iso_string)
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        except ValueError as e:
            raise ValueError(f"Invalid ISO format: {iso_string}") from e

    def to_iso_format(self):
        return self._datetime.isoformat()

    def to_human_readable_format(self):
        return self._datetime.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def year(self):
        return self._datetime.year

    @property
    def month(self):
        return self._datetime.month

    @property
    def day(self):
        return self._datetime.day

    @property
    def hour(self):
        return self._datetime.hour

    @property
    def minute(self):
        return self._datetime.minute

    @property
    def second(self):
        return self._datetime.second

    @staticmethod
    def validate_date(year, month, day):
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        if not isinstance(date1, cls) or not isinstance(date2, cls):
            raise ValueError("Both dates must be instances of CustomDateTime")

        delta = date1._datetime - date2._datetime

        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return (date1.year - date2.year) * 12 + date1.month - date2.month
        else:
            raise ValueError("Invalid unit. Use 'days', 'weeks', or 'months'.")

    @classmethod
    def date_from_string(cls, date_string):
        try:
            dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        except ValueError as e:
            raise ValueError(f"Invalid date string format: {date_string}") from e

    @classmethod
    def date_now(cls):
        current_datetime = datetime.datetime.utcnow()
        return cls(current_datetime.year, current_datetime.month, current_datetime.day,
                   current_datetime.hour, current_datetime.minute, current_datetime.second)

    @staticmethod
    def day_of_week(date):
        return date._datetime.strftime("%A")


date1 = CustomDateTime(2021, 4, 3, 11, 32, 56)
date2 = CustomDateTime.from_iso_format("2021-04-03T11:32:56")

# Printing in different formats
print("ISO Format:", date1.to_iso_format())
print("Human Readable Format:", date1.to_human_readable_format())

# Accessing individual parts of the datetime object
print("Year:", date1.year)
print("Month:", date1.month)
print("Day:", date1.day)
print("Hour:", date1.hour)
print("Minute:", date1.minute)
print("Second:", date1.second)

# Validating a date
print("Is given date '2021-04-04' a valid date?", CustomDateTime.validate_date(2022, 4, 3))
print("Is given date '2023-02-30' a valid date?", CustomDateTime.validate_date(2023, 2, 30))

# Date difference
date3 = CustomDateTime(2019, 5, 10)
print("Difference between date1 and date3 in days:", CustomDateTime.date_difference(date1, date3, unit='days'))
print("Difference between date1 and date3 in weeks:", CustomDateTime.date_difference(date1, date3, unit='weeks'))
print("Difference between date1 and date3 in months:", CustomDateTime.date_difference(date1, date3, unit='months'))

# Creating a date from a string
date4 = CustomDateTime.date_from_string("2023-10-07 12:45:36")
print("Created date through string:", date4.to_human_readable_format())