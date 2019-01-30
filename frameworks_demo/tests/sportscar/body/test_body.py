from pytest import mark


@mark.body
class BodyTests(object):
    @mark.door
    @mark.body
    def test_body_functions_as_expected(self):
        assert True

    def test_bunper(self):
        assert True

    def test_windshielf(self):
        assert True
