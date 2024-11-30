import psycopg
from os import environ
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

config = {
    'conninfo': environ['DATABASE_URL'],
}


@app.get("/")
def read_root():
    return {"Advent of Music": "Welcome!! Please visit the challenge's page https://adventofmusic.rmercado.dev"}


@app.get("/items")
def get_items():
    try:
        with psycopg.connect(conninfo=config['conninfo']) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT content FROM gifts WHERE display_date <= CURRENT_DATE ORDER BY display_date ASC;")
                x = cur.fetchall()
        for i in range(len(x)):
            x[i] = x[i][0]
        [x.append({"day": d + 1, "class": "upcoming"}) for d in range(len(x), 25)]
        [x.append({"day": d + 1, "class": "disabled"}) for d in range(25, 31)]
        return x
    except (Exception, psycopg.DatabaseError) as error:
        raise error
