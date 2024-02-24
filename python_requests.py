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


def query_strings():
    response = requests.post(
        "https://learningrequests.free.beeceptor.com",
        headers={
            "X-API-KEY": "123456",
            "Testing": "Hello",
        },
        params={"sort": "asc", "page": "1"},
    )

    print(f"{response.status_code = }")


def request_headers():
    response = requests.post(
        "https://learningrequests.free.beeceptor.com",
        headers={
            "X-API-KEY": "123456",
            "Testing": "Hello",
        },
    )

    print(f"{response.status_code = }")


def json_data():
    """
    sending json data in the body of the request, sent as application/json
    Content-Type header not automatically populated by requests library
    """
    response = requests.post(
        "https://learningrequests.free.beeceptor.com",
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps({"data1": "this is data1"}),
    )

    print(f"{response.status_code = }")


def form_data():
    """
    Sending form data in body of the request, sent as application/x-www-form-urlencoded
    Content-Type header automatically populated by requests library
    """
    response = requests.post(
        "https://learningrequests.free.beeceptor.com",
        data={"data1": "this is data1"},
    )

    print(f"{response.status_code = }")


def raw_data():
    """
    Sending raw data
    """
    response = requests.post(
        "https://learningrequests.free.beeceptor.com", data=b"This is raw data"
    )

    print(f"{response.status_code = }")


def uploading_files():
    """
    sending files in the body of the request, sent as multipart/form-data
    Content-Type header automatically populated by requests library
    """
    response = requests.post(
        "https://learningrequests.free.beeceptor.com",
        files={"file": open("python_requests.py")},
    )

    print(f"{response.status_code = }")


def advanced():
    response = requests.post(
        "https://learningrequests.free.beeceptor.com",
        # auth=('username', 'password') # basic auth
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
# query_strings()
# json_data()
# form_data()
# raw_data()
# uploading_files()
# advanced()
# using_sessions()
