from bson.objectid import ObjectId
from log.logger import get_logger
from config import Config
from datetime import datetime
import requests


logger=get_logger('cliente')

# Lista Clientes
def listar_clientes(id_=None,per_page=200,page=1,return_all_data=False,address=Config.API_ADDRESS,auth=Config.API_AUTH):

    address_ = address+"/customer/"

    header = {
        'Content-Type': 'application/json',
        'Authorization': auth
    }

    payload = {
        "id": id_,
        "per_page": per_page,
        'page':page
    }

    r = requests.get(address_,headers=header,params=payload)
   
    # pprint(r.json())
    json_obj = r.json()
    data = json_obj['status']['data']
    next_page = json_obj['status']['next_page']

    # Lista clientes de todas as páginas
    while next_page!= None:
        r = requests.get(next_page,headers=header)
        json_obj = r.json()
        data+=json_obj['status']['data']
        next_page = json_obj['status']['next_page']

    logger.debug(f'São {len(data)} clientes cadastrados no SD')
    print(f'São {len(data)} clientes/empresas cadastrados no SD')
    return data