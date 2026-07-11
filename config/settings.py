import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

TEST_EMAIL = os.getenv("TEST_EMAIL")

TEST_PASSWORD = os.getenv("TEST_PASSWORD")