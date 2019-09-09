from newspaper import Article

# 

def get_title_text_topimgURL(url, img_fetch=False, text_fetch=False):
    # 
    article = Article(url)
    article.download()
    article.parse()
    image_url = ""
    url_text= ""
    if not img_fetch == False:
        image_url = article.top_image
    if not text_fetch == False:    
        url_text = article.text
    
    url_title = article.title
    
    return [url, url_title, url_text, image_url] # url, title, text, img_url