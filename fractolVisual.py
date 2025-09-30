
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.zeros((height, width))
    
    for i in range(width):
        for j in range(height):
            c = x[i] + 1j * y[j]
            img[j, i] = mandelbrot(c, max_iter)
    return img

def show_fractal():
    print("Generating Mandelbrot fractal... this might take a few seconds.")
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5
    width, height = 800, 800
    max_iter = 256
    
    img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap="magma")
    plt.colorbar()
    plt.title("Mandelbrot Fractal")
    plt.show()

if __name__ == "__main__":
    show_fractal()
