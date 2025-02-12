# Rate Limiter
This repository contains an example simulator of rate-limiting middleware implemented using the token bucket algorithm. Rate limiting is a technique used to control the rate at which requests are processed, ensuring system stability and preventing abuse.

## Features
**Token Bucket Algorithm:** Efficiently manages request rates by allowing bursts of traffic up to a defined limit while maintaining a steady flow over time.

**Simulation Environment:** Provides a framework to simulate and test the behavior of the rate limiter under various conditions.

## Getting Started
### Prerequisites
Python 3.x

### Installation
Clone the Repository:
```bash
git clone https://github.com/bartkorn/rate-limiter.git
cd rate-limiter
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

## Usage
The simulator allows you to test the rate-limiting behavior by configuring parameters such as token generation rate and bucket capacity.

### Configure Parameters:

Experiment with max_time, max_requests parameters to establish for how long (in seconds) the simulation should run or how many requests to make. Set token_count and refill_rate to configure bucket size and the amount of tokens refilled every second. 

### Run the Simulator:
```bash
python rate_limiter.py
```
The simulator will process a series of requests and output the results, indicating which requests were allowed and which were rate-limited.

### Help:

```bash
python rate_limiter.py --help
```
Use cmd-line help to see available run options and mandatory parameters

### Project Structure
`rate_limiter.py`: Main script that sets up and runs the rate-limiting simulation.
`token_bucket.py`: Contains the implementation of the token bucket algorithm.
`request.py`: Defines the request model used in the simulation.
`requirements.txt`: Lists the Python dependencies required for the project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
