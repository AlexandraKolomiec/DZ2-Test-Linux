from checkout import checkout
from  checkout import  crc32

path_dir = '/home/user/tst'
path_arch: str = '/home/user/arx2'


def test_step1():
    assert checkout('cd {}; 7z a {}'.format(path_dir, path_arch), "Everything is OK"), "Test1 Fail"


def test_step2():
    assert checkout('echo:"Hello"', "Hello")


def test_step3():
    assert checkout('cd {}; 7z u {}'.format(path_dir, path_arch), "Everything is OK"), "Test3 Fail"


def test_step4():
    assert checkout('cd {}; 7z d {}'.format(path_dir, path_arch), "Everything is OK"), "Test4 Fail"


# Для просмотра внутренностей используется команда l: 7z l arch.7z, 7z l -slt arch.7z
def test_step7():
    assert checkout("cd {}; 7z l {}".format(path_dir, path_arch), "Everything is OK"), "Test7 Fail"


# Для извлечения содержимого из архива arch.7z в текущую директорию, выполните в терминале:  7z x arch.7z
# Если архив разбит на множество частей, используйте имя с наименьшим номером тома: 7z x arch.7z.001
# Если вы хотите извлечь архив не в текущей диреkтории, вы можете явно задать целевую директорию с помощью опции -o
# 7z x arch.7z -o/home/user/Desktop/TheExtractionDir
def test_step8():
    assert checkout("cd {}; 7z x arx2.7z -o{}".format(path_dir, path_arch), "Everything is OK"), "Test8 Fail"


def test_step9(b=None):
    if crc32(b, 'h_crc') == checkout('7z h {}'.format(path_arch), "Everything is OK"):
        return True
    else:
        return False

""" System ERROR:
Неизвестная ошибка -2147024872
========================================================== short test summary info ==
FAILED test_positive.py::test_step1 - AssertionError: Test1 Fail
FAILED test_positive.py::test_step2 - assert False
FAILED test_positive.py::test_step3 - AssertionError: Test3 Fail
FAILED test_positive.py::test_step4 - AssertionError: Test4 Fail
FAILED test_positive.py::test_step7 - AssertionError: Test7 Fail
FAILED test_positive.py::test_step8 - AssertionError: Test8 Fail
======================================================== 6 failed, 1 passed in 0.14s ="""