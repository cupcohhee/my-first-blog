def quicksort(li, first, last):
    if first < last:
        pivotid = QS(li, first, last)
        print(pivotid)
        print(li)

        quicksort(li, first, pivotid-1)
        quicksort(li, pivotid + 1, last)

def suu(list):
    y = 0
    for i in range(1,len(list)):
        y += i
    return y

def QS(li, first, last):
    pivot = first
    left = first + 1
    right = last
    done = True

    while done:
        while left <= right and li[left] <= li[pivot]:
            left += 1

        while left <= right and li[right] >= li[pivot]:
            right -= 1

        if left > right:
            done = False
        else:
            li[left], li[right] = li[right], li[left]

    li[pivot], li[right] = li[right], li[pivot]

    return right


if __name__ == "__main__":
    l = [3, 7, 5, 9, 2]
    m = [0]*6
    # quicksort(l,0,len(l)-1)
    print(suu(m))
