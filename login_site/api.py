from ninja import NinjaAPI
from appapi.api import router as api_router


api = NinjaAPI()

api.add_router("/", api_router)
