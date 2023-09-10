'''Crie uma classe chamada ValidadorSenha que contenha um método estático chamado validar_senha. 
Este método estático deve receber uma senha como argumento e verificar se ela atende aos seguintes 
critérios de validação:

A senha deve ter pelo menos 8 caracteres.
A senha deve conter pelo menos uma letra maiúscula.
A senha deve conter pelo menos uma letra minúscula.
A senha deve conter pelo menos um dígito.
A senha deve conter pelo menos um caractere especial (por exemplo, @, #, $, %, etc.).
O método validar_senha deve retornar True se a senha atender a todos os critérios de validação e 
False caso contrário.

Você pode começar definindo a classe ValidadorSenha e implementando o método estático validar_senha 
dentro dela. O método validar_senha deve aceitar uma senha como argumento e realizar as verificações 
necessárias para determinar se a senha é válida ou não.'''


class ValidadorSenha:
    @staticmethod
    def validar_senha(senha):
        senha = str(senha)

        if len(senha) >= 8:
            cont_maiuscula = 0
            cont_minuscula = 0
            cont_digito = 0
            cont_especial = 0

            for c in senha:
                if c.isupper():
                    cont_maiuscula += 1
                if c.islower():
                    cont_minuscula += 1
                if c.isnumeric():
                    cont_digito += 1
                if c in "!@#$%^&*()_+[]{}|;:,.<>?/~":
                    cont_especial += 1

        if cont_maiuscula and cont_minuscula and cont_digito and cont_especial > 0:
            return True
        else:
            return False
            
        
print(ValidadorSenha.validar_senha('Diego.200529@gmail.com'))
