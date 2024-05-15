import io
import matplotlib
matplotlib.use('Agg')
from flask import Flask, request, jsonify
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
import random
import itertools
from PIL import Image
import os
import time
import asyncio
import aiohttp

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

def create_Rectangle(length,width,place):
    rectangle = np.full((width, length), place)
    return rectangle

def create_Triangle(width,place):
    triangle = create_Rectangle(width*2-1,width,0)
    for i in range(width):
        for j in range((width - i - 1), (width - i - 1)+(2 * i + 1)):
            triangle[i][j] = place
    return triangle

def create_Parallelogram(length,width,place):
    parallelogram = create_Rectangle(length+width-1,width,0)
    for i in range(width):
        for j in range((width - i -1), (width - i -1) + (length)):
            parallelogram[i][j] = place
    return parallelogram

def create_Rhombus(length, place):
    triangle = create_Triangle(length, place)
    return np.concatenate((triangle, np.rot90(triangle[:-1], k=2)), axis=0)

def create_Hexagon(length, place):
    triangle = create_Triangle(length, place)
    rectangle = create_Rectangle(2 * length - 1,length-1,place)
    return np.concatenate((triangle, rectangle, np.rot90(triangle[:-1], k=2)), axis=0)

def resize_2d_array(objects, container):
    if objects.shape[0] <= container.shape[0] and objects.shape[1] <= container.shape[1]:
        container = np.copy(container)
        container[:objects.shape[0], :objects.shape[1]] = objects
        return container
    return None

def rotate_matrix_right(matrix):
    matrix_np = np.array(matrix)
    if np.all(matrix_np[:, -1] == 0):
        rotated_matrix_np = np.roll(matrix_np, 1, axis=1)
        return rotated_matrix_np
    return None

def shift_matrix_down(matrix):
    if np.all(matrix[-1] == 0):
        shifted_matrix_np = np.zeros_like(matrix)
        shifted_matrix_np[1:] = matrix[:-1]
        return shifted_matrix_np
    return None

def add_arrays_with_rotation(objects, container):
    local_object = objects
    while True:
        mask = (container == 0) | (objects == 0)
        if np.all(mask):
            break
        temp = rotate_matrix_right(objects)
        if temp is not None:
                objects = temp
        else:
            temp = shift_matrix_down(local_object)
            local_object = temp
            if temp is not None:
                objects = temp
            else:
                return container
    return container + objects

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

