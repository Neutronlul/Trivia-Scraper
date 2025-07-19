import os

from dotenv import load_dotenv

load_dotenv()
baseURL = os.getenv("TARGET_URL")
pageCounter = 1

print(baseURL + str(pageCounter))
