from src.decorators import log


def test_log1():
    @log(filename="log_file.txt")
    def func(x, y):
        return x / y

    assert func(6, 1) == 6


def test_log2(capsys):
    @log()
    def func(x, y):
        return x / y

    func(6, 1)
    cap = capsys.readouterr()
    assert cap.out == "func ok\n"


def test_log3(capsys):
    @log()
    def func(x, y):
        return x / y

    func(6, 0)
    cap = capsys.readouterr()
    assert cap.out == "func error: ZeroDivisionError. Inputs:((6, 0),{}). division by zero\n"
