import os
import random

import click
import tweepy

from tech.process.array_processor import LingoArrayProcessor
from tech.process.pelican_content_writer import PelicanContentWriter
from tech.process.process import process_techlingos


@click.group()
def cli():
    pass


@cli.command()
def convert():
    processor = PelicanContentWriter()
    process_techlingos(processor)


@cli.command()
def tweet():
    processor = LingoArrayProcessor()
    process_techlingos(processor)
    tweet_content = random.choice(processor.lingos)
    tweet_text = f"{tweet_content.original_title}: {tweet_content.content}\nhttps://techlingo.fyi/{tweet_content.slug}"

    # Authenticate to Twitter
    consumer_key = os.environ["TWITTER_API_KEY"]
    consumer_secret = os.environ["TWITTER_API_SECRET"]
    access_token = os.environ["TWITTER_ACCESS_TOKEN"]
    access_secret = os.environ["TWITTER_ACCESS_SECRET"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    api.update_status(tweet_text)


if __name__ == "__main__":
    cli()
