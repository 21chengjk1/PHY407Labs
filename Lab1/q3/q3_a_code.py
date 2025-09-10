"""
This is the code for part a, where i try to write histogram function
"""
import numpy as np
import matplotlib.pyplot as plt
import time


def search_bins(input, edges):
    length = len(edges)
    
    min = 0
    max = length - 1

    if input < edges[min]:
        print("????")
        return
    if input > edges[max]:
        print("what...")
        return
    
    while min < max - 1:  # if they are next to each other, stop.
        mid = (min + max) // 2
        if input < edges[mid]:
            max = mid
        else:
            min = mid

    return min  # index

def my_histogram(list, M, range):
    
    bin_size = (range[1] - range[0]) / M

    bin_edges = [range[0]]
    bin = range[0]

    while bin < range[1] - 1e-12:
        bin = bin + bin_size
        bin_edges.append(bin)

    hist = [0] * M
    for i in list:
        x = search_bins(i, bin_edges)
        hist[x] += 1

    return hist, bin_edges


def main():
    np.random.seed(101)
    print("Hi Welcome to my histogram function")
    
    N_list = [10, 100, 1000, 10000, 100000, 1000000]
    my_time = []
    np_time = []
    for n in N_list:
        N = n
        random_list = np.random.randn(N)

        start_time = time.time()
        
        my_hist, my_bin_edges = my_histogram(list=random_list, M=1000, range=(-5, 5))
        end_time = time.time()
        elapsed_time = end_time - start_time
        my_time.append(elapsed_time)


        start_time = time.time()

        hist, bin_edges = np.histogram(random_list, bins=1000, range=(-5, 5))

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        np_time.append(elapsed_time)

        my_hist = np.array(my_hist)
        my_bin_edges = np.array(my_bin_edges)
        hist = np.array(hist)
        
        # print(my_hist)
        # print(hist)

        # print(hist == my_hist)
        if np.any(hist != my_hist):
            print("PROBLEM.")

        # # plot my version
        # plt.subplot(1,2,1)
        # plt.bar(bin_edges[:-1], my_hist, width=np.diff(my_bin_edges), align="edge", alpha=0.5, label="my_hist")
        # plt.title("my_histogram")

        # # plot numpy version
        # plt.subplot(1,2,2)
        # plt.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align="edge", alpha=0.3, label="np.histogram")
        # plt.title("np.histogram")

        # plt.tight_layout()
        # plt.show()
    plt.plot(N_list, my_time, marker='o', label="my_histogram")
    plt.plot(N_list, np_time, marker='s', label="np.histogram")
    plt.xscale("log")   # N grows by powers of 10
    plt.yscale("log")   # runtime spans large range
    plt.xlabel("Sample size N (log scale)")
    plt.ylabel("Execution time (seconds, log scale)")
    plt.title("Runtime Comparison: my_histogram vs np.histogram")
    plt.legend()
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.show()


if __name__ == "__main__":
    main()