import requests
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from resizeimage import resizeimage
import io




def get_resized_img_from_imgURL(url): 
    # return [img, (thumbW, thumbH), (originW, originH)]
    
    
    thumb_size = (100, 100) # wanted thumbsize
    
    r = requests.get(url, allow_redirects=True) # with bytes
    
    image = Image.open(io.BytesIO(r.content)) # it is bytes to normal readed as if from file
    
    origin_size = image.size # original image size from memory not from file as tupple
    
    xy_ratios = [(origin_size[0]/thumb_size[0]),(origin_size[1]/thumb_size[1])]

    if xy_ratios[0] == max(xy_ratios):
        xy_ratio_K = xy_ratios[0]
    
    else:
        xy_ratio_K = xy_ratios[1]  
        
    new_xy_ratios = [(origin_size[0]/xy_ratio_K), (origin_size[1]/xy_ratio_K)]
    rounded_new_xy_ratios = [round(new_xy_ratios[0]),round(new_xy_ratios[1])]
    
    
    thumb_image = image.resize((rounded_new_xy_ratios[0], rounded_new_xy_ratios[1]), Image.ANTIALIAS)    
        
    offset_x = round((thumb_size[0]-new_xy_ratios[0])/2)
    offset_y = round((thumb_size[1]-new_xy_ratios[1])/2)
    offset_xy_tuple = (offset_x, offset_y)
    
    #.paste(thumb_image, offset_xy_tuple)
    
    filled_thumb = Image.new(mode='RGBA',size=thumb_size,color=(255,255,255,0)) # if wanted transparent a = 0
    
    filled_thumb.paste(thumb_image, offset_xy_tuple)
    
    return [filled_thumb, thumb_size, origin_size] # return [img, (thumbW, thumbH), (originW, originH)]
        
        
        
        
        
        
        