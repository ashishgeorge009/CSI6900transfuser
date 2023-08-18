import csv
import random

def create_test(no_of_test, repetition,csv_file_path):
    data = []
    for i in range(no_of_test):  # Change this value to generate more or fewer rows
        id = i
        non_ego_model = random.randint(1, 25)
        ego_model = random.randint(1, 25)
        cloudiness = random.randint(0, 100)
        precipitation = random.randint(0, 100)
        fog_density = random.randint(0, 100)
        front = random.randint(0,5)
        back = random.randint(0,5)
        across = random.randint(0,5)
        for i in range(repetition):
            data.append({'id': id,'non_ego_model' : non_ego_model ,'ego_model': ego_model,'cloudiness' : cloudiness,'precipitation':precipitation,'fog_density' :fog_density,'front': front,'back': back,'across':across})

    # Define the CSV file name
    csv_file = csv_file_path

    # Write the data to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        print(file)
        fieldnames = ['id','non_ego_model','ego_model','cloudiness','precipitation','fog_density','front','back','across']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

create_test(100, 10,'/home/ashish/Documents/Project/transfuser/leaderboard/data/longest6/sample_test.csv')