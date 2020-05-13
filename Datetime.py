import datetime
import pytz

dt_zag = datetime.datetime.now(tz=pytz.timezone('Europe/Zagreb'))

#print(dt_zag.strftime('%B %d, %Y'))

dt_str = 'March 01, 2020'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)






