

#Schreib count_by(items, key): Sie zählt, wie oft jeder Wert eines Keys 
#in einer Liste von Dicts vorkommt, und gibt ein Dict zurück. Beispiel: 
#[{"typ": "a"}, {"typ": "b"}, {"typ": "a"}] ergibt {"a": 2, "b": 1}.

def count_by(items, key):
    values = {}
    item_values = []
    if not items:
        raise ValueError("empty input")
    # wenn kein key übergeben wird, value error, weil immer ein key benötigt wird
    if not key:
        raise ValueError("empty key")
    
    # alle values aus items in liste legen
    # wenn ein dict den key nicht hat, liegt ein fehler vor und das program wirft key error
    for item in items:
        item_values.append(item[key])
    # jedes item in items in der liste zählen und in dict legen. Nur exact match zählt
    for item in items:
        values[item[key]] = item_values.count(item[key])

    return values

        
                
if __name__ == "__main__":
    print(count_by([{"typ": "a"}, {"typ": "b"}, {"typ": "a"}],"typ"))


