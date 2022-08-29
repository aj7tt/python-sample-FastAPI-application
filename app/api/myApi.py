from fastapi import APIRouter


router = APIRouter()


# route for Items api service
from .endpoints.Items.items import items as itemAPIRouter
router.include_router(itemAPIRouter)


# # route for stores api service
from app.api.endpoints.Stores.stores import store as storeAPIRouter
router.include_router(storeAPIRouter)
