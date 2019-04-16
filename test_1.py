class Branch:
    def __init__(self, Nom, ville):
        self.nom = Nom
        self.ville = ville
        self.clients= {}


class Client:

    def __init__(self,id, nom, comptes_bancaires):
        self.nom=nom
        self.cpt = comptes_bancaires
        self.id=id
        self.balance = 0

    def return_balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount



