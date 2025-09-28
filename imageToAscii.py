from PIL import Image

# ASCII characters from dark to light
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # Adjust height for terminal look
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # Convert to grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"Error opening image: {e}"
    
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    
    ascii_img = "\n".join([ascii_str[i:(i+img_width)] for i in range(0, len(ascii_str), img_width)])
    return ascii_img

if __name__ == "__main__":
    path = input("Enter path to image: ")
    ascii_art = image_to_ascii(path)
    print(ascii_art)
