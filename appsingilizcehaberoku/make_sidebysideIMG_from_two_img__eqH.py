from PIL import Image






def make_sidebysideIMG_from_two_img__eqH(img1, img2):
    # return [image, (W, H)]
    
    img1_w = img1.size[0]
    img2_w = img2.size[0]
    
    imgs_h = img1.size[1] # or img2.size[1] because they have the same H
    
    
    
    sided_img_W = img1_w + img2_w
    
    img_size_tupple = (sided_img_W, imgs_h)
    
    sided_img = Image.new(mode='RGBA',size=img_size_tupple,color=(255,255,255,0)) # if not wanted transparent a = 1
    
    sided_img.paste(img1, (0,0))
    
    sided_img.paste(img2, (img1_w,0))
    
    return [sided_img, img_size_tupple]