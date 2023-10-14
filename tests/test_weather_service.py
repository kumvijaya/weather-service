"""
Unit tests for weather service
"""
import json

from src.weather_service import get_default_location, get_api_url_response

def test_default_location():
    """Test default location"""
    expected = {'lattitude' : 52.52, 'langitude': 13.41}
    assert expected == get_default_location()

def test_api_url_response():
    """Test api url"""
    user_data = """ 
        {    "data": {
                "id": 2,
                "email": "janet.weaver@reqres.in",
                "first_name": "Janet",
                "last_name": "Weaver",
                "avatar": "https://reqres.in/img/faces/2-image.jpg"
            },
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
        }
    """
    expected = json.loads(user_data)
    assert expected == get_api_url_response('https://reqres.in/api/users/2')
