import os
import urllib.request

# You could use your web browser to download the file
# But I prefer this solution

DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/dwyl/english-words/master/'
WORDS_PATH = os.path.join('datasets','words')
WORDS_URL = DOWNLOAD_ROOT + 'words_alpha.txt'


def fetch_words_data(words_path=WORDS_PATH,words_url=WORDS_URL):
    ''' Download the Data '''
    os.makedirs(words_path,exist_ok=True)
    words_alpha = os.path.join(words_path,'words_alpha.txt')
    urllib.request.urlretrieve(words_url,words_alpha)
    f = open(words_alpha,'r+')
    dataset = f.read()
    dataset = dataset.splitlines() 
    f.close()
    
    return dataset

df = fetch_words_data() 