from fastapi import FastAPI

app = FastAPI()

characters_details = [
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
        "role": "fisherman",
        "area": "Vada Chennai - Dockside"
    },
]

@app.get("/")
async def characters():
    return characters_details
