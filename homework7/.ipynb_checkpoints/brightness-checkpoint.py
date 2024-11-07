# File name: brightness.py

def avg_brightness(table):
    """
    Calculates the average brightness of the entire "image"/table

    Input: table (numpy.ndarray): 2D array of the brightness of each pixel

    Output: avg_brightness (float): the average brightness of all the pixels in the image
    """
    flattened_arr = table.reshape(-1) # numpy function
    total = sum(flattened_arr)
    avg = round(total/len(flattened_arr), 2)
    return avg
    
def find_max_brightness_pixel(table):
    """
    Finds the pixel/value with the maximum brightness 
    
    Input: table (numpy.ndarray): 2D array of the brightness of each pixel

    Outputs: 
    max_brightness (float): the value of the maximum brightness
    location (list): list with 2 elements that indicate the pixel with the maximum brightness.
    """
    max_brightness = table[0][0]
    location = []
    for row in range(len(table)):
        for col in range(len(table[row])):
            if(table[row][col] > max_brightness):
                max_brightness = table[row][col]
                location = [row,col]
    return max_brightness, location

def row_brightness(table):
    """
    Calculates the average brightness for each row in the table

    Input: table (numpy.ndarray): 2D array of the brightness of each pixel

    Output: row_brightnesses (list): list with the sum of the brightness of each of the pixels in each row
    """
    row_brightnesses = []
    brightness = 0
    for row in range(len(table)):
        for col in range(len(table[row])):
            brightness += table[row][col]
        row_brightnesses.append(round(brightness,2))
        brightness = 0
    return row_brightnesses
def scale_brightness(table, factor):
    """
    Scales each value in the table by a certain factor. If the factor causes the average brightness to go greater than 70, then the phrase
    "too bright" will be printed. If the factor causes the average brightness to go below 30, then the phrase "too dim" will be printed. 
    Otherwise, we will print out "the factor is okay" (this is definitely not to meet the if, elif, and else requirement lol). The table
    will still be printed.

    Input: 
    table (numpy.ndarray): 2D array of the brightness of each pixel
    factor (float): factor that each brightness will be multiplied by 

    Output: table (numpy.ndarray): 2D array with the scaled brightness of the image
    """
    arr = np.array([])
    for row in range(len(table)):
        for col in range(len(table[row])):
            table[row][col] *= factor
    avg_bright = avg_brightness(table)
    if (avg_bright > 70):
        print("Too bright")
    elif (avg_bright < 30):
        print("Too dim")
    else:
        print("Factor is acceptable")
    return table