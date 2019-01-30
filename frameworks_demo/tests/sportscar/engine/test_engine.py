from pytest import mark


@mark.door
@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True

