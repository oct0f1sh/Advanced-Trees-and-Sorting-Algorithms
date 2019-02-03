#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    if len(items) <= 1:
        return True

    last_num = items[0]

    for item in items[1:]:
        if not last_num <= item:
            return False
        else:
            last_num = item

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    while not is_sorted(items):
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                # swap 'em
                items[i], items[i + 1] = items[i + 1], items[i]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    if len(items) <= 1:
        return

    minimum = items[0]
    minimum_index = 0

    print(items, ' start')

    for swaps in range(len(items)):
        for i, item in enumerate(items[swaps:]):
            if item <= minimum:
                minimum = item
                minimum_index = i + swaps
                
        print('swap {} with {}'.format(swaps, minimum_index))
        items[swaps], items[minimum_index] = items[minimum_index], items[swaps]
        print(items, swaps, ' swaps')

    print(items, ' end')
            


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
