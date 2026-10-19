from fastapi import FastAPI

app = FastAPI(title="Riverstone Subscriptions")

PLANS = [
    {"id": "house", "name": "House Espresso", "every_weeks": [2, 4], "price": 15.0},
    {"id": "origin", "name": "Rotating Single Origin", "every_weeks": [2, 4], "price": 18.0},
    {"id": "seasonal", "name": "Seasonal (Holiday Blend in Dec)", "every_weeks": [4], "price": 19.0},
]
SUBSCRIPTIONS = {}


@app.get("/plans")
def plans():
    return PLANS


@app.post("/subscriptions")
def create(plan_id: str, email: str, every_weeks: int = 4):
    sub_id = len(SUBSCRIPTIONS) + 1
    SUBSCRIPTIONS[sub_id] = {"plan": plan_id, "email": email, "every_weeks": every_weeks, "skips": 0}
    return {"id": sub_id, **SUBSCRIPTIONS[sub_id]}


@app.post("/subscriptions/{sub_id}/skip")
def skip(sub_id: int):
    SUBSCRIPTIONS[sub_id]["skips"] += 1
    return SUBSCRIPTIONS[sub_id]
