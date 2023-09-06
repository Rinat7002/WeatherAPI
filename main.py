from flask import Flask, request
from flask_restful import Api, Resource
import asyncio

import sqlite
import weather


app = Flask(__name__)
api = Api()


async def main(city):
    sqlite.sql_start()
    global Weather
    Weather = await weather.getweather(city)
    weather2 = {"City": city, "Weather": Weather}
    return weather2


class Main(Resource):
    def get(self):
        city = request.args.get('city')
        result = asyncio.run(main(city))

        sqlite.sql_start()
        sqlite.sql_add(city, Weather)
        return result


api.add_resource(Main, '/weather')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

# http://127.0.0.1:3000/weather?city=Ufa
