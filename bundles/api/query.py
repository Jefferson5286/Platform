from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from httpx import AsyncClient
from json.decoder import JSONDecodeError


router = APIRouter(prefix='/query')


@router.get('/cep/{cep}')
async def get_cep_data(cep: str) -> JSONResponse:
    async with AsyncClient() as client:
        request = await client.get(f'https://viacep.com.br/ws/{cep}/json/')

        if request.status_code == 400:
            raise HTTPException(400, 'CEP invalido.')

        try:
            data = request.json()
        except JSONDecodeError:
            raise HTTPException(400, 'Erro ao buscar o pelo CEP!')

    response = {
        'uf': data.get('uf', None) if data.get('uf', None) != '' else None,
        'bairro': data.get('bairro', None) if data.get('bairro', None) != '' else None,
        'localidade': data.get('localidade', None) if data.get('localidade', None) != '' else None,
        'complemento': data.get('complemento', None) if data.get('complemento', None) != '' else None,
        'logradouro': data.get('logradouro', None) if data.get('logradouro', None) != '' else None
    }

    return JSONResponse(status_code=200, content=response)
