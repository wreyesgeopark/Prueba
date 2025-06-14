from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai
from openai import OpenAI
from typing import Optional
import traceback

print(f"OpenAI version: {openai.__version__}")
print("Environment variables available:", [k for k in os.environ.keys()])

class ChatRequest(BaseModel):
    message: str

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "ok",
        "env_vars_available": [k for k in os.environ.keys()]
    }

@app.post("/api/test-gpt")
async def test_gpt(request: ChatRequest, x_api_key: Optional[str] = Header(None)):
    try:
        # Verificar la API key
        expected_api_key = os.getenv("X_API_KEY")
        print(f"Received X-API-KEY header: {x_api_key}")
        print(f"Expected X-API-KEY from env: {expected_api_key}")
        
        if not expected_api_key:
            raise HTTPException(status_code=500, detail="X_API_KEY not configured on server")
            
        if not x_api_key:
            raise HTTPException(status_code=401, detail="X-API-KEY header is missing")
            
        if x_api_key != expected_api_key:
            raise HTTPException(status_code=401, detail="Invalid X-API-KEY")
        
        # Verificar la OpenAI API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="OpenAI API key not found")
        
        client = OpenAI(api_key=api_key)
        
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.message}]
        )
        
        return {"message": completion.choices[0].message.content}
    except Exception as e:
        error_details = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error_details)  # Log error to server console
        raise HTTPException(status_code=500, detail=error_details)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000))) 