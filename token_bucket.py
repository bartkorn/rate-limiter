import multiprocessing
import time
import logging


class TokenBucket:
    """
    Token bucket represents a bucket of MAX tokens refiled with X tokens every second
    """
    def __init__(self, bucket_size: int, refill_rate: int, manager: multiprocessing.Manager):
        self.bucket_size = bucket_size
        self.refill_rate = refill_rate
        self.tokens = manager.list(["*" for token in range(self.bucket_size)])
        self.refill_time = time.time()

    def refill(self, process_name: str) -> None:
        if time.time() - self.refill_time > 5:
            self.refill_time = time.time()
            for token in range(self.refill_rate):
                if not len(self.tokens) >= self.bucket_size:
                    self.tokens.append("*")
                    logging.info(f"[{process_name}] Adding 1 token to the bucket")
        logging.info(f"[{process_name}] Current token count: {len(self.tokens)}")

    def get_token(self, request_name: str) -> str | None:
        if not len(self.tokens) < 1:
            logging.info(f"[{request_name}] Getting 1 token")
            return self.tokens.pop()
        return None
