import os
import tweepy
from gateway import Gateway


class XGateway(Gateway):
    def __init__(self):
        """
        Initialize the X (Twitter) API gateway.
        Loads API credentials from environment variables.
        """
        self.api_key = os.getenv("X_API_KEY")
        self.api_secret = os.getenv("X_API_KEY_SECRET")
        self.access_token = os.getenv("X_API_ACCESS_TOKEN")
        self.access_token_secret = os.getenv("X_API_ACCESS_TOKEN_SECRET")
        self.bearer_token = os.getenv("X_API_BEARER_TOKEN")

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "API credentials not found. Please set X_API_KEY and X_API_SECRET in your .env file."
            )

        # Initialize Tweepy client with API v2
        if self.bearer_token:
            self.client = tweepy.Client(
                bearer_token=self.bearer_token,
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
            )
        else:
            # Fallback to OAuth 1.0a if bearer token not available
            self.client = tweepy.Client(
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
            )

    def post(self, text: str) -> bool:
        """
        Post a tweet with the given text.

        Args:
            text: The tweet content (max 280 characters)

        Returns:
            bool: True if the tweet was posted successfully, False otherwise
        """
        try:
            response = self.client.create_tweet(text=text)
            self.log(f"text: {text}")
            self.log(f"response: {response}")
            return response.data is not None
        except Exception as e:
            self.log(f"Error posting tweet: {e}")
            return False
