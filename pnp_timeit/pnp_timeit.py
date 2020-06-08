
import os
import json
import functools
import logging
from datetime import datetime

class Pnp_Timeit:
    """
    Provide code level time cost measurement.

    Pnp_Timeit can be swtiched ON or OFF, default is OFF.
    """
    
    ENABLE_TIMEIT=False
    LOGGER_NAME="pnp.library"

    @classmethod
    def timeit(cls, func):
        @functools.wraps(func)
        def wrapper_timeit_func(*args, **kwargs):
            if cls.is_enable():
                time_begin = datetime.utcnow()

                response = func(*args, **kwargs)

                time_end = datetime.utcnow()
                time_diff_seconds = (time_end - time_begin).total_seconds()
                logger = logging.getLogger(cls.LOGGER_NAME)

                dict_time_info = {"func": func.__name__, "args":args, "kwargs":kwargs, "time_cost_seconds":time_diff_seconds}
                logger.debug("{}".format(json.dumps(dict_time_info, default=cls.__default_converter)))

                return response
            else:
                return func(*args, **kwargs)
            
        return wrapper_timeit_func


    @classmethod
    def enable(cls):
        """
        Process scope enable, default is OFF 
        """
        Pnp_Timeit.ENABLE_TIMEIT = True


    @classmethod
    def disable(cls):
        """
        Session level disable, default is DISABLE
        """
        Pnp_Timeit.ENABLE_TIMEIT = False
        
    @classmethod
    def is_enable(cls) -> bool:
        """
        Check whether timeit is enabled

        Return: 
            True: enabled
            False: disabled
        """
        return Pnp_Timeit.ENABLE_TIMEIT



    @classmethod
    def __default_converter(cls, pi_obj):
        """
        Convert datatime type to string
        """
        if isinstance(pi_obj, datetime):
            return pi_obj.__str__()
