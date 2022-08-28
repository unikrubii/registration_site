from urllib import response
from ninja import Router
from . import api_serializer, dbhandler


router = Router()

@router.get("/register")
def get_regis(request):
    return ({"text": "Hello Api"})


@router.post("/register/")
def account_db(request, payload: api_serializer.AccountRegis):
    """
        username: str,
        password: str,
    """
    cmd = dbhandler.dbCommands(request)
    r = cmd.register(payload)
    return {"status_code": r['status']}


@router.get("/auth")
def get_pwd(request, u_name:str, pwd:str):
    cmd = dbhandler.dbCommands(request)
    pwd_db = cmd.get_pwd(u_name)
    response = {
        'password': ''
    }
    if pwd == pwd_db['password']:
        response['password'] = pwd
    return response


@router.get("/profile/")
def get_profile(request, u_name:str):
    cmd = dbhandler.dbCommands(request)
    account = cmd.get_account(u_name)
    data = []
    data.append(account)
    return data

@router.patch("/profile/")
def edit_profile(request, payload: api_serializer.AccountOut):
    cmd = dbhandler.dbCommands(request)
    status = cmd.update_account(payload.username)
    return status

