
# Example & Usage
## Example Code 1

copy following code to file: aa.py

    import time
    from pnp_timeit.pnp_timeit import Pnp_Timeit

    @Pnp_Timeit.timeit
    def myfunc(arg1, arg2, arg3='hello'):
        time.sleep(3)

    if __name__ == "__main__":
        Pnp_Timeit.enable()
        myfunc("a1", "a2", arg3="hello world")


execute file: aa.py

    $ python aa.py

    {"func": "myfunc", "args": ["a1", "a2"], "kwargs": {"arg3": "hello world"}, "time_cost_seconds": 3.002114}



## Example Code 2

copy following code to file: bb.py

    import time
    import logging
    from pnp_timeit.pnp_timeit import Pnp_Timeit

    @Pnp_Timeit.timeit
    def myfunc(arg1, arg2, arg3='hello'):
        time.sleep(3)

    if __name__ == "__main__":

        logger = logging.getLogger("MYTEST_LOGGER")
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.setLevel(logging.INFO)

        Pnp_Timeit.enable(logger)
        myfunc("a1", "a2", arg3="hello world")






execute file: bb.py

    $ python bb.py

    2020-06-08 16:39:54,151 - MYTEST_LOGGER - INFO - {"func": "myfunc", "args": ["a1", "a2"], "kwargs": {"arg3": "hello world"}, "time_cost_seconds": 3.01584}
