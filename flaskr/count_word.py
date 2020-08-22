import requests
from collections import Counter
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
import re
from models import Result
from app import db



def word_count(url):
    
    r = requests.get(url)
    raw = BeautifulSoup(r.text).get_text()
    nltk.data.path.append('./nltk_data')
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
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
    
       
    