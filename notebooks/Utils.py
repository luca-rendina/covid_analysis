def fromWeekToDate(week, weekFormat="%Y-%W-%w", dateFormat="%Y-%m-%d"):
    """Given a date returns a date
    Parameters
    ----------
     week : str
        The file location of the spreadsheet
    weekFormat : str
        Format of the input string (optional)  
    dateFormat : str
        Format of the return string (optional)

    Returns
    -------
    list
        a list of 2 elements of type string representing the range of the week
    """
    r = datetime.datetime.strptime(week+"-1", weekFormat)
    return [r.strftime(dateFormat), (r + datetime.timedelta(days=6)).strftime(dateFormat)]



def replace(df, col, key, val):
    m = [v == key for v in df[col]]
    df.loc[m, col] = val