import pytest


@pytest.fixture(scope='function')
def generate_trap():
    print("Setup: Configurations on scm, snmp server")
    return True


@pytest.fixture(scope='function')
def snmp_scm_cleanup(generate_trap, request):
    """Configure default snmp settings for cleanup."""
    def configure_default_snmp():
        print("Teardown: set Default snmp settings")

    request.addfinalizer(configure_default_snmp)


@pytest.fixture
def mail_admin():
    print("Inside mail_admin")
    return True


@pytest.fixture
def sending_user(mail_admin):
    print("Inside sending_user")
    user = "sending_user1"
    yield user
    delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    print("Inside receiving_user")
    user = "receiving_user1"
    yield user
    delete_user(user)


# @pytest.fixture
def delete_user(user):
    print("delete_user deleted {}".format(user))
