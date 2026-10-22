import csv

def count_by(items:list, key:str) -> dict:
    values = {}
    # if no key is given raise value error because a key is always nessesary
    if key is None:
        raise ValueError("empty key")

    # iterate through keys from input
    for item in items:
        # check if key is part of values if not so add to dict
        if item[key] not in values:
            values[item[key]] = 1
        # if it is, add 1 to count 
        else:
            values[item[key]] +=1
    return values

def count_rows_by(rows: list,column:str ,key:str ) -> int:
    key_count:int = 0
    # make sure key is lower and has no trailing spaces
    key = key.strip().lower()

    # check the inputs
    if not key:
        raise ValueError("empty key")
    if column is None:
        raise ValueError("empty column name")

    
    # iterate through rows with column key
    for row in rows:
        if key in row[column].lower():
            
            key_count += 1
    return key_count
# handcheck for Stellenscreening.csv:
# column 1: 5 Security, 4 DevOps, 4 python dev, 1 Backend dev, 3 Application security, 4 Junior Pentester
# column 5: python == 5  

if __name__ == "__main__":
    to_count_list = []
    with open("data/Stellenscreening.csv","r",newline='',encoding="utf-8") as csvfile:
        jobs_file = csv.DictReader(csvfile,delimiter=',')
        for row in jobs_file:
            to_count_list.append(row)


    print(count_by(to_count_list,"Bereich"))   
    print(count_rows_by(to_count_list,"Weitere Voraussetzungen","Python"))


