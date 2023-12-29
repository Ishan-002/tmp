from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import random

app = FastAPI()

# origins = [
#     "http://localhost:5175",
#     "localhost:5175",
#     "http://127.0.0.1:5175",
#     "127.0.0.1:5175",
# ]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# Sends one of the resopnses from the array at random
def get_response_after_business_logic():
    responses_option = [
        {
            "submit": False,
            "form": [
                {"field": "username", "input": "text"},
                {"field": "email", "input": "email"},
                {"field": "mobile", "input": "number"},
            ],
        },
        {
            "submit": True,
            "form": [],
        },
        {
            "submit": False,
            "form": [
                {"field": "dob", "input": "number"},
                {"field": "pan", "input": "text"},
            ],
        },
    ]
    return responses_option[random.choice([0, 1, 2])]


@app.post("/api/form")
async def onboarding_post(request: Request):
    data = await request.json()
    print(data)
    # some business logic to validate input and send back what inputs to render
    # format:
    # response = {
    #   // if submit is true, then the onboarding is finished
    #   submit: false,
    #   // all the form elements that need to be rendered
    #   form: [
    #     {
    #       field: 'username',
    #       input: 'text',
    #     },
    #     {
    #       field: 'mobile',
    #       input: 'number',
    #     },
    #     {
    #       field: 'email',
    #       input: 'email',
    #     },
    #     ...
    #   ],
    # };

    return get_response_after_business_logic()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=7000, reload=True)
