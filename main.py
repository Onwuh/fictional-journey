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
    to_count_list2 = []
    list_of_rows = []
    with open("data/Stellenscreening.csv","r",newline='') as csvfile:
        jobs_file = csv.DictReader(csvfile,delimiter=',')
        for row in jobs_file:
            # add complete file to the list, does not matter since count_by will only look at the key word
            to_count_list.append(row)
            # for the second part I cannot simply use the full csv in dicts because the key word is hidden inside of a string. I need to seperate the string 
            # into indivdual words for the exact match. I need to split it into dicts e.g. {key:Python} {key:is} {key:great}etc and then extract the python key 
            # from the output and print that

            #split the rows into individual lists 
            list_of_rows.append(row["Weitere Voraussetzungen"].split())
        # create a list single list out of the lists per row
        list_of_values = [x for lst in list_of_rows for x in lst]
        # iterate through the values then strip ");:(" to remove sonderzeichen
        #  and lower them while adding them to a key: value pair to work around the key error if the key is missing in a key:value
        for x in list_of_values:
            to_count_list2.append({"key":x.lower().strip(");:(")})
    # get the counted values
    counted_list = count_by(to_count_list2,"key")
    # and only return the pythons
    print(count_by(to_count_list,"Bereich"),{"Python":counted_list["python"]})   


