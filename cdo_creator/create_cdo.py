from eloqua_session import EloquaSession

session = EloquaSession()

request_body = {
    "name": "Emmanual CDO",
    "description": "bottom text",
    "fields":
    [
        {}
    ]
}

response = session.post(url='/api/REST/2.0/assets/customObject', data=request_body)
