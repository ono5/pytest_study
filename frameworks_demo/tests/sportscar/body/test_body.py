from pytest import mark


@mark.smoke
@mark.body
class BodyTests(object):

    @mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('http://www.motorrend.com/')
        assert True

    def test_bunper(self):
        assert True

    def test_windshielf(self):
        assert True
