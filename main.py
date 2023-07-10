from PIL import Image, ImageEnhance


black_white_ramp = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`.'
ori_image = ''
new_image = ''
pixels = ''
ori_width, ori_height = 0, 0
new_width, new_height = 0, 0
x_scale = 256
y_scale = 256
white_text = True
strings = []


def load_from(load_path):
    return Image.open(load_path)


def menu():
    global ori_image
    global pixels
    global ori_width, ori_height
    global new_width, new_height
    global x_scale
    global y_scale
    global white_text
    ori_image = load_from(str(input("paste the path for the image here: ")))
    x_scale = int(input("X-axis Image Scale (full = 256): "))/256
    y_scale = int(input("Y-axis Image Scale (full = 256): ")) / 256
    enhancement = float(input("Contrast Enhancement Factor: "))
    if str(input("white text (y/n): ")) == "y":
        white_text = True
    else:
        white_text = False
    ori_width, ori_height = ori_image.size
    rescale(enhancement)  # modifies image to scale
    pixels = new_image.load()  # get the pixels with the remade image
    new_width, new_height = new_image.size
    convert_to_string()

    # output
    for i in range(len(strings)):
        print(strings[i])  # this way they are in order


def rescale(enhancement):
    global ori_image
    global new_image
    temp = (ori_image.convert('RGB')).resize((int(ori_width*x_scale), int(ori_height*y_scale)), Image.LANCZOS)
    new_image = (ImageEnhance.Contrast(temp)).enhance(enhancement)


def convert_to_string():
    global new_image
    for y in range(new_height):
        string = ''
        for x in range(new_width):
            brightness = sum(pixels[x, y])/3/255  # average and convert to 0 to 1
            selector = round((len(black_white_ramp)-1)*brightness)  # increasing with brightness
            if white_text:
                character = black_white_ramp[len(black_white_ramp)-selector]
            else:
                character = black_white_ramp[selector]
            string += character
        strings.append(string)


menu()
