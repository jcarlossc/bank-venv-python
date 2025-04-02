



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