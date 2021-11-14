File Name To Recognise to pytest should in below format:

    test_*.py
    *_test.py
    and then run pytest command 
    if you have created a package for test python file explicitly than this package should have __init__.py
    pytest --help for more functionalties

Commands:

    pytest
    pytest -v (it will also give method name)
    pytest -v -s (it will also print the print statment of test methods)
    pytest -v -s tests/test_user.py (to run only specific module)
    pytest -v -s -x (-x => this command will stop the process of test if anyone test is failed)
    => above way is usefull when we have large number of tests 
    



