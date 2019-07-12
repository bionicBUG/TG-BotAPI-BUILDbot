import os
from dotenv import load_dotenv

TOKEN = os.environ.get("TOKEN", None)

if TOKEN == None:
    print ("No bot token")
    quit()
    
