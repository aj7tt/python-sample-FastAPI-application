## create virtualenv

```
pip install virtualenv

virtualenv --version

python -m venv env  
            
env\Scripts\activate 

 ```

```
git init
```

## create .gitignore file

```
__pycache__
.env
env
```

## create a folder "app and a file inside it  requirements.txt

- uvicorn
- fastapi

run 
```
pip install -r requirements.txt
```

pip install --upgrade pip


```
inside app name crete a folder confiig and create a file config.py

We will store our project settings and configurations inside of this file named config.py.

```


#runnn
uvicorn app.main:app --reload 


## models and schemas

```
To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file 
models.py with the  SQLAlchemy models , and the file schemas.movieDataSchema.py with the Pydantic models.
```