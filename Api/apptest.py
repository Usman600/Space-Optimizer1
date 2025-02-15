import matplotlib
matplotlib.use('Agg')
from flask import Flask, request, jsonify
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import random
import itertools
import os
import time
import asyncio

app = Flask(__name__)

def create_Rectangle(length,width,place):
    rectangle = [[place for j in range(length)] for i in range(width)]
    return rectangle

def create_Triangle(width,place):
    triangle = []
    for i in range(width):
        triangle.append([])
        triangle[-1] = [0 for j in range(width - i - 1)]
        triangle[-1] += [place for j in range(2 * i + 1)]
        triangle[-1] += [0 for j in range(width - i - 1)]
    return triangle

def create_Parallelogram(length,width,place): 
    parallelogram = []
    for i in range(width):
        parallelogram.append([])
        parallelogram[-1] = [0 for i in range(width - i -1)]
        parallelogram[-1] += [place for i in range(length)]
        parallelogram[-1] += [0 for i in range(i)]
    return parallelogram

def create_Rhombus(length, place):
    triangle1 = create_Triangle(length, place)
    triangle2 = triangle1[::-1]
    return triangle1 + triangle2[1:]

def create_Hexagon(length, place):
    triangle1 = create_Triangle(length, place)
    triangle2 = triangle1[::-1]
    rectangle = [[place for i in range(i + 2 * length - (i*2) - 1 + i)] for i in range(length -2)]
    return triangle1 + rectangle + triangle2

def resize_2d_array(arr, container):
    # Create a new 2D array with the desired size
    if len(arr) <= len(container) and len(arr[0]) <= len(container[0]):
        new_rows, new_columns = len(container), len(container[0])
        new_arr = [[0] * new_columns for _ in range(new_rows)]

        # Copy elements from the old array to the new array
        for i in range(min(len(arr), new_rows)):
            for j in range(min(len(arr[0]), new_columns)):
                new_arr[i][j] = arr[i][j]
        return new_arr
    return 0

