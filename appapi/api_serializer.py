from ninja import ModelSchema
from appdb.models import Account

class AccountRegis(ModelSchema):
    """
    Schema for post api to store in db
    """
    class Config:
        model = Account
        model_fields = [
            'username',
            'password',
        ]


class AccountIn(ModelSchema):
    """
    Schema for post api to store in db
    """
    class Config:
        model = Account
        model_fields = [
            'firstname',
            'lastname',
            'email',
            'tel_number',
        ]


class AccountOut(ModelSchema):
    """
    Output of Account
    """
    class Config:
        model = Account
        model_fields = [
            'username',
            'firstname',
            'lastname',
            'email',
            'tel_number',
            # 'gender',
            # 'subscription'
        ]


class profile(ModelSchema):
    """
    for login
    """
    class Config:
        model = Account
        model_fields = ['username']