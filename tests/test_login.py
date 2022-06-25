import week4_task2 as bank_app
import pytest


TEST_PASSWORD = 1234


def test_login_success(monkeypatch, capsys):
    # given
    bank_app.logged_in = False
    monkeypatch.setattr('builtins.input', lambda _: TEST_PASSWORD)

    # when
    bank_app.login(TEST_PASSWORD)

    # then
    assert bank_app.logged_in == True
    captured = capsys.readouterr()
    assert captured.out == '''0
you have Login, please operate your account
'''


def test_login_failure(monkeypatch):
    # given
    bank_app.logged_in = False
    monkeypatch.setattr('builtins.input', lambda _: "9999")

    # when / then
    with pytest.raises(AssertionError):
        bank_app.login(TEST_PASSWORD)


def test_login_success_after_failure(monkeypatch):
    # given
    attempts = ['0000', '9999', TEST_PASSWORD]
    bank_app.logged_in = False
    monkeypatch.setattr('builtins.input', lambda _: attempts.pop(0))

    # when
    bank_app.login(TEST_PASSWORD)

    # then
    assert bank_app.logged_in == True
