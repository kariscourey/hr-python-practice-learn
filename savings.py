# Implement the function calculate_monthly_savings which will return the total you will save each month if you save a percent of your salary.

# annual_salary	save_rate	output
# 60000	0.05	250
# 120000	0.10	100
# 150000	0.15	1875
# To calculate the total you will save, divide your annual salary into how much you would save per month (12 months in a year), then multiply that by the save_rate.

def calculate_monthly_savings(salary, save_rate):
    return salary/12 * save_rate


print(calculate_monthly_savings(60000,0.05))
