from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, cod, nome, matricula, semestre):
        Aluno.__init__(self, cod, nome, matricula)
        self.semestre = semestre
        
    def imprimir(self):
        Aluno.imprimir(self)
        print(f'''Semestre: {self.semestre}º Semestre da Graduação''')