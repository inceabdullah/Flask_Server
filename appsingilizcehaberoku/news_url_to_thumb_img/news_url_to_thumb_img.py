import get_title_text_topimgURL # [url, title, text, img_url]
import text_2_md5_hash # just returns str hashed from any text
import get_resized_img_from_imgURL # [img, (thumbW, thumbH), (originW, originH)] like [<PIL.Image.Image image mode=RGBA size=100x100 at 0x7F1576BC2CF8>, (100, 100), (1050, 550)] 
import make_fittedFRAMED_textIMG # [image, (width, height)] like [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=220x100 at 0x7FE86925EF98>, (220, 100)]

import make_sidebysideIMG_from_two_img__eqH # return [image, (W, H)]


def news_url_to_thumb_img(url):
    # return [img, filename]
    
    geted_infos = get_title_text_topimgURL.get_title_text_topimgURL(url)
    
    img_url = geted_infos[3]
    title = geted_infos[1]
    url = geted_infos[0]
    
    file_name = text_2_md5_hash.text_2_md5_hash(url)
    
    geted_top_img = get_resized_img_from_imgURL.get_resized_img_from_imgURL(img_url)[0]
    
    maked_text_img = make_fittedFRAMED_textIMG.make_fittedFRAMED_textIMG(title)[0]
    
    sided_img = make_sidebysideIMG_from_two_img__eqH.make_sidebysideIMG_from_two_img__eqH(geted_top_img, maked_text_img)[0]
    
    filename_for_png = file_name+".png"
    
    return [sided_img, filename_for_png] # [img, filename]