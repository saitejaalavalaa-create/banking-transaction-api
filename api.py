from pydantic import BaseModel
from main import deposit_money, withdraw_money
from fastapi import FastAPI, HTTPException

class DepositRequest(BaseModel):
    balance: float
    deposit: float
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to the Banking Transaction API!"}

@app.post("/deposit")
def deposit(request: DepositRequest):
    if request.deposit <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount cannot be negative.")
    updated_balance = deposit_money(request.balance, request.deposit)
    return{"updated_balance": updated_balance}

class WithdrawRequest(BaseModel):
    balance: float
    withdrawal: float
@app.post("/withdraw")
def withdraw(request: WithdrawRequest):
    if request.withdrawal <= 0:
        raise HTTPException(status_code=400, detail="Deposit amount must be greater than zero.")
    if request.withdrawal > request.balance:
        raise HTTPException(status_code=400, detail="Insufficient funds for withdrawal.")
    updated_balance = withdraw_money(request.balance, request.withdrawal)
    return {"updated_balance": updated_balance}