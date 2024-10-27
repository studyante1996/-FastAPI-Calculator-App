from os import name
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get(path="/", response_class=HTMLResponse)
async def calculator(request: Request):
    return templates.TemplateResponse(
        name="calculator.html",
        context= {"request": request}
        )

@app.post(path="/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request, 
    firstDigit: float = Form(...), 
    secondDigit: float = Form(...), 
    operation: str = Form(...)
    ):
    result = None
    error = None
    if operation == "+":
        result = firstDigit + secondDigit
    elif operation == "-":
        result = firstDigit - secondDigit
    elif operation == "*":
        result = firstDigit * secondDigit
    elif operation == "/":
        if secondDigit != 0:
            result = firstDigit / secondDigit
        else:
            error = "Error: Division by zero"
    
    return templates.TemplateResponse(
        name="calculator.html",
        context={
        "request": request,
        "firstDigit": firstDigit,
        "secondDigit": secondDigit,
        "operation": operation,
        "result": result,
        "error": error
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000
        )
