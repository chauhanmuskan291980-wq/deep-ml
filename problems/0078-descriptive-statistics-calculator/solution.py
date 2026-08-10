import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    n=len(data)
    mean = sum(i for i in data)/n 
    median = (data[n//2-1] + data[n//2])/2 if n%2==0 else data[n//2]

    frequency = {}
    for i in data:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] = frequency[i] +1 
    
    maximumFrq = max(frequency.values())

    mode = [key for key , value in frequency.items() if value == maximumFrq]

    mode = min(mode)


    variance = [i-mean for i in data]
    variance = [i*i for i in variance]
    variance = sum(variance)/n

    standardDeviation = (variance)**0.5

    q1,q2,q3 = np.percentile(data,[25,50,75])

    IQR = abs(q3-q1)


    output = {
        'mean':mean,
        'median':median,
        'mode':mode,
        'variance':variance,
        'standard_deviation':standardDeviation,
        '25th_percentile':q1,
        '50th_percentile':q2,
        '75th_percentile':q3,
        'interquartile_range':IQR
    }

    return output

 

















