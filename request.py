from token_bucket import TokenBucket
import logging


class Request:

    def __init__(self, name):
        self.name = name
        self.statistics = {
            "successful": 0,
            "throttled": 0,
            "total": 0
        }

    def make(self, token_bucket: TokenBucket) -> None:
        if token_bucket.get_token(self.name):
            logging.info(f"[{self.name}] Successful request.")
            self.statistics["successful"] += 1
        else:
            logging.info(f"[{self.name}] Request throttled.")
            self.statistics["throttled"] += 1
        self.statistics["total"] += 1
