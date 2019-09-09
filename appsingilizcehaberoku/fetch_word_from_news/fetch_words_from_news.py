from newspaper import Article
import nltk, re, pprint
from nltk import word_tokenize
import string
from yandex.Translater import Translater


tr = Translater()

tr.set_key('trnsl.1.1.20190620T080928Z.059272b876400ab5.db9848757da3b1698721fef656db05d4903c4d1b')

tr.set_from_lang('en')
tr.set_to_lang('tr')

nltk.download('words')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

#get stopwords, corpus-words

from nltk.corpus import words
from stop_words import get_stop_words
from nltk.corpus import stopwords


stop_words = list(get_stop_words('en'))         #Have around 900 stopwords
nltk_words = list(stopwords.words('english'))   #Have around 150 stopwords
stop_words.extend(nltk_words)





def fetch_words_from_news(url):
    # return [[],[]] 0: en, 1:tr
    article = Article(url)
    article.download()
    article.parse()

    for_nltk = []
    news_text = article.text
    for_nltk.append(article.text)
    news_text = news_text.upper()
    news_text_wo_rn = news_text.replace('\n', ' ')
    news_text_wo_rn = news_text_wo_rn.replace('\r', ' ')
    news_text_list = news_text_wo_rn.split(' ')
    news_text_list = set(news_text_list)
    tokenized_sents = [word_tokenize(i) for i in for_nltk]
    
    
    # remove punctuations from list
    
    res = []
    new_res = []
    
    
    #s.translate(None, string.punctuation)
    
    #res = [s.translate(str.maketrans('', '', string.punctuation)) for s in tokenized_sents[0]
    
    for tixt in tokenized_sents[0]:
        new_tixt = ''.join(c.translate(str.maketrans('', '', string.punctuation+'“”')) for c in tixt if c not in string.punctuation+'“”')
        res.append(new_tixt)
        
        
    for d in res:
        if not d == '':
            new_res.append(d)
            
            
    
    capitalized_new_res = [KAP.upper() for KAP in new_res]
    
    
    capitalized_setted_new_res = set(capitalized_new_res)
    
    # delete one len item
    
    more_than_one_len_CSNR = []
    
    for e in capitalized_setted_new_res:
        if not len(e) < 2:
            more_than_one_len_CSNR.append(e)
            
            
    # delete numbers
    
    digitless_more_than_OLC = []
    
    for g in more_than_one_len_CSNR:
        if g.isalpha():
            digitless_more_than_OLC.append(g)    
    
    
    tags_of_diggless = [nltk.pos_tag(f) for f in digitless_more_than_OLC]
    tags_of_diggless_2 = nltk.pos_tag(digitless_more_than_OLC)
    
    prepless_digitless_MTO = []
    
    for h in digitless_more_than_OLC:
        if not h.lower() in stop_words:
            prepless_digitless_MTO.append(h)
    
    
    if_word_in_cor_PDMTO = []
    TR_if_word_in_cor_PDMTO = []
        
    for g in prepless_digitless_MTO:
        if g.lower() in words.words():
            if_word_in_cor_PDMTO.append(g)
            tr.set_text(g)
            TR_if_word_in_cor_PDMTO.append(tr.translate())
    
    return [if_word_in_cor_PDMTO, TR_if_word_in_cor_PDMTO] # return [[],[]] 0: en, 1:tr
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    