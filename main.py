from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Advent of Music": "Welcome!! Please visit the challenge's page https://adventofmusic.rmercado.dev"}


@app.get("/items")
def read_item():
    return [
        {
            "day": 1,
            "class": "past",
            "title": "Snowflake melody",
            "body": "",
            "emoji": ":notes:",
            "tags": [
                "melody",
                "period form"
            ]
        },
        {
            "day": 2,
            "class": "active",
            "title": "Snowflake melody 2",
            "emoji": ":notes:",
            "tags": [
                "melody",
                "period form"
            ]
        },
        {
            "day": 3,
            "class": "upcoming"
        },
        {
            "day": 4,
            "class": "upcoming"
        },
        {
            "day": 5,
            "class": "upcoming"
        },
        {
            "day": 6,
            "class": "upcoming"
        },
        {
            "day": 7,
            "class": "upcoming"
        },
        {
            "day": 8,
            "class": "upcoming"
        },
        {
            "day": 9,
            "class": "upcoming"
        },
        {
            "day": 10,
            "class": "upcoming"
        },
        {
            "day": 11,
            "class": "upcoming"
        },
        {
            "day": 12,
            "class": "upcoming"
        },
        {
            "day": 13,
            "class": "upcoming"
        },
        {
            "day": 14,
            "class": "upcoming"
        },
        {
            "day": 15,
            "class": "upcoming"
        },
        {
            "day": 16,
            "class": "upcoming"
        },
        {
            "day": 17,
            "class": "upcoming"
        },
        {
            "day": 18,
            "class": "upcoming"
        },
        {
            "day": 19,
            "class": "upcoming"
        },
        {
            "day": 20,
            "class": "upcoming"
        },
        {
            "day": 21,
            "class": "upcoming"
        },
        {
            "day": 22,
            "class": "upcoming"
        },
        {
            "day": 23,
            "class": "upcoming"
        },
        {
            "day": 24,
            "class": "upcoming"
        },
        {
            "day": 25,
            "class": "upcoming"
        },
        {
            "day": 26,
            "class": "disabled"
        },
        {
            "day": 27,
            "class": "disabled"
        },
        {
            "day": 28,
            "class": "disabled"
        },
        {
            "day": 29,
            "class": "disabled"
        },
        {
            "day": 30,
            "class": "disabled"
        },
        {
            "day": 31,
            "class": "disabled"
        }
    ]
