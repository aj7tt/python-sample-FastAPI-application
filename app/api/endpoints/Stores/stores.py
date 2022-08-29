
from fastapi import Depends, APIRouter, HTTPException
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.database.dbConfig import get_db
from app.database.crud import  StoreRepo

import app.pydanticModel.schemas as schemas

store = APIRouter()

@store.post('/stores', tags=["Store"], response_model=schemas.Store, status_code=201)
async def create_store(store_request: schemas.StoreCreate, db: Session = Depends(get_db)):
    """
    Create a Store and save it in the database
    """
    db_store = StoreRepo.fetch_by_name(db, name=store_request.name)
    print(db_store)
    if db_store:
        raise HTTPException(status_code=400, detail="Store already exists!")

    return await StoreRepo.create(db=db, store=store_request)


@store.get('/stores', tags=["Store"], response_model=List[schemas.Store])
def get_all_stores(name: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Get all the Stores stored in database
    """
    if name:
        stores = []
        db_store = StoreRepo.fetch_by_name(db, name)
        print(db_store)
        stores.append(db_store)
        return stores
    else:
        return StoreRepo.fetch_all(db)


@store.get('/stores/{store_id}', tags=["Store"], response_model=schemas.Store)
def get_store(store_id: int, db: Session = Depends(get_db)):
    """
    Get the Store with the given ID provided by User stored in database
    """
    db_store = StoreRepo.fetch_by_id(db, store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found with the given ID")
    return db_store


@store.delete('/stores/{store_id}', tags=["Store"])
async def delete_store(store_id: int, db: Session = Depends(get_db)):
    """
    Delete the Item with the given ID provided by User stored in database
    """
    db_store = StoreRepo.fetch_by_id(db, store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found with the given ID")
    await StoreRepo.delete(db, store_id)
    return "Store deleted successfully!"


