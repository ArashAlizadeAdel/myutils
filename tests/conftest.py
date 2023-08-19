import pytest
import pandas as pd
import numpy as np
import datetime as dt
import time
import random

@pytest.fixture
def data():
    '''Dataframe containing most data types'''
    data = pd.DataFrame({"col1" : [1,2,3],
                         "col2" : ["a","b","c"],
                         "col3" : [dt.datetime.now(),dt.datetime.now(),dt.datetime.now()],
                         "col4" : [dt.datetime.now().date(),dt.datetime.now().date(),dt.datetime.now().date()],
                         "col5" : [1.0,2.0,3.0],
                         "col6" : [np.nan,np.nan,np.nan],
                         "col7" : [None,None,None],
                         })
    return data

@pytest.fixture
def data_big(data):
    '''Dataframe that is bigger than usual dataframes'''
    repeat_count = random.randint(100, 1000)
    concat_list = []
    for i in range(repeat_count):
        concat_list.append(data)
    data = pd.concat(concat_list)
    return data


@pytest.fixture
def data_empty_with_cols(data):
    '''Empty dataframe with columns'''
    data = data[0:0]
    return data

@pytest.fixture
def data_empty():
    '''Empty dataframe'''
    data = pd.DataFrame()
    return data

@pytest.fixture
def data_different(data):
    '''Dataframe containing most data types'''
    data = data[[i for i in data.columns if "1" not in i]]
    return data

@pytest.fixture
def data_with_json_col():
    '''Dataframe with a column containing different representations of JSON'''
    col1 = [
        np.nan,
        None,
        "",
        "{}",
        dict(),
        {1 : 1, 4 : 2},
        {"x1" : 1, "x2" : 2},
        {"x1" : 1, 1 : 1},
        '{"x1" : 1, "x2" : 2}',
        '{"x1" : 1, 1 : 1}',
        "{'x1' : 1, 'x2' : 2}",
        "{'x1' : 1, 1 : 1}",
        {"x1" : [1,2,3], 3 : 2},
        ]

    data = pd.DataFrame({"col1" : col1,
                         })
    return data


@pytest.fixture(params=["x",
                        [1,2,3],
                        1,
                        1.0,
                        ])
def data_with_error_json_col(request):
    '''Dataframe with a column containing different representations of data that is not JSON'''
    col1 = [request.param]
    data = pd.DataFrame({"col1" : col1})
    return data

@pytest.fixture 
def function():
    '''Simple function'''
    def x(value):
        result = value
        return result
    return x

@pytest.fixture 
def function_with_sleep():
    '''Function that takes a value and sleeps the code for that amount in seconds'''
    def x(value):
        time.sleep(value)
        return
    return x

@pytest.fixture 
def function_with_loop():
    '''Function that takes a value and loops for that amount in seconds'''
    def x(value):
        start_time = dt.datetime.now()
        while True :
            end_time = dt.datetime.now()
            duration = (end_time - start_time).total_seconds()
            if duration >= value :
                break
        return
    return x

@pytest.fixture 
def _class_simple():
    '''Simple class'''
    class X:
        pass
    return X

@pytest.fixture 
def _class_with_init():
    '''Class with initialization'''
    class X:
        def __init__(self,val1):
            self.val1 = val1
    return X

@pytest.fixture 
def _class_with_function():
    '''Class with a function'''
    class X:
        def x(self):
            result = 1 
            return result
    return X

@pytest.fixture 
def _class_with_property():
    '''Class with a property'''
    class X:
        
        @property
        def x(self):
            result = 1 
            return result
    return X


@pytest.fixture 
def _class_realistic():
    '''Class that looks like a regular class a prgorammer develop'''
    class X:
        
        def __init__(self,val1):
            self.val1 = val1
        
        def x(self):
            result = 1 
            return result
        
        @property
        def x_property(self):
            return self.val1
    return X




