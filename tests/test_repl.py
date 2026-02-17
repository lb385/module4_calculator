from app.main import run
import runpy


def run_with_inputs(monkeypatch, inputs_list):
    inputs = iter(inputs_list)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))


def test_exit(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["exit"])
    run()
    output = capsys.readouterr().out
    assert "Goodbye" in output


def test_help_then_exit(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["help", "exit"])
    run()
    out = capsys.readouterr().out
    assert "Operations: add, sub, mul, div" in out
    assert "Goodbye" in out


def test_add_and_history(monkeypatch, capsys):
    # add 2 + 3, then show history, then exit
    run_with_inputs(monkeypatch, ["add", "2", "3", "history", "exit"])
    run()
    out = capsys.readouterr().out
    assert "Result: 5.0" in out
    assert "2.0 Add 3.0 = 5.0" in out


def test_divide_by_zero(monkeypatch, capsys):
    run_with_inputs(monkeypatch, ["div", "5", "0", "exit"])
    run()
    out = capsys.readouterr().out
    assert "Error: Division by zero" in out


def test_invalid_operation_and_invalid_number(monkeypatch, capsys):
    # invalid operation
    run_with_inputs(monkeypatch, ["mod", "1", "2", "exit"])
    run()
    out = capsys.readouterr().out
    assert "Error: Invalid operation" in out

    # invalid number input (non-numeric) - then exit
    run_with_inputs(monkeypatch, ["add", "not_a_number", "exit"])
    run()
    out2 = capsys.readouterr().out
    assert "Error:" in out2


def test_module_main_executes(monkeypatch, capsys):
    # Execute module as __main__ to cover the module-level run() call
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    runpy.run_module('app.main', run_name='__main__')
    out = capsys.readouterr().out
    assert "Goodbye" in out
