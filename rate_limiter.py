import time
import multiprocessing
import logging
import random
import typer
from typing_extensions import Annotated
from token_bucket import TokenBucket
from request import Request

app = typer.Typer()

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def refiller(token_bucket: TokenBucket, lock: multiprocessing.Lock, process_name: str, stop_event: multiprocessing.Event):
    while not stop_event.is_set():
        with lock:
            token_bucket.refill(process_name)
            time.sleep(0.5)


@app.command()
def run(max_time: Annotated[int, typer.Argument(help="Maximum number of time in seconds to run the simulation.")],
        max_requests: Annotated[int, typer.Argument(help="Maximum number of random requests to perform during simulation.")],
        token_count: Annotated[int, typer.Argument(help="Bucket size represented by maximum amount of tokens.")],
        refill_amount: Annotated[int, typer.Argument(help="Amount of tokens added to the bucket in given time interval.")],
        refill_interval: Annotated[int, typer.Argument(help="Time interval [in seconds] in which tokens are added to the bucket")]):

    """Simulates performing requests against a rate limiting middleware using token bucket algorithm. Simulation runs until MAX_TIME elapses or MAX_REQUESTS are performed."""
    with multiprocessing.Manager() as manager:
        shared_token_bucket = TokenBucket(bucket_size=token_count, refill_amount=refill_amount, refill_interval=refill_interval, manager=manager)
        shared_lock = multiprocessing.Lock()
        shared_event = multiprocessing.Event()
        process1 = multiprocessing.Process(target=refiller,
                                           args=(shared_token_bucket, shared_lock, "refiller-process", shared_event))
        process1.start()

        start_time = time.time()
        request1 = Request("GET/")

        while time.time() - start_time < max_time and request1.statistics["total"] < max_requests:
            request1.make(shared_token_bucket)
            time.sleep(random.randint(1, 5))

        elapsed = time.time() - start_time
        shared_event.set()
        process1.join()

        logging.info(f"Request statistics in {elapsed:.2f} seconds: \n{request1.statistics}")


if __name__ == "__main__":

    app()


