def taxes(num_hours):    #num_hours is the number of hours of work per week
    pay_pretax = num_hours * 15 #the rate is 15$/hour
    pay_aftertax = pay_pretax * 0.88 #the tax bracket is 12% so the pay post taxes is 88%
    return str(pay_aftertax)

num_hours = int(input("how many hours did you work this week:"))

print("Your Paycheck after taxes is:" + taxes(num_hours) +"$")