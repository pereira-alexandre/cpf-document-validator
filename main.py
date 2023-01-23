from cpf_validator import CPFValidator

cpf_value = input('Digite seu CPF: ')
cpfvalidator = CPFValidator(cpf_value)

if cpfvalidator.isCPF():
    print('CPF Válido!')
else:
    print('CPF Inválido')