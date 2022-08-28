from appdb.models import Account
from django.shortcuts import get_object_or_404
from . import api_serializer


class dbCommands:

    def __init__(self, request):
        self.request = request

    def __str__(self):
        return f"{self.request.method}"

    def register(self, acc_regis: api_serializer.AccountRegis):
        try:
            acc = get_object_or_404(Account, username=acc_regis.username)
            return {"status": "found"}
        except:
            acc = Account(
                username = acc_regis.username,
                password = acc_regis.password,
            )
            acc.save()
            return {"status": "create"}

    def get_pwd(self, u_name:str):
        try:
            acc = get_object_or_404(Account, username=u_name)
            return {'password': acc.password}
        except:
            return None

    def get_account(self, u_name:str):
        try:
            acc = get_object_or_404(Account, username=u_name)
            account = {
                "username": acc.username,
                "email": acc.email,
                "firstname": acc.firstname,
                "lastname": acc.lastname,
                "tel_number": acc.tel_number,
            }
            return account
        except:
            return None

    def update_account(self, payload: api_serializer.AccountIn):
        try:
            acc = get_object_or_404(Account, username=payload.username)
            acc.firstname = payload.firstname
            acc.lastname = payload.lastname
            acc.email = payload.email
            acc.tel_number = payload.tel_number
            acc.save()
        except:
            return None
        return {"status": 202}
