import csv

'''
Read csv file and convert to list
'''
def csv_to_list(file_path, delimiter=','):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        data = list(reader)
        return data

'''
Read csv file and convert to dictionary (first line as keys)
'''
def csv_to_dict(file_path, delimiter=','):
    with open(file_path) as csvfile:
        data = csv.DictReader(csvfile)
        
        for row in data:
            print(row.items())

'''
Write a list to a csv file
'''
def list_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)

'''
Write a dictionary to a csv file
'''
def dict_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
