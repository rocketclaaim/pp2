#ex1
from datetime import datetime,timedelta
current_date=datetime.now()
new_date=current_date-timedelta(days=5)
print(current_date)
print(new_date)

#ex2
from datetime import datetime,timedelta
current_date=datetime.now()
yesterday_date=current_date-timedelta(days=1)
today_date=current_date
tomorrow_date=current_date+timedelta(days=1)
print(yesterday_date)
print(today_date)
print(tomorrow_date)

#ex3
from datetime import datetime,timedelta
current_date=datetime.now()
new_date=current_date.replace(microsecond=0)
print(new_date)

#ex4
from datetime import datetime
date_str1 = input()
date_str2 = input()
date1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')
difference_in_seconds = abs((date2 - date1).total_seconds())
print(difference_in_seconds)