from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai
from openai import OpenAI

print(f"OpenAI version: {openai.__version__}")

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
    return {"status": "ok"}

@app.post("/api/test-gpt")
async def test_gpt(request: ChatRequest):
    try:
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
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000))) 