import re
from datetime import datetime


def check_departure_date(departure_date_str):
    if not re.fullmatch(r'\d{4}(-\d{2}){2}', str(departure_date_str)):
        return False

    departure_date_date = datetime.strptime(departure_date_str, '%Y-%m-%d').date()

    return departure_date_date >= datetime.today().date()
