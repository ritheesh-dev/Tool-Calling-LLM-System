import datetime
import requests 

def get_current_date():
    """Retuen today's date"""
    return datetime.date.today().isoformat()


def calculate(expression:str):
    """Safely evaluates a math expression like '12 * 4 + 3'."""
    try:
        return str(eval(expression,{"__builtins__": {}}))

    except Exception as e:
        return f"Error:{e}"


def get_weather(city: str):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        return response.text
    except Exception as e:
        return f"Weather fetch failed: {e}"


