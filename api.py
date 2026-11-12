from pydantic import BaseModel
from main import deposit_money, withdraw_money
from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

@app.get("/account/{account_id}")
def get_account(account_id: int):
    connection = sqlite3.connect("banking.db")
    cursor = connection.execute(
        "SELECT * FROM accounts WHERE account_id = ?", (account_id,)
    )
    account = cursor.fetchone()
    connection.close()

    if account is None:
        raise HTTPException(status_code=404, detail ="Account not found")
    return { "account_id": account[0], "name": account[1], "balance_cents": account[2] }


class DepositRequest(BaseModel):
    balance: float
    deposit: float

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