def Outcomes(j, k, row, container):
    objects = []
    selected = []
    if row['Shape_Type'] == "Rectangle":
        rectangle = create_Rectangle(row['ShapeLength'], row['ShapeWidth'], len(j) + 1)
        temp = resize_2d_array(rectangle, container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
        temp = resize_2d_array(list(map(list, zip(*rectangle))), container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
    if row['Shape_Type'] == "Square":
        square = create_Rectangle(row['ShapeLength'], row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(square, container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
    if row['Shape_Type'] == "Triangle":
        triangle = create_Triangle(row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(triangle, container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
            objects.append(j +[resize_2d_array(triangle[::-1], container)])
            selected.append(k + [row['ShapeName']])
        temp = resize_2d_array(list(map(list, zip(*triangle))), container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
        temp = resize_2d_array(list(map(list, zip(*triangle[::-1]))), container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
    if row['Shape_Type'] == "Parallelogram":
        parallelogram = create_Parallelogram(row['ShapeLength'], row['ShapeWidth'], len(j) + 1)
        temp = resize_2d_array(parallelogram, container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
        temp = resize_2d_array(list(map(list, zip(*parallelogram))), container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
    if row['Shape_Type'] == "Rhombus":
        rhombus = create_Parallelogram(row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(rhombus, container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
    if row['Shape_Type'] == "Hexagon":
        hexagon = create_Hexagon(row['ShapeLength'], len(j) + 1)
        temp = resize_2d_array(hexagon, container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
        temp = resize_2d_array(list(map(list, zip(*hexagon))), container)
        if temp != 0:
            objects.append(j + [temp])
            selected.append(k + [row['ShapeName']])
    return objects, selected

def rotate_matrix_right(matrix):
    if all(row[-1] == 0 for row in matrix):
        rotated_matrix = [row[-1:] + row[:-1] for row in matrix]
        return rotated_matrix
    return 1

def shift_matrix_down(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check if the last column contains only zeros
    if all(row == 0 for row in matrix[-1]):
        # If yes, then rotate the matrix up
        shifted_matrix = [[0] * num_cols for _ in range(num_rows)]
        for col in range(num_cols):
            for row in range(num_rows):
                shifted_row = (row - 1) % num_rows
                shifted_matrix[row][col] = matrix[shifted_row][col]
        return shifted_matrix
    else:
        # If no, return 1
        return 1

def add_arrays_with_rotation(arr1, arr2):
    local_array = arr1
    result = [[0 for j in i] for i in arr1]
    i = 0
    while i < len(arr1):
        checker = 0
        for j in range(len(arr1[0])):
            if (arr1[i][j] == 0 and arr2[i][j] == 0) or (arr1[i][j] != 0 and arr2[i][j] == 0) or (arr1[i][j] == 0 and arr2[i][j] != 0):
                result[i][j] = arr1[i][j] + arr2[i][j]
            else:
                checker = 1
                break
        if checker == 1:
            temp = rotate_matrix_right(arr1)
            if temp != 1:
                arr1 = temp
            else:
                arr1 = local_array
                temp = shift_matrix_down(arr1)
                if temp != 1:
                    arr1 = temp
                    local_array = arr1
                else:
                    return arr2
            result = [[0 for j in i] for i in arr1]
            i = 0
        else:
            i += 1
    return result

def convert_to_3d_array(input_array):
    unique_values = np.unique(input_array)
    num_channels = len(unique_values)
    height, width = input_array.shape

    # Create a 3D array filled with zeros
    image_3d_array = np.zeros((height, width, 3), dtype=np.uint8)

    # Assign unique colors to each channel using a colormap
    colormap = plt.cm.get_cmap("tab10", num_channels)  # Use 'tab10' colormap with num_channels

    # Ensure that 0 is always in white color
    zero_color = np.array([255, 255, 255], dtype=np.uint8)
    image_3d_array += (input_array == 0).reshape((height, width, 1)) * zero_color

    for d, value in enumerate(unique_values):
        if value == 0:
            continue  # Skip 0, already handled
        color = np.array(colormap(d)[:3]) * 255  # Extract RGB values and scale to 0-255
        mask = (input_array == value).reshape((height, width, 1))
        image_3d_array = (image_3d_array.astype(np.float64) + mask.astype(np.float64) * color).astype(np.uint8)

    return image_3d_array

async def Main(container_Dim, dataset, userID):
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
            else:
                objects_temp = objects
                selected_temp = selected

    wasted_area = sum(row.count(0) for row in container)
    result_array = []
    if len(objects) > 10:
        selected_index = [random.randint(0, len(objects)-1) for _ in range(random.randint(10, min(50,len(objects))))]
        objects = [objects[i] for i in selected_index]
        selected = [selected[i] for i in selected_index]
    for j in range(len(objects)):
        temp = container
        selected_temp_new = []
        for i in range(len(objects[j])):
            temp1 = add_arrays_with_rotation(objects[j][i], temp)
            if temp1 != temp:
                selected_temp_new.append(selected[j][i])
            temp = temp1
        if sum(row.count(0) for row in temp) < wasted_area:
            result_array = temp
            wasted_area = sum(row.count(0) for row in result_array)
            selected_shapes = selected_temp_new

    test = np.unique(result_array[result_array != 0])
    for value in test:
        if value == 0:
            continue
        color_index = np.where(np.unique(result_array) == value)[0][0]
        color = plt.cm.get_cmap("tab10", len(test))(color_index)
    
    image_3d_array = convert_to_3d_array(np.array(result_array))

    plt.imshow(image_3d_array)
    filename = f'\\Output_images\\{userID}_image_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png'
    try:
        plt.savefig(f"{os.getcwd()}{filename}")
        filename = filename.replace("\\", "/")
    except Exception as e:
        print(e)
    plt.close()
    await asyncio.sleep(1)

    return filename, wasted_area, selected_shapes

@app.route('/optimize', methods=['POST'])
async def optimize():
    try:
        # Get the parameters from the request
        data = request.json
        dataList = data.get('dataList')
        shapeArray = data.get('shapeArray')
        userId = data.get('userID')
        # Convert dataList and shapeArray to appropriate formats if needed

        # Call the Main function asynchronously
        loop = asyncio.get_event_loop()
        result = await loop.create_task(Main(shapeArray, dataList, str(userId)))

        # Return the output
        response = {
            'filename': result[0],
            'wasted_area': result[1],
            'selected_shapes': ", ".join(result[2])
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)