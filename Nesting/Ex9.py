def process_data(data):
    results = []
    for datum in data:
        if datum % 2 == 0:
            if datum > 0:
                if datum < 100:
                    results.append(datum * 2)
                else:
                    results.append(datum * 3)
            else:
                results.append(datum)
        else:
            results.append(datum)
    return results
