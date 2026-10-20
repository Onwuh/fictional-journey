

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

        
                
if __name__ == "__main__":
    print(count_by([{"typ": "a"}, {"typ": "b"}, {"typ": "a"}],"typ"))


