class Aluno:
    def __init__(self, cod = None, nome = None, matricula = None):
        self.codigo = cod
        self.nome = nome
        self.matricula = matricula
    
    def imprimir(self):
        print(f'''
Código: {self.codigo}
Nome: {self.nome}
Matricula: {self.matricula}''')
        