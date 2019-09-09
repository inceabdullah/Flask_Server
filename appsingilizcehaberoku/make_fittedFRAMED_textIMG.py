from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

print("(text, centered_one_line_TF, COL_textSize, COL_bgName)")
print("""make_fittedFRAMED_textIMG.make_fittedFRAMED_textIMG("CONTRUCTIONSSZZ", True, 24, "bg_320x50.png")""")
print("ya da")
print("""make_fittedFRAMED_textIMG.make_fittedFRAMED_textIMG("Bakın da ne dedi??", False, 24, "bg_320x50.png", True, (220,100),18)""")

def make_fittedFRAMED_textIMG(text, centered_one_line_TF = False, COL_textSize = 23, COL_bgName = 'background.png', AutoWhiteBg = False, BgFrameSize = (220,100), AutoBgFontSize = 18):


        
    # return [image, (width, height)] like [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=220x100 at 0x7FE86925EF98>, (220, 100)] centered_one_line_TF: True, False; COL_imgSize: tupple; COL_textSize: int
    

    def text_wrap(text, font, max_width):
        lines = []
        # If the width of the text is smaller than image width
        # we don't need to split it, just add it to the lines array
        # and return
        if font.getsize(text)[0] <= max_width:
            lines.append(text) 
        else:
            # split the line by spaces to get words
            words = text.split(' ')  
            i = 0
            # append every word to a line while its width is shorter than image width
            while i < len(words):
                line = ''         
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                    line = line + words[i] + " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                # when the line gets longer than the max width do not append the word, 
                # add the line to the lines array
                lines.append(line)    
        return lines
 
 
    def draw_text(text):    
        # open the background file
        if AutoWhiteBg == False:
            if not centered_one_line_TF == True:
                img = Image.open('background.png')
            else:
                img = Image.open(COL_bgName)
                
        else:
            img = Image.new(mode='RGB',size=BgFrameSize,color=(255,255,255))
            
        draw = ImageDraw.Draw(img)
        # size() returns a tuple of (width, height) 
        image_size = img.size # [0] probably width
 
        # create the ImageFont instance
        font_file_path = 'fonts/AbhayaLibre-Medium.ttf'
        if not centered_one_line_TF == True:
            font_size = 23
        else:
            font_size = COL_textSize
            
        if AutoWhiteBg == True:    
            font_size = AutoBgFontSize
            
        font = ImageFont.truetype(font_file_path, size=font_size, encoding="utf-8")
 
        # get shorter lines
        lines = text_wrap(text, font, image_size[0])
        line_height = font.getsize('hg')[1]
        
        if centered_one_line_TF == True:
            one_line_text = text
            one_line_text_sizes = font.getsize(one_line_text)
            one_line_text_sizes_w = one_line_text_sizes[0]
            one_line_text_sizes_h = one_line_text_sizes[1]
            oring_img_w = image_size[0]
            oring_img_h = image_size[1]
            offset_w = round((oring_img_w-one_line_text_sizes_w)/2)
            offset_h = round((oring_img_h-one_line_text_sizes_h)/2)
            offset_tupple = (offset_w, offset_h)

        line_say = 0 
        x = 1
        y = 1
        
        if not centered_one_line_TF == True:
        
            for line in lines:
                line_say += 1
        
                if line_say == 3:
                    if len(line) >= 3:
                        line = line[0:(len(line)-2)]+".."

                if not line_say >= 4:
                    # draw the line on the image
                    draw.text((x, y), line, fill="black", font=font)
    
                    # update the y position so that we can use it for next line
                    y = y + line_height
                    
        else:
            
            draw.text(offset_tupple, one_line_text, fill="black", font=font)
                
            
        
    
        #print(lines)# ['This could be a single line text ', 'but its too long to fit in one. ']
        return [img, img.size] # [image, (width, height)]
        
        
    
    
    return_list_from_inside_def = draw_text(text)
    
    return return_list_from_inside_def # [image, (width, height)] like [<PIL.PngImagePlugin.PngImageFile image mode=RGBA size=220x100 at 0x7FE86925EF98>, (220, 100)]
    
   