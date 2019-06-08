tic
========

current_time
--------
::


def current_time():
    """ Provide current time as YYYY-MM-DD_HH-MM-SS

    """

time_to_str
--------
::

def time_to_str(delta_t, mode="min"):
    """Convert elapsed time to string representation

    Parameters
    --------
    delta_t: time difference
        Elapsed time
    mode: str
        Time representation manner, by "minitues" or "seconds".

    Returns
    --------
    delta_str: str
        Elapsed time string representation

    Examples
    --------
    >>> from timeit import default_timer as timer
    >>> start = timer()
    >>> end = timer()
    >>> elapsed_time_str = time_to_str(end - start, "min")

    """
