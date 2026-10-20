

#Schreib count_by(items, key): Sie zählt, wie oft jeder Wert eines Keys 
#in einer Liste von Dicts vorkommt, und gibt ein Dict zurück. Beispiel: 
#[{"typ": "a"}, {"typ": "b"}, {"typ": "a"}] ergibt {"a": 2, "b": 1}.

def count_by(items, key):
    values = {}
    if not items:
        raise ValueError("empty input")

    # alle values aus items in liste legen
    item_values = items.values()
    # jedes item in items in der liste zählen und in dict legen. Nur exact match zählt
    for item in items:
        values[item[key]] = item_values.count(item[key])

    return values

        
                

print(count_by([{"typ": "a"}, {"typ": "b"}, {"typ": "a"}],"typ"))


