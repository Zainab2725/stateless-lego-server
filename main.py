from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title='My Lego Server')

toys_data = [
    {'id':1, 'name':'Lego Castle', 'color': 'Gray'},
    {'id':2, 'name':'Race Car', 'color': 'Red'}
]

class Toy(BaseModel):
    id:int
    name:str
    color:str


@app.get('/toys')
def get_all_toys():
    return{'status':'success','toys':toys_data}

@app.post('/toys')
def create_new_toy(new_toy : Toy):
    toy_dict = new_toy.model_dump()
    toys_data.append(toy_dict)

    return{'message':'Toy added to the box!','current_box':toys_data}