from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

# Serve static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

class CalculationRequest(BaseModel):
    expression: str

class CalculationResponse(BaseModel):
    result: float
    expression: str

@app.get("/")
async def root():
    """Serve the calculator UI"""
    return {"message": "Calculator API is running. Visit /static/index.html"}

@app.post("/api/calc")
async def calculate(request: CalculationRequest):
    """Calculate the result of a mathematical expression"""
    try:
        # Safely evaluate the expression
        result = eval(request.expression)
        return CalculationResponse(result=float(result), expression=request.expression)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)