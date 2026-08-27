seatwork_02_employee_name = input('Enter employee name: ')

if seatwork_02_employee_name == '':
    print('Employee name cannot be empty')
    exit()

seatwork_02_employee_initials = input('Enter employee initials: ')

if seatwork_02_employee_initials == '':
    print('Employee initials cannot be empty')
    exit()

try:
    seatwork_02_employee_work_hours = float(input('Enter hours worked: '))
except ValueError:
    print('Hours worked must be a numeric value')
    exit()

