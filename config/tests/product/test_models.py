import pytest

pytestmark = pytest.mark.django_db


class TestCategory:
    def test_str_method(self, category_factory):
        x=category_factory(name='test_category')
        assert x.__str__() == 'test_category'


# class TestBrand:
#     def test_category_model():
#         pass



# class TestProduct:
#     def test_category_model():
#         pass        