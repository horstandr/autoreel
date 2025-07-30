from PIL import Image, ImageDraw, ImageFont
import random

poster = Image.open('background_images/1.png').convert('RGBA').resize((1080,1080))

# DRAW TITLE
draw = ImageDraw.Draw(poster)
font = ImageFont.truetype('fonts/tiktoksans/static/TikTokSans_18pt_Condensed-Regular.ttf', 40)
draw.text((60,60), "These initials go extremely well together:", font=font, fill="white", stroke_fill="black", stroke_width=2)

width = 2
height = 5

# DRAW INITIALS
for i in range(height):
    for j in range(width):
        draw.text((60+(j*120), 120+(i*60)), "W+W", font=font, fill="white", align="left", stroke_fill="black", stroke_width=2)

poster.save("output/output_poster.png")