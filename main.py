from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Union
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Adjust this to restrict methods if needed
    allow_headers=["*"],  # Adjust this to restrict headers if needed
)

# User details (hardcoded for this example)
USER_ID = "aditya_narayan_mahapatra_09072003"
EMAIL = "adityanarayan.mahapatra2021@vitstudent.ac.in"
ROLL_NUMBER = "21BRS1114"

# Define the request model
class DataRequest(BaseModel):
    data: List[Union[str, int]] = Field(..., description="List containing strings or integers")

# Define the response model
class DataResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_lowercase_alphabet: List[str]

@app.get("/bfhl")
async def bfhl_get():
    try:
        # Hardcoded response for the GET request
        response = {"operation_code": 1}
        
        # Return the response with a 200 status code
        return JSONResponse(content=response, status_code=200)
    
    except Exception as e:
        
        # Return a 500 Internal Server Error with an appropriate message
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/bfhl", response_model=DataResponse)
async def bfhl_post(request: DataRequest):
    try:
        data = request.data
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = []

        # Separate numbers and alphabets
        for item in data:
            if isinstance(item, str):
                if item.isdigit():
                    numbers.append(item)
                else:
                    alphabets.append(item)
            elif isinstance(item, int):
                numbers.append(str(item))

        # Determine the highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        if lowercase_alphabets:
            highest_lowercase_alphabet.append(max(lowercase_alphabets))
        
        
        # Prepare the response
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet,
        }

        return JSONResponse(content=response, status_code=200)

    except Exception as e:
        # Return a 500 Internal Server Error with an appropriate message
        raise HTTPException(status_code=500, detail="Internal Server Error")