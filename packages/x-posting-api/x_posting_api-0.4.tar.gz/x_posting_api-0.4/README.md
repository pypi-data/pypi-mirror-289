# Twitter API Package

A simple Python library for posting tweets using Twitter API v2.

## Installation

You can install the package using pip:

```bash
pip install x_posting_api
```

## Usage

```
from x_posting_api import XPostingAPI

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'

def main():
    # Initialize XPostingAPI
    twitter_api = XPostingAPI(CONSUMER_KEY, CONSUMER_SECRET)

    # Authorize (only needed once)
    twitter_api.authorize()

    # Post a tweet
    tweet_text = "Hello world!"
    twitter_api.post_tweet(tweet_text)

if __name__ == "__main__":
    main()

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
