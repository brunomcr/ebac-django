import pytest

from mysite.myapp.factories import PostFactory
#from myapp.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
