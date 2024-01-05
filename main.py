import csv
with open("D:\\vadik\\travel app\\Clean_Dataset.csv") as f:
    reader = csv.DictReader(f)
    #data = list(reader)
    search_values=["Delhi","Mumbai","Economy"]
    sum=0
    c=0
    for row in reader:

        if row['source_city'] == search_values[0] and row['destination_city'] == search_values[1] and row['class']== search_values[2]:
            sum+=int(row['price'])
            c+=1
    print(sum/c)