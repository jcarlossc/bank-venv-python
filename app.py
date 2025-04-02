



from banco.conta.ContaCorrente import ContaCorrente
from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica


pf1 = PessoaFisica("carlos", "12345678989")
print(pf1.get_nome())
print(pf1.get_cpf())
print(pf1.get_tipo_usuario())
pj1 = PessoaJuridica("soares", "12345678989123")
print(pj1.get_nome())
print(pj1.get_cnpj())
print(pj1.get_tipo_usuario())

cc1 = ContaCorrente(pf1)
print(cc1.get_saldo())
cc1.depositar(100.00)
print(cc1.get_saldo())