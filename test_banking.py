from main import deposit_money, withdraw_money
def test_valid_deposit():
    result = deposit_money(1000,500)
    assert result == 1500
def test_invalid_deposit():
    result = deposit_money(1000, -500)
    assert result == 1000
def test_valid_withdrawal():
    result = withdraw_money(1000, 300)
    assert result == 700
def test_negative_withdrawal():
    result = withdraw_money(1000, -300)
    assert result == 1000
def test_insufficient_funds():
    result = withdraw_money(1000, 2000)
    assert result == 1000