def Outcomes(j, k, row, container):
    objects = []
    selected = []

    if row['Shape_Type'] == "Rectangle":
        rectangle = create_Rectangle(row['ShapeLength'], row['ShapeWidth'], len(j) + 1)
        temp = resize_2d_array(rectangle, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

        rectangle_flipped = np.flip(np.transpose(rectangle), axis=0)
        temp = resize_2d_array(rectangle_flipped, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

    elif row['Shape_Type'] == "Square":
        square = create_Rectangle(row['ShapeLength'], row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(square, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

    elif row['Shape_Type'] == "Triangle":
        triangle = create_Triangle(row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(triangle, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

        triangle_flipped = np.flip(np.transpose(triangle), axis=0)
        temp = resize_2d_array(triangle_flipped, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
            objects.append(j + [resize_2d_array(np.transpose(np.flip(triangle, axis=0)), container)])
            selected.append(k + [row['ShapeName']])

    elif row['Shape_Type'] == "Parallelogram":
        parallelogram = create_Parallelogram(row['ShapeLength'], row['ShapeWidth'], len(j) + 1)
        temp = resize_2d_array(parallelogram, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

        parallelogram_flipped = np.flip(np.transpose(parallelogram), axis=0)
        temp = resize_2d_array(parallelogram_flipped, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

    elif row['Shape_Type'] == "Rhombus":
        rhombus = create_Parallelogram(row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(rhombus, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

    elif row['Shape_Type'] == "Hexagon":
        hexagon = create_Hexagon(row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(hexagon, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

        hexagon_flipped = np.flip(np.transpose(hexagon), axis=0)
        temp = resize_2d_array(hexagon_flipped, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
    
    elif row['Shape_Type'] == "Other":
        irreguar = Create_Irreguar(row['ImageData'])
        temp = resize_2d_array(irreguar, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])

        irreguar_flipped = np.flip(np.transpose(irreguar), axis=0)
        temp = resize_2d_array(irreguar_flipped, container)
        if temp is not None:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
            objects.append(j + [resize_2d_array(np.transpose(np.flip(irreguar, axis=0)), container)])
            selected.append(k + [row['ShapeName']])
    return objects, selected

def Main(container_Dim, dataset, userID):
    container = create_Rectangle(container_Dim[0], container_Dim[1], 0)
    objects = [[]]
    selected = [[]]
    for row in dataset:
        for i in range(row['Quantity']):
            objects_temp = []
            selected_temp = []
            for j, k in zip(objects, selected):
                temp = Outcomes(j, k, row, container)
                objects_temp.extend(temp[0])
                selected_temp.extend(temp[1])
            if len(objects_temp) != 0:
                objects = objects_temp
                selected = selected_temp
    wasted_area = np.count_nonzero(container == 0)
    result_array = []
    if len(objects) > 10:
        selected_index = [random.randint(0, len(objects)-1) for _ in range(random.randint(10, min(50,len(objects))))]
        objects = [objects[i] for i in selected_index]
        selected = [selected[i] for i in selected_index]
    for k, l in zip(objects, selected):
        objects_temp = [] # Initialize objects_temp inside the outer loop
        selected_temp = []  # Initialize selected_temp inside the outer loop

        for ob, sl in zip(itertools.permutations(k), itertools.permutations(l)):
            objects_temp.append(list(ob))
            selected_temp.append(list(sl))

            # Check if the limit is reached
            if len(objects_temp) >= len(k):
                break

        for j in range(len(objects_temp)):
            temp = container
            selected_temp_new = []
            for i in range(len(objects_temp[0])):
                temp1 = add_arrays_with_rotation(objects_temp[j][i], temp)
                if not np.array_equal(temp1, temp):
                    selected_temp_new.append(selected_temp[j][i])
                temp = temp1
            if np.count_nonzero(temp == 0) < wasted_area:
                result_array = temp
                wasted_area = np.count_nonzero(result_array == 0)
                selected_shapes = selected_temp_new
    test = np.unique(result_array[result_array != 0])
    for value in test:
        if value == 0:
            continue
        color_index = np.where(np.unique(result_array) == value)[0][0]
        color = plt.cm.get_cmap("tab10", len(test))(color_index)

    image_3d_array = convert_to_3d_array(np.array(result_array))
    image_bytes = io.BytesIO()
    plt.imshow(image_3d_array)
    filename = f'\\Output_images\\{userID}_image_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png'
    try:
        plt.savefig(image_bytes, format='png', bbox_inches='tight', pad_inches=0)
        #plt.show()
        plt.savefig(f"{os.getcwd()}{filename}")
        filename = filename.replace("\\", "/")
    except Exception as e:
        print(e)
    plt.close()

    # Get the image data as bytes
    image_bytes.seek(0)
    image_data = image_bytes.getvalue()

    return image_data , wasted_area, selected_shapes

result = [
    {'ShapeName': 'Shape4', 'Shape_Type': 'Other', 'ShapeWidth': 0, 'ShapeLength': 0, 'ImageData': 'E:\Learning\Space_Optimizer\Input_images\Admin_5_1_2024.png', 'Quantity': 1},
    {'ShapeName': 'Shape7', 'Shape_Type': 'Hexagon', 'ShapeWidth': 10, 'ShapeLength': 10, 'ImageData': '', 'Quantity': 1},
    #{'ShapeName': 'Shape1', 'Shape_Type': 'Rectangle', 'ShapeWidth': 2, 'ShapeLength': 3, 'Quantity': 1},
    {'ShapeName': 'Shape2', 'Shape_Type': 'Square', 'ShapeWidth': 10, 'ShapeLength': 10, 'ImageData': '', 'Quantity': 5},
    {'ShapeName': 'Shape3', 'Shape_Type': 'Square', 'ShapeWidth': 10, 'ShapeLength': 10, 'ImageData': '', 'Quantity': 8 },
    #{'ShapeName': 'Shape6', 'Shape_Type': 'Parallelogram', 'ShapeWidth': 4, 'ShapeLength': 3, 'Quantity': 1}
    # Add more rows as needed
]
start_time = time.time()
result = Main([100, 100], result, "Admin_5")
end_time = time.time()  # Record end time
elapsed_time = end_time - start_time  # Calculate elapsed time
print(elapsed_time)