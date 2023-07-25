class Paciente:
    def __init__(self, codigo_p, codigo_adm, nome, cpf, telefone, profissao, estado, cidade, bairro, rua, numero):
        self.codigo_adm = codigo_adm
        self.codigo_p = codigo_p
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.profissao = profissao
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

