#!/usr/bin/env python3

"""
Module to fetch weather information from wttr.in
This FastAPI application provides an endpoint to retrieve weather data for a specified location.
It uses the wttr.in service to fetch the weather information and returns it in a structured format
"""
from fastapi import FastAPI
import uvicorn
import httpx

app = FastAPI()


@app.get("/")
async def read_root():
    """Welcome message for the Weather API.
    """
    return {"message": "Welcome to the Weather API!"}


@app.get("/weather/{location}")
async def get_weather(location: str):
    """ Fetch weather information for a given location. 
    """
    url = f"https://wttr.in/{location}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return {"location": location, "weather": response.text}
        return {
            "error": "Could not retrieve weather data",
            "status_code": response.status_code,
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
