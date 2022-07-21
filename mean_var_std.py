import numpy as np

def calculate(list):
    # If a list containing less than 9 elements is passed into the function,
    # it should raise a ValueError exception with the message: "List must
    # contain nine numbers.
    list_length = len(list)
    if list_length>9 or list_length<9:
        raise ValueError('List must contain nine numbers.')
    else:
        # The function should convert the list into a 3 x 3 Numpy array
        arr = np.array(list)
        arr_2d = np.reshape(arr,(3,3))
        #print(arr_2d)
        #----------------------- --MEAN---------------------------------
        arr_mean_axis_0 = arr_2d.mean(axis=0).tolist()
        arr_mean_axis_1 = arr_2d.mean(axis=1).tolist()
        arr_mean_flattened = arr_2d.mean()
        arr_mean_all = [arr_mean_axis_0,arr_mean_axis_1,arr_mean_flattened]
        #print(arr_mean_all)
        #--------------------------MEAN---------------------------------

        #-------------------------VARIANCE---------------------------------
        arr_var_axis_0 = arr_2d.var(axis=0).tolist()
        arr_var_axis_1 = arr_2d.var(axis=1).tolist()
        arr_var_flattened = arr_2d.var()
        arr_var_all = [arr_var_axis_0,arr_var_axis_1,arr_var_flattened]
        #print(arr_var_all)
        #-------------------------VARIANCE---------------------------------

        #---------------------------STD---------------------------------
        arr_std_axis_0 = arr_2d.std(axis=0).tolist()
        arr_std_axis_1 = arr_2d.std(axis=1).tolist()
        arr_std_flattened = arr_2d.std()
        arr_std_all = [arr_std_axis_0,arr_std_axis_1,arr_std_flattened]
        #print(arr_std_all)
        #----------------------------STD---------------------------------

        #---------------------------MAX---------------------------------
        arr_max_axis_0 = arr_2d.max(axis=0).tolist()
        arr_max_axis_1 = arr_2d.max(axis=1).tolist()
        arr_max_flattened = arr_2d.max()
        arr_max_all = [arr_max_axis_0,arr_max_axis_1,arr_max_flattened]
        #print(arr_max_all)
        #----------------------------MAX---------------------------------

        #---------------------------MIN---------------------------------
        arr_min_axis_0 = arr_2d.min(axis=0).tolist()
        arr_min_axis_1 = arr_2d.min(axis=1).tolist()
        arr_min_flattened = arr_2d.min()
        arr_min_all = [arr_min_axis_0,arr_min_axis_1,arr_min_flattened]
        #print(arr_min_all)
        #----------------------------MIN---------------------------------

        #---------------------------SUM---------------------------------
        arr_sum_axis_0 = arr_2d.sum(axis=0).tolist()
        arr_sum_axis_1 = arr_2d.sum(axis=1).tolist()
        arr_sum_flattened = arr_2d.sum()
        arr_sum_all = [arr_sum_axis_0,arr_sum_axis_1,arr_sum_flattened]
        #print(arr_sum_all)
        #----------------------------SUM---------------------------------

        #------------Summarizing all in a dictionary----------------------
        calculations = dict()
        calculations['mean'] = arr_mean_all
        calculations['variance'] = arr_var_all
        calculations['standard deviation'] = arr_std_all
        calculations['max'] = arr_max_all
        calculations['min'] = arr_min_all
        calculations['sum'] = arr_sum_all
        #print(calculations)
        #------------Summarizing all in a dictionary----------------------
        
        return calculations