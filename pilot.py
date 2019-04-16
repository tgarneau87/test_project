from test_1 import Branch, Client


def print_releve(bank, client_id):
    print(bank.nom, bank.clients[client_id].nom, bank.clients[client_id].balance)


y = Branch('Ste-foy bank', 'quebec')
y.clients[12345] = Client(1, 'tristan', 1)

# Code de pilotage
running = True
while running is True:

    x = input(print('{} \n{}\n{}'.format('1-voir solde', '2-Dépot', '3-Retrait')))

    if x == '1':
        print_releve(y, 12345)

    elif x == '2':
        y.clients[12345].deposit(int(input('Montant du dépot: ')))
    elif x == '3':
        y.clients[12345].deposit(int(input('Montant du retrait: ')) * -1)
    else:
        running = False
