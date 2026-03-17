def remove_bookkeeping_stockcodes(df):
    """
    Remove rows where the StockCode begins with a letter.
    These usually correspond to bookkeeping or system entries.
    """
    mask = df['StockCode'].str[0].str.isalpha()
    clean_df = df[~mask]
    return clean_df



def remove_bookkeeping_rows(df):
    """
    A data cleaning function which removes rows that contain bookkeeping entries, such rows would fulfill the following pattern:
    - The quantity is negative
    - The transaction was not cancelled
    - The customer id is missing
    - The description is not missing
    """
    negative_quantity = df['Quantity'] < 0
    notcancelled_transactions = ~df['InvoiceNo'].str.startswith('C')
    missing_customerid = df['CustomerID'].isna()
    present_description = df['Description'].notna()
    
    mask = negative_quantity & notcancelled_transactions & missing_customerid & present_description
    clean_df = df[~mask]
    return clean_df



def remove_zero_price_rows(df):
    """
    Removes rows with a unit price of zero.
    """
    clean_df = df[df['UnitPrice'] != 0]
    return clean_df