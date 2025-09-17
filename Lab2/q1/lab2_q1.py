"""
Question 1
"""
import numpy as np

PART_D_WORKAROUND = True

def std_1(array):
    """
    Implements equation 1 to calculate std
    """
    n = len(array)
    array_sum = 0
    for i in range(n):
        array_sum += array[i]
    
    mean = array_sum / n
    sum = 0
    for i in range(n):
        sum += (array[i] - mean) ** 2
    
    return np.sqrt(sum / (n-1))

def std_2(array):
    """
    Implements equation 2 to calculate std
    """
    sum = 0
    array_sum = 0
    n = len(array)

    for i in range(n):
        array_sum += array[i]
        sum += (array[i]) ** 2
    
    mean = array_sum / n
    temp = sum - (n * (mean ** 2))

    if temp < 0:
        print("Std2 had to sqrt a number less than 0 !!!!!!!!!!")
    
    return np.sqrt(abs(temp) / (n-1))

def std_2_workaround(array):
    """
    Implements eq 2, the one pass method, with the workaround of shifting closer to the data
    This means that we're computing the std dev using a mean closer to 0, which is better
    """
    sum = 0
    array_sum = 0
    n = len(array)

    center = array[0]  # Shift towards some datapoint.

    for i in range(n):
        array_sum += array[i] - center
        sum += (array[i] - center) ** 2
    
    mean = array_sum / n
    temp = sum - (n * (mean ** 2))

    if temp < 0:
        print("Std2 had to sqrt a number less than 0 !!!!!!!!!!")
    
    return np.sqrt(abs(temp) / (n-1))


def main():
    print("=========START=========")

    np.random.seed(2)

    cdata = np.loadtxt("data/cdata.txt")

    sigma_1 = std_1(cdata)
    sigma_2 = std_2(cdata)

    truth_sigma = np.std(cdata, ddof=1)

    relative_error_1 = abs(sigma_1 - truth_sigma) / truth_sigma 
    relative_error_2 = abs(sigma_2 - truth_sigma) / truth_sigma

    print("Relative error for eq 1 is", relative_error_1)
    print("Relative error for eq 2 is", relative_error_2)

    print("\n")
    mean, sigma, n = (0., 1., 2000)
    random_array = np.random.normal(mean, sigma, n)
    random_sigma_1 = std_1(random_array)
    random_sigma_2 = std_2(random_array)
    random_truth_sigma = np.std(random_array, ddof=1)
    relative_error_1 = abs(random_sigma_1 - truth_sigma) / random_truth_sigma 
    relative_error_2 = abs(random_sigma_2 - truth_sigma) / random_truth_sigma
    print("Relative error for eq 1 with a 0 mean", relative_error_1)
    print("Relative error for eq 2 with a 0 mean", relative_error_2)
    if PART_D_WORKAROUND:
        random_sigma_shift = std_2_workaround(random_array)
        relative_error_shift = abs(random_sigma_shift - truth_sigma) / random_truth_sigma
        print("Relative error for eq 2(shifted) with a 0 mean", relative_error_shift)



    # and another one with
    mean, sigma, n = (1.e7, 1., 2000)
    random_array = np.random.normal(mean, sigma, n)
    random_sigma_1 = std_1(random_array)
    random_sigma_2 = std_2(random_array)
    random_truth_sigma = np.std(random_array, ddof=1)
    relative_error_1 = abs(random_sigma_1 - truth_sigma) / random_truth_sigma 
    relative_error_2 = abs(random_sigma_2 - truth_sigma) / random_truth_sigma
    print("Relative error for eq 1 with a 1.e7 mean", relative_error_1)
    print("Relative error for eq 2 with a 1.e7 mean", relative_error_2)
    if PART_D_WORKAROUND:
        random_sigma_shift = std_2_workaround(random_array)
        relative_error_shift = abs(random_sigma_shift - truth_sigma) / random_truth_sigma
        print("Relative error for eq 2(shifted) with a 1.e7 mean", relative_error_shift)

    print("=========END=========")

if __name__ == "__main__":
    main()