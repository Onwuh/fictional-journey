import csv

def count_by(items:list, key:str) -> dict:
    values = {}
    # if no key is given raise value error because a key is always nessesary
    if key == None:
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

        
# handcheck for Stellenscreening.csv:
# column 1: 5 Security, 4 DevOps, 4 python dev, 1 Backend dev, 3 Application security, 4 Junior Pentester
# column 5: python == 5  

if __name__ == "__main__":
    to_count_list = []
    with open("data/Stellenscreening.csv","r",newline='') as csvfile:
        jobs_file = csv.DictReader(csvfile,delimiter=',')
        for row in jobs_file:
            to_count_list.append(row)
            
            #to_count_list.append({"key_word": })
    print(count_by(to_count_list,"Bereich"))   
    #print(to_count_list)        


