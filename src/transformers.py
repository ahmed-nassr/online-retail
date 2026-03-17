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



def cancelled_column_creation(InvoiceNo):
    """
    Returns a boolean series that flags cancelled invoice numbers which start with the letter 'C'.
    """
    Cancelled = InvoiceNo.str.startswith('C')
    return Cancelled



def normalize_invoice_numbers(InvoiceNo):
    """
    Remove the 'C' prefix from cancelled invoice numbers.
    """
    normalized_InvoiceNo = InvoiceNo.str.replace('C', '')
    return normalized_InvoiceNo



def standardize_descriptions(df):
    """
    Standardize product descriptions by replacing each with the most frequent description associated with each stockcode.
    """
    canonical_descriptions = (
        df.groupby('StockCode')['Description']
            .agg(lambda x: x.value_counts().idxmax())
    )
    standardized_descriptions = df['StockCode'].map(canonical_descriptions)
    df['Description'] = standardized_descriptions
    return df
    