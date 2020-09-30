import app
from flask import Flask
import urllib.request, json

def random_quotes():


  """Function that formats the data from API into a list using the zip 
      function ready for consumption"""

   
  with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as quotes:
    quotes_open = quotes.read()
    quotes_open_response = json.loads(quotes_open)
  return quotes_open_response


  

    
