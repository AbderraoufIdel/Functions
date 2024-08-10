def taxes(num_hours, hourly_wage, tax_bracket):
    pay_pretax = num_hours * hourly_wage 
    pay_aftertax = pay_pretax * (1 - tax_bracket/100)
    return str(pay_aftertax)
print("Paycheck after taxes!!")
num_hours = int(input("how many hours did you work this week:"))
hourly_wage = int(input("what is your hourly wage:"))
tax_bracket = int(input("what is your tax bracket:"))

print("Your paycheck after taxes is:" + taxes(num_hours, hourly_wage, tax_bracket) + "$")