def check_sort(lst: list):
    if not lst or len(lst) <= 1:
        return False
    
    if lst == sorted(lst) or lst == sorted(lst, reverse=True):
        return True
    
    else:
        return False
