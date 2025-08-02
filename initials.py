from PIL import Image, ImageDraw, ImageFont
import random

capital_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def random_initial():
    return capital_letters[random.randint(0,25)]

def random_image_path(reel_type):
    if reel_type == 'initials':
        return "background_images/initials/" + str(random.randint(1,5)) + '.png'
    elif reel_type == 'initials_ranking':
        return "background_images/initials_ranking/" + str(random.randint(1,6)) + '.png'

def add_color_filter(image):
    width, height = image.size
    pixels = image.load()

    for py in range(height):
        for px in range(width):
            r, g, b = image.getpixel((px,py))
            newr = r
            newg = round(g*0.2)
            newb = round(b*0.8)

            pixels[px,py] = (newr, newg, newb)

    return image

def initials_img(img_width=1080, img_height=1080, tile_width=3, tile_height=5, title="These initials go extremely well together:"):
    # load poster and apply pink effect
    poster = add_color_filter(Image.open(random_image_path('initials')).convert('RGB').resize((img_width,img_height)))

    # DRAW TITLE
    draw = ImageDraw.Draw(poster)
    font = ImageFont.truetype('fonts/tiktoksans/static/TikTokSans_18pt_Condensed-Regular.ttf', 40)
    draw.text((60,60), title, font=font, fill="white", stroke_fill="black", stroke_width=2)

    # DRAW INITIALS

    # every pixel one by one
    for i in range(tile_height):
        for j in range(tile_width):

            # Every 60 pixels, initials are drawn.
            draw.text((60+(j*120), 120+(i*60)),
                    f"{random_initial()}+{random_initial()}", 
                    font=font, 
                    fill="white", 
                    align="left", 
                    stroke_fill="black", stroke_width=2)

    poster.save("output/output_poster.png")

def initials_ranking_img(img_width=1080, img_height=1080, list_length=5, title="These initials get the most huzz:"):

    # load poster and apply pink effect
    poster = Image.open(random_image_path('initials_ranking')).convert('RGB').resize((img_width,img_height))

    # DRAW TITLE
    draw = ImageDraw.Draw(poster)
    font = ImageFont.truetype('fonts/tiktoksans/static/TikTokSans_18pt_Condensed-Regular.ttf', 80)
    draw.text((60,60), title, font=font, fill="white", stroke_fill="black", stroke_width=2)

    for i in range(list_length):
        
        if i==0:
            draw.text((480,180),
                      '! ' + random_initial(),
                      font=font,
                      fill="white",stroke_fill="black",stroke_width=2)
        elif i==1:
            draw.text((480,300),
                      '@ ' + random_initial(),
                      font=font,
                      fill="white",stroke_fill="black",stroke_width=2)
        elif i==2:
            draw.text((480,420),
                      '# ' + random_initial(),
                      font=font,
                      fill="white",stroke_fill="black",stroke_width=2)
        elif i>=3:
            draw.text((480, 300+(i*80)),
                      str(i+1) + ' ' + random_initial(),
                      font=font,
                      fill="white",stroke_fill="black",stroke_width=2)

    poster.save("output/output_poster.png")

if __name__ == '__main__':
    print('''
    ___         __        ____            __
   /   | __  __/ /_____  / __ \___  ___  / /
  / /| |/ / / / __/ __ \/ /_/ / _ \/ _ \/ / 
 / ___ / /_/ / /_/ /_/ / _, _/  __/  __/ /  
/_/  |_\__,_/\__/\____/_/ |_|\___/\___/_/
   The method to farm Instagram Reels!''')
    
    print('How many reels would you like to create today?')
    reel_amount = int(input())
    for i in range(reel_amount):
        
        # MENU
        print('''Please select from this menu:
                    1. Initials reel
                    2. Initials ranking reel''')
        q1 = input()

        # INITIALS REEL SELECTION
        if q1 == '1':
            print(chr(27) + "[2J")
            print('You will be asked for some information about the reel you want to make.')
            print('Please input the desired image width (when leaving the field empty, the default amount (1080px) will be chosen):', end="")
            image_width = input()
            if image_width == '':
                print(1080)
                image_width = 1080
            else:
                image_width = int(image_width)
            print('Please input the desired image height (when leaving the field empty, the default amount (1080px) will be chosen):', end="")
            image_height = input()
            if image_height == '':
                print(1080)
                image_height = 1080
            else:
                image_height = int(image_height)

            print('Please input the grid size of the initials you want (Width x Height). For example: if you want 20 initials on one page, you can input 4x5.\nYou can leave this field empty as well, the default is 3x5.', end ="")
            grid_size = input()
            if grid_size == '':
                print('3x5')
                grid_width, grid_height = 3, 5
            else:
                grid_width, grid_height = grid_size.split('x')
                grid_width = int(grid_width)
                grid_height = int(grid_height)

            print('Please input the title you want at the top of the reel. The default title is: "These initials go extremely well together:".', end="")
            title = input()
            if title == '':
                print('These initials go extremely well together:')
                title = "These initials go extremely well together:"

            initials_img(image_width, image_height, grid_width, grid_height, title)

        elif q1 == '2':
            print(chr(27) + "[2J")
            print('You will be asked for some information about the reel you want to make.')

            print('Please input the desired image width (when leaving the field empty, the default amount (1080px) will be chosen):', end="")
            image_width = input()
            if image_width == '':
                print(1080)
                image_width = 1080
            else:
                image_width = int(image_width)
            print('Please input the desired image height (when leaving the field empty, the default amount (1080px) will be chosen):', end="")
            image_height = input()
            if image_height == '':
                print(1080)
                image_height = 1080
            else:
                image_height = int(image_height)

            print('Please input the title you want at the top of the reel. The default title is: "These initials go extremely well together:".', end="")
            title = input()
            if title == '':
                print('These initials go extremely well together:')
                title = "These initials go extremely well together:"

            print('Please enter the amount of ranking places you want to see in the reel. The default is 5.', end="")
            list_length = input()
            if list_length == '':
                print('5')
                list_length = 5
            else: 
                list_length = int(list_length)

            initials_ranking_img(image_width, image_height, list_length, title)

        print('\n\n')
        print(f'✅ Reel {i+1}/{reel_amount} finished.')
        print('The finished reel is saved in the "output" folder.')