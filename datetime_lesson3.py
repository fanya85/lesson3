from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# today
dt_now = datetime.now()
print(datetime.date(dt_now))

# yesterday
yesterday = dt_now - timedelta(days=1)
print(yesterday.strftime('%Y-%m-%d'))

# one month later
month_later = dt_now - relativedelta(months = 1)
print(month_later.strftime('%Y-%m-%d'))