from pydantic import BaseModel


class OptionalAuthShema(BaseModel):
    nome_social: str = None

    cpf: str = None
    cnpj: str = None
    telefone: str = None

    cep: str = None
    logradouro: str = None
    uf: str = None
    bairro: str = None
    localidade: str = None
    complemento: str = None
    endereco: str = None


class AuthShema(OptionalAuthShema):
    nome: str
    senha: str
    email: str
