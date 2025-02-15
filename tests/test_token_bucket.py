import pytest
from token_bucket import TokenBucket
from unittest.mock import patch, MagicMock


@patch("multiprocessing.Manager")
def test_init(mock_manager):
    mock_manager_instance = MagicMock()
    mock_manager_instance.list.return_value = []
    mock_manager.return_value = mock_manager_instance

    token_bucket = TokenBucket(
        bucket_size=5,
        refill_amount=1,
        refill_interval=1,
        manager=mock_manager
    )
    assert token_bucket.bucket_size == 5
    assert token_bucket.refill_amount == 1
    assert token_bucket.refill_interval == 1

