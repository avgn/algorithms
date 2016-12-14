#!/usr/bin/python

# Implementation of the merge sort algorithm described in CLRS p.31

import numpy as np

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [ ]
    right = [ ]
    for i in range(1, n1+1):
        left.append(arr[p+i-1])
    for j in range(1, n2+1):
        right.append(arr[q+j])
    left.append(np.inf)
    right.append(np.inf)
    i = 0
    j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) / 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

        

def main():
    pass


if __name__ == "__main__":
    main()