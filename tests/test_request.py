from request import Request
from token_bucket import TokenBucket
from multiprocessing import Manager

def test_init():

    request = Request("test request")

    assert request.name == "test request"
    assert request.statistics["successful"] == 0
    assert request.statistics["throttled"] == 0
    assert request.statistics["total"] == 0


def test_make():

    token_bucket = TokenBucket(5, 1, 1, Manager())
    request = Request("test request")
    request.make(token_bucket)

    assert request.statistics["successful"] == 1
    assert request.statistics["total"] == 1