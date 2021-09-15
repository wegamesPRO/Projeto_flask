import dataset


class Banco:
    def registrar(self, data):
        with dataset.connect('sqlite:///covid_2') as db:
            return db['usuarios'].insert(dict(
                nome=data['nome'],
                numero_cartao=data['numero_cartao'],
                cvv=data['cvv'],
                validade=data['validade'],
                cpf=data['cpf']
            ))

    def listar(self, id = None):
        with dataset.connect('sqlite:///covid_2') as db:
            if id == None:
                lista = db['usuarios'].all()
            else:
                lista = db['usuarios'][id]

            if db['usuarios'].count() > 0:
                usuarios = [dict(
                id=data['id'],
                nome=data['nome'],
                numero_cartao=data['numero_cartao'],
                cvv=data['cvv'],
                validade=data['validade'],
                cpf=data['cpf']
            )for data in lista]
                return usuarios
            else:
                return False

    def apagar(self, id):
        with dataset.connect('sqlite:///covid_2') as db:
            return db['usuarios'].delete(id=id)



