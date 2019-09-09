from newspaper import Article

# 

def get_title_text_topimgURL(url):
    # 
    article = Article(url)
    article.download()
    article.parse()
    image_url = article.top_image
    url_title = article.title
    url_text = article.text
    
    return [url, url_title, url_text, image_url] # url, title, text, img_url