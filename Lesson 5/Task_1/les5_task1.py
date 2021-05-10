from collections import deque

quantity = int(input("Введите кол-во компаний: "))
sum=0
company = deque([],maxlen=4)
name = deque([],maxlen=quantity)
profit = deque([],maxlen=quantity)
for i in range(quantity):
    name.append(input(f'Введите название {i+1} компании: '))
    for j in range(4):
        company.append(int(input(f'Введите прибыль за {j+1} квартал: ')))
    profit_for_company = 0
    for k in company:
        sum += k
        profit_for_company+=k
    profit.append(profit_for_company)
print(f'Средняя прибыль компаний за год: {sum/quantity}')
print("Прибыльные компании: ")
for j in range(len(profit)):
    if profit[j]>(sum/quantity):
        print(name[j])
print("Убыточные компании: ")
for j in range(len(profit)):
    if profit[j]<(sum/quantity):
        print(name[j])
