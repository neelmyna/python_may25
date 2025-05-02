name = input('Enter employee name: ')
id = int(input('Enter employee Id: '))
basic_monthly_salary = float(input('Enter employee basic monthly salary: '))
monthly_allownaces = float(input('Enter employee monthly allowances: '))
bonus_percentage = float(input('Enter employee bonus percentage: '))

gross_monthly_salary = basic_monthly_salary + monthly_allownaces
annual_salary_without_bonus = (gross_monthly_salary * 12)
annual_gross_salary = annual_salary_without_bonus + (bonus_percentage * annual_salary_without_bonus / 100)

print('%-11s %-6s %-20s %-17s %-6s %-12s %s'%('NAME', 'ID', 'BASIC_MONTHLY_SALARY', 'MONTHLY_ALLOWANCE', 'BONUS', 'GROSS_SALARY', 'ANNUAL_SALARY'))
print('-' * 90)

print('%-11s %-6d %-20.2f %-17.2f %-6.2f%% %-12.2f %-7.2f'%(name, id, basic_monthly_salary, monthly_allownaces, bonus_percentage, gross_monthly_salary, annual_gross_salary))

# bonus = str(('%-4.2f')%(bonus_percentage)) + '%'
# print('%-11s %-6d %-20.2f %-17.2f %-6s %-12.2f %-7.2f'%(name, id, basic_monthly_salary, monthly_allownaces, bonus, gross_monthly_salary, annual_gross_salary))

print('-' * 90)

# print(name, id, basic_monthly_salary, monthly_allownaces, bonus_percentage,'%', gross_monthly_salary, annual_gross_salary)

# print('NAME        ID  BASIC_MONTHLY_SALARY MONTHLY_ALLOWANCE BONUS GROSS_SALARY ANNUAL_SALARY')