def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        for j in range(size-1):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp

    return elements

if __name__ == "__main__":
    elements = [5, 9, 2, 67, 9, 2]
    elements_sorted = bubble_sort(elements)
    print(elements_sorted)