def clear_stocks(stock_code):
    """
    
    Takes in a stock code and returns the code without the alphabetic suffix (if it existed) or if the stock code is only alphabetic, it returns the stock code as is.
    
    Examples:
    1. Input: "123"    Output: "123"
    2. Input: "345C"   Output: "345"
    3. Input: "Hello"  Output: "Hello"
    
    Made specifically for:
    df['StockCode'].apply(clear_stocks) 
    
    """
    if stock_code.isdigit():
        return stock_code
    elif stock_code[:-1].isdigit():
        return stock_code[:-1]
    else:
        return stock_code