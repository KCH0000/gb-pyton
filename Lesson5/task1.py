class Factory:
    def __init__(self, name, cash_flow):
        summ = 0
        self.name = name
        self.cash_flow = cash_flow
        for cash in cash_flow:
            summ += cash
        self.cash = summ
        self.cash_avg = summ / len(cash_flow)


factory_list = []
i = 1
cash_sum = 0
cash_avg = 0

while True:
    factory_name = input(f'Ведите название {i}-го предприятия(0-exit): ')
    if '0' == factory_name:
        break
    cash = [int(x) for x in input('Введите прибыль по кварталам через пробел: ').split(' ')]
    factory_list.append(Factory(factory_name, cash))
    i += 1

factory_list.sort(key=lambda factory: factory.cash_avg)

for factory in factory_list:
    cash_sum += factory.cash_avg
cash_avg = cash_sum / len(factory_list)

print('')
print(f'Средняя прибыль: {cash_avg}')
i = 0
print('')
print('*' * 10 + 'Outsiders' + '*' * 10)
while i < len(factory_list):
    print(f'{factory_list[i].name} средняя прибыль {factory_list[i].cash_avg}')
    i += 1
    if factory_list[i - 1].cash_avg < cash_avg <= factory_list[i].cash_avg:
        print('')
        print('*' * 10 + 'TOP' + '*' * 10)

