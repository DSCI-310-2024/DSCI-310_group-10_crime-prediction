
def get_time_period(hour, minute):
    """
    get the correct time period for the incident time

    generate the time period ('Late Night', 'Morning', 'Afternoon', 'Evening', 'Night') 
    indicating the proper time period of the incident

    Parameters:
    -----------
    hour: int
        The input hour of the incident from the hour column of the dataframe

    minute: int
        The input minute of the incident from the minute column of the dataframe 

    Returns:
    --------
    String
        A string indicate the correct time period using the given hour and minute.
        ('Late Night', 'Morning', 'Afternoon', 'Evening', 'Night')
        
    Examples:
    ---------
    >>> time_period = get_time_period(3, 12) # replace (3, 12) with the actural hour and miniute
    >>> print(time_period)

    Notes:
    ------
    This function does not need extra library. It will provide the indication of the time period from the given data.

    """
