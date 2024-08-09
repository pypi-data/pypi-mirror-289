"""
Quick and dirty utilties for timing code.
"""

import os
import time
import contextlib
from datetime import timedelta

def beg():
    beg_tm = time.perf_counter()
    os.environ['the_logger_time'] =  str(beg_tm)

def end():
    end_tm = time.perf_counter()
    beg_tm = float(os.environ['the_logger_time'])
    sec_delta = end_tm - beg_tm
    sec_delta = round(sec_delta, 3)
    exec_tm = str(timedelta(seconds = sec_delta)).rstrip('0')
    print(f"Elapsed Time: {exec_tm}")
    
@contextlib.contextmanager 
def timer(name=None, times=None, printit=1):
    """
    Context manager that provides timing of code execution.
    
    Parameters
    ----------
    name : str, default is None
        Key used to store the timing in the `times` dict.
    times : dict, default is None
        Used to store timings of code execution.
    printit : int, default is 1
        If not equal 1 then the elasped time is not printed.

    Example
    -------
    >>> import thelogger as tl
    >>> import time 
    ...
    >>> with tl.timer():
    ...     time.sleep(0.1)
    Elapsed Time: 0:00:00.104
    
    >>> times = dict()
    >>> with tl.timer('test', times, 0):
    ...     time.sleep(.01)
    >>> times
    {'test': 0.015}
    """
    beg_tm = time.perf_counter()
    yield 
    end_tm = time.perf_counter()
    sec_delta = end_tm - beg_tm
    sec_delta = round(sec_delta, 3)
    if name:
        times[str(name)] = sec_delta
    if printit == 1:
        exec_tm = str(timedelta(seconds = sec_delta)).rstrip('0')
        print(f"Elapsed Time: {exec_tm}")
    