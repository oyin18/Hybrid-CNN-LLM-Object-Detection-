import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("AIzaSyDXrkprOF8URfaMENhbeN8bLrG9vevdGls")

if api_key:
    print('loaded')
else:
    print('not loaded, check your env file!')