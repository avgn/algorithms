#!/usr/bin/python

# Implementation of the insertion sort algorithm as described in CLRS p.18

def insertion_sort(arr):
        n = len(arr)
        for j in range(1, n):
            key = arr[j]
            # insert arr[j] into the sorted sequence arr[0:j-1]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i+1] = arr[i]
                i -= 1
            arr[i+1] = key


def main():
    pass


if __name__ == "__main__":
    main()