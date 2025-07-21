from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Character(BaseModel) :
    name : str
    role : str
    area : str


characters_details : Character = [
    {
        "name": "Anbu",
        "role": "rebel",
        "area": "Vada Chennai - North Colony",
    },
    {
        "name": "Rajan",
        "role": "leader",
        "area": "Vada Chennai - Old Town",
    },
    {
        "name": "Guna",
        "role": "gangster",
        "area": "Vada Chennai - Phase II",
    },
    {
        "name": "Senthil",
        "role": "politican",
        "area": "Vada Chennai - Phase I",
    },
    {
        "name": "Velu",
        "role": "henchman",
        "area": "Vada Chennai - South Market",
    },
    {
        "name": "Palani",
        "role": "gym-rat",
        "area": "Vada Chennai - Dockside"
    },
]

@app.get("/characters")
async def characters():
    return characters_details

@app.post("/characters")
async def characters(characters : Character):
    characters_details.append(characters)
    print("Character Updated Details" , characters_details)
    return {"message" : f"The character {characters.name} is succesfully added in the universe 😉"}

@app.get("/character/${characterName}")
async def get_character(characterName: str):
    for character in characters_details:
        if character["name"] == characterName:
            return {"data": character}
    return {"message": f"The character {characterName} is not found in the universe 🤷‍♂️"}