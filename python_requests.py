import json
import requests


def basics():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"{response.status_code = }")
    print(f"{response.text = }")

    """
    serliazied json content is converted to a dictionary
    note that not all responses are serialized json so response.json() will give an error in that case.
    """
    print(f"{response.json() = }")
    """ using response.json() is same as """
    print(f"{json.loads(response.text) = }")
    print(f"{response.headers = }")


def advanced():
    response = requests.post(
        "https://learningrequests.free.beeceptor.com",
        headers={
            "X-API-KEY": "123456",
            "Testing": "Hello",
        },
        params={"sort": "asc", "page": "1"},
        # auth=('username', 'password') # basic auth
        data={"data1": "this is data1", "data2": "this is data2"},  # sending json data
        files={"file": open("python_requests.py")},
        timeout=2,
        verify=True,  # ssl verification
    )

    print(f"{response.status_code = }")


def using_sessions():
    """
    Sessions persist parameters across requests
    """
    session = requests.Session()
    session.params = {"a": 1, "b": 2}
    response = session.get("https://learningrequests.free.beeceptor.com")
    print(f"{response.status_code = }")


# basics()
advanced()
# using_sessions()
