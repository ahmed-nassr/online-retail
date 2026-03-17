def proportion(part, total):
    """

    Calculates the proportion of two containers.
    
    """
    proportion = (len(part) / len(total)) * 100
    rounded_proportion = round(proportion, 2)
    return str(rounded_proportion) + '%'