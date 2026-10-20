

def count_by(items:list, key:str) -> dict:
    values = {}
    item_values = []
    # the input should never be completly empty, because this function is to count, if the input is empty, there is something wrong and we should raise an Error
    if not items:
        raise ValueError("empty input")
    # wenn kein key übergeben wird, value error, weil immer ein key benötigt wird
    if key == None:
        raise ValueError("empty key")
    
    # alle values aus items in liste legen
    # wenn ein dict den key nicht hat, liegt ein fehler vor und das program wirft key error
    for item in items:
        item_values.append(item[key])
    # jedes item in items in der liste zählen und in dict legen. Nur exact match zählt
        values[item[key]] = item_values.count(item[key])
    return values

        
                
if __name__ == "__main__":
    print(count_by([{"typ": "a"}, {"typ": "b"}, {"typ": "a"}],"typ"))


