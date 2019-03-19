def merge_sort(items):

   """
   returns: list array of items sorted in ascending order

   """

   if len(items) > 1:
       left, right = map(lambda l: list(reversed(merge_sort(l))), (items[::2], items[1::2]))
       items.clear()
       while left and right:
           items.append(left.pop() if left[-1] < right[-1] else right.pop())
       items.extend(left[::-1])
       items.extend(right[::-1])
   return items


'''Return an array with sorted ascending order'''

   def bubble_sort(items):
    z =[]
    while len(items) > 0:
        for i in items:

            if i == min(items):
                z.append(min(items))
                items.remove(min(items))
    return z


'''Return a list in sorted ascending order'''
def quick_sort(items):

    less = []
    equal = []
    greater = []

    if len(items) > 1:

        pivot = items[0]

        for x in items:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)


        return quick_sort(less)+equal+quick_sort(greater)

    else:
        return items
