def write_data(file_name, data):
    with open(file_name, 'w') as file:
        for key, value in data.items():
            file.write(f'{key}: {value}\n')

def read_data(file_name):
    data = {}
    with open(file_name, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            data[key] = value
    return data

def clear_file(file_name):
    with open(file_name, 'w') as file:
        pass

# Write data to the first file
data1 = {'name': 'Ahmet', 'age': '25', 'city': 'Ankara'}
write_data('first_file.txt', data1)

# Read data from the first file
read1 = read_data('first_file.txt')
print('Data read from the first file:', read1)

# Write data to the second file
data2 = {'name': 'Ayse', 'age': '30', 'city': 'Istanbul'}
write_data('second_file.txt', data2)

# Read data from the second file
read2 = read_data('second_file.txt')
print('Data read from the second file:', read2)

# Clear the content of the first file
clear_file('first_file.txt')
print('Content of the first file has been cleared.')

# Read data from the cleared first file
read_cleared = read_data('first_file.txt')
print('Data read from the cleared first file:', read_cleared)

# This code includes three functions: write_data, read_data, and clear_file. 
# The write_data function writes data to a text file based on the provided file name and data. 
# The read_data function reads data from a specified file and creates a dictionary. 
# The clear_file function clears the content of a specified file.

