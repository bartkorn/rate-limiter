import time
from token_bucket import TokenBucket
from multiprocessing import Manager


def test_init():

    token_bucket = TokenBucket(
        bucket_size=5,
        refill_amount=1,
        refill_interval=1,
        manager= Manager()
    )
    assert token_bucket.bucket_size == 5
    assert token_bucket.refill_amount == 1
    assert token_bucket.refill_interval == 1
    assert len(token_bucket.tokens) == 5

def test_get_token():

    token_bucket = TokenBucket(
        bucket_size=5,
        refill_amount=1,
        refill_interval=1,
        manager=Manager()
    )

    token = token_bucket.get_token("test request")
    assert token == "*"


def test_refill():

    token_bucket = TokenBucket(
        bucket_size=5,
        refill_amount=1,
        refill_interval=1,
        manager=Manager()
    )

    token = token_bucket.get_token("test request")
    token = token_bucket.get_token("test request")
    token = token_bucket.get_token("test request")

    time.sleep(1)

    token_bucket.refill("test process")

    assert len(token_bucket.tokens) == 3