import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))

DBHOST =  str(os.getenv("DBHOST"))
DATABASE = str(os.getenv("DATABASE"))

#POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
POSTGRES_URI = "postgres://pewltqqyuvured:4e290e282f8631977af14ddcfca5db812bc6a0d1c4ceb96dd0b89d0cc3deb264@ec2-52-19-170-215.eu-west-1.compute.amazonaws.com:5432/d2g3jv2p1vmtnb"