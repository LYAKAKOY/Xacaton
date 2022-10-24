from datetime import datetime, timedelta
from calendar import monthrange



def get_days_in_month():
    current_year = datetime.now().year
    month = datetime.now().month
    return monthrange(current_year, month)

def get_day_of_month():
    given_date = datetime.today().date()
 
    first_day_of_month = given_date - timedelta(days = int(given_date.strftime("%d"))-1)
    return first_day_of_month
