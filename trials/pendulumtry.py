import pendulum

now_in_paris = pendulum.now('Europe/Paris')
print(now_in_paris)

now_in_paris.in_timezone('UTC')
print(now_in_paris)

tom = pendulum.now().add(days=1)
print(tom)
last_week = pendulum.now().subtract(weeks=1)
print(last_week)

past = pendulum.now().subtract(minutes=2)
print(past)
past.diff_for_humans()
print(past)