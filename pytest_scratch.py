import pytest

'''
To list all the test that will be executed without actually running
pytest -sv .\scratch.py -k test_exception --collect-only
'''

'''
Fixtures are functions, which will run before each test function to 
which it is applied. Fixtures are used to feed some data to the tests 
such as database connections, URLs to test and some sort of input data. 
Therefore, instead of running the same code for every test, 
we can attach fixture function to the tests and it will run and 
return the data to the test before executing each test.

A fixture function defined inside a test file has a scope within the test file only. 
We cannot use that fixture in another test file. 
To make a fixture available to multiple test files, 
we have to define the fixture function in a file called conftest.py.

The tests will look for fixture in the same file. As the fixture is not found in the file, 
it will check for fixture in conftest.py file. On finding it, 
the fixture method is invoked and the result is returned to the input argument of the test.

'''
# 1. Fixture with yield:
# The setup_teardown fixture uses yield to separate setup and teardown code.
# The code before yield is executed before the test function.
# The code after yield is executed after the test function finishes.
# 2. Test using the fixture:
# The test_example function takes the setup_teardown fixture as an argument. This automatically triggers the fixture's execution.
@pytest.fixture
def setup_teardown():
    print("Setting up...")
    yield "stage1" # Test runs here
    print("Tearing down1...")
    yield  # Test runs here
    print("Tearing down2...")

def test_example(setup_teardown):
    print("Running test...")
    assert 1 == 1

@pytest.mark.parametrize('direction', ['outbound', 'inbound'])
@pytest.mark.parametrize('site', ['DefaultSite', 'RemoteSite'])
@pytest.mark.parametrize('profile', ['Custom_Profile_1', 'Custom_Profile_2'])
def test_parametrize_case(direction, site, profile):
    print (direction, site, profile)


@pytest.mark.xfail(reason='Bug 192118')
def test_relay_failover_tcp_opt(ez_relay_setup, iperf_tcp_traffic,
                                test_objects):
    pass

skip_flag = True
@pytest.mark.skipif(skip_flag, reason="Table Output parsing not implemented.")
def test_skipif(client):
    pass

@pytest.mark.skip(reason="skip until NX works again.")
def test_skip(client):
    pass