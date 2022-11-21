def salaries():
    for x in range(len(total_fname)):
        bonus = int(all_salary[x]) * 1/10
        print(f'Name: {total_lname[x]} {total_fname[x]} \n Age: {total_age[x]} \n Salary: {all_salary[x]} \n Bonus: {bonus}')

def bonuses():
    for x in range(len(total_fname)):
        bonus = int(all_salary[x]) * 1/10
        print(f'Name: {total_lname[x]} {total_fname[x]} \n Bonus: Yes')

total_fname = []
total_lname = []
total_age = []
all_salary = []
for x in range(2):
    fname = input('What is your first name?')
    lname = input('What is your last name?')
    age = input('How old are you?')
    salary = input('What is your salary')
    total_fname.append(fname)
    total_lname.append(lname)
    total_age.append(age)
    all_salary.append(salary)
type = input('Which report do you want: public or private?').lower()
if type == 'public':
     salaries()
elif type == 'private':
     bonuses()
else:
    print('Sorry, invalid type')


