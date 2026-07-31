def percent(part, total):
    """

    Calculate `part` as a percentage from `total`.
    
    """
    if total == 0:
        raise ValueError("Total cannot be zero.")
    elif total < 0 or part < 0:
        raise ValueError("Input cannot be negative")
    if part == 0:
        return "0%"
    percentage = (part / total) * 100
    if round(percentage, 2) > 0:
        rounded_percentage = round(percentage, 2)
        return str(rounded_percentage) + '%'
    else:
        new_percentage = format(percentage, '.0e')
        return new_percentage + '%'