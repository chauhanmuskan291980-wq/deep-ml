def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    frequancy = {}
    output = []
    for i in samples:
        if i not in frequancy:
            frequancy[i] = 1
        else:
            frequancy[i] = frequancy[i]+1
    
    for key , value in frequancy.items():
        output.append((key,value/len(samples)))
    
    return output