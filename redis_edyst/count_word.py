import requests
from collections import Counter
from bs4 import BeautifulSoup
import re
from models import Result
from app import db



def word_count(url):
    
    r = requests.get(url)
    raw = BeautifulSoup(r.text).get_text()
    text = raw.replace("\n", "").split(" ")
    flat_data = re.compile('.*[A-Za-z].*')
    raw_words = [w for w in text if flat_data.match(w)]
    count_data = Counter(raw_words) 
    
    
    result = Result(
            url=url,
            count_data=count_data
        )
    db.session.add(result)
    db.session.commit()
    return result.id
    
       
    