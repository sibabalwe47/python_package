def top_n(items, n):
    """
    Returns the top n items in an array, in desc order

    Args: 
        array: top n items, in desc order

    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,3]
    """
    for i in range(n):
        for j in range(len(items)-1-i):

            if(items[j] > items[j+i]):
                items[j], items[j+i] = items[j+i], items[j]
    top_n = items[-n:]

    return top_n[::-1]
