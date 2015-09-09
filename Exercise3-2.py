#Exercise 3.2

#Pay employee 1.5 times the hourly rate for hours worked above 40

#Enter hours: 45
#Enter Rate: 10
#Pay: 475.0

try:
  hours_worked = int(raw_input('Enter hours worked: '))
  pay_rate = float(raw_input('Enter pay rate: '))
except:
  print 'Please enter a number in decimal notation i.e. 10 not ten'
  quit()

if hours_worked <= 40:
 total_pay = hours_worked * pay_rate
else:
 overtime_hours = hours_worked - 40
 overtime_payrate = pay_rate * 1.5
 overtime_pay = overtime_hours * overtime_payrate
 total_pay = 40 * pay_rate + overtime_pay

print 'Pay: ' + str(total_pay)
