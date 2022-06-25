import week4_task2 as bank_app
import pytest

WITHDRAW_AMOUNT=150

def test_transaction_fail(monkeypatch):
    # given
    monkeypatch.setattr('builtins.input', lambda _: WITHDRAW_AMOUNT)

    # when
    bank_app.withdraw_cash(100)

    # then
    assert bank_app.withdraw_cash(100) == 100


def test_transaction_success(monkeypatch):
    # given
    monkeypatch.setattr('builtins.input', lambda _: WITHDRAW_AMOUNT)

    # when
    bank_app.withdraw_cash(200)

    # then
    assert bank_app.withdraw_cash(200) == 50
