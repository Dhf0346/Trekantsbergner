import datetime

todaysDateTime = datetime.datetime.now()

danishDage = {
    'Monday': 'Mandag',
    'Tuesday': 'Tirsdag',
    'Wednesday': 'Onsdag',
    'Thursday': 'Torsdag',
    'Friday': 'Fredag',
    'Saturday': 'Lørdag',
    'Sunday': 'Søndag'
}

print("The time when you startede the program:", todaysDateTime.time())
print(todaysDateTime.date())
print("I dag er det:", danishDage[todaysDateTime.strftime("%A")])