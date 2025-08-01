from PIL import Image, ImageDraw, ImageFont
import random

capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def initials_img(width=1080, height=1080, tile_width=3, tile_height=5, title=""):
    # init
    poster = Image.open(f'background_images/{random.randint(1,5)}.png').convert('RGBA').resize((width,height))

    # DRAW TITLE
    draw = ImageDraw.Draw(poster)
    font = ImageFont.truetype('fonts/tiktoksans/static/TikTokSans_18pt_Condensed-Regular.ttf', 40)
    draw.text((60,60), "These initials go extremely well together:", font=font, fill="white", stroke_fill="black", stroke_width=2)

    # DRAW INITIALS

    for i in range(tile_height):
        for j in range(tile_width):
            draw.text((60+(j*120), 120+(i*60)), 
                    f"{capital_letters[random.randint(0,25)]}+{capital_letters[random.randint(0,25)]}", 
                    font=font, 
                    fill="white", 
                    align="left", 
                    stroke_fill="black", stroke_width=2)

    poster.save("output/output_poster.png")

initials_img()