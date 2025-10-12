# find the total profit/loss of each trader working in a trading firm. Information regarding number of traders and number of transactions is unknown.

empID = input('Enter the employee ID:')
while empID != -1:
    trade = int(input('Enter the trade amount'))
    profit_loss = 0
    while trade != 0:
        profil_loss = profit_loss + trade 
        trade = int(input('Enter the trade amount: '))
    print(f'profit\loss for employee{empID} is {profil_loss}')
    empID = input('Enter the employee ID:')

