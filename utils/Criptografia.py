import bcrypt

class Criptografia:
    def criptografar_senha(senha):
        # Gera um salt aleatório
        salt = bcrypt.gensalt()
        # Criptografa a senha usando o salt
        senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_criptografada.decode('utf-8')