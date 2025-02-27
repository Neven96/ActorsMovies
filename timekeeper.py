import time

def timekeeper(out_print, function):
    '''
    For measuring the time a function takes to run
    Uses lambda for passing the function on

    Parameters
    -----------
    out_print : str
        The string which should be printed out
    function : func
        The function to be ran

    Returns
    -----------
    output : unknown
        This just returns whatever the main function returns
    '''

    start_time = time.perf_counter_ns()

    output = function()

    time_used = time.perf_counter_ns() - start_time

    time_symbol = 'ns'

    if time_used > 1000000000:
        time_used = time_used/1000000000.0
        time_symbol = 's'
    elif time_used > 1000000:
        time_used = time_used/1000000.0
        time_symbol = 'ms'

    print(f'{out_print} time: {time_used:.4f} {time_symbol}')

    return output
