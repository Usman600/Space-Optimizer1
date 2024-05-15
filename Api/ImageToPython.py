from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt
import io

def random_number(existing_colors, threshold=100):
    if existing_colors == []:
        existing_colors = [np.random.randint(0, 256, size=3, dtype=np.uint8)]
    existing_colors = np.array(existing_colors)
    while True:
        new_color = np.random.randint(0, 256, size=3, dtype=np.uint8)
        if np.all(np.linalg.norm(new_color - existing_colors, axis=1) > threshold):
            break
    return new_color

def convert_to_3d_array(data):
    unique_values = np.unique(data)

    my_dict = {}  # Create an empty dictionary
    for i in unique_values:
        temp = np.array([100, 100, 100], dtype=np.uint8)
        if i == 0:
            temp = np.array([255, 255, 255], dtype=np.uint8)
        elif i > 0:
            temp = random_number(list(my_dict.values()))
        my_dict[i] = temp

    # Convert my_dict values to NumPy arrays
    my_dict = {k: np.array(v) for k, v in my_dict.items()}

    # Map each value in the input data to its corresponding color
    converted_data = np.array([my_dict[val] for val in data.flat], dtype=np.uint8)
    converted_data = converted_data.reshape(data.shape + (3,))  # Reshape to 3D array
    return converted_data
def plot(image_array):
    image_3d_array = convert_to_3d_array(np.array(image_array))
    plt.imshow(image_3d_array)
    plt.show()
    plt.close()

def Create_Irreguar(path):
    image = Image.open(path)
    new_size = (800, 500)
    resized_image = image.resize(new_size)
    new_image = Image.new("RGB", resized_image.size, (255, 255, 255))
    new_image.paste(resized_image, mask=resized_image.split()[3])
    image_array = np.array(new_image)
    row_sums = np.sum(image_array, axis=-1)
    mask = row_sums != 765
    test_2d = mask.astype(int)
    len_arr = test_2d[np.any(test_2d != 0, axis=1)]
    Wid_arr = len_arr[:, np.any(len_arr != 0, axis=0)] 
    return Wid_arr
Wid_arr = Create_Irreguar('E:\Learning\Space_Optimizer\Input_images\Admin_5_1_2024.png')
plot(Wid_arr)