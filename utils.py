
import datetime as datetime
import secrets

def createdId(data):
  data_length = len(data)
  last_itemId = data[data_length - 1]["Id"]
  return last_itemId + 1

def createdDate():
  return datetime.datetime.now()

def createToken():
  return secrets.token_hex(16)
