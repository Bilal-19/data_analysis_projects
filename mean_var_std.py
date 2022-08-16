import numpy as np
def calculate(list):
    # raise exception if the length of array is less than 9
    if len(list) < 9:
        raise ValueError("Array size is less than 9")
        
    elif len(list) >= 9:
        # Converting list into dictionary
        array = np.array(list)
        array = array.reshape(3,3)
        calculations = {
        'mean': [array.mean(axis=0),
                 array.mean(axis=1), 
                 array.mean()],
        
        'variance': [array.var(axis=0),
                     array.var(axis=1),
                     array.var()],
        
        'standard deviation': [array.std(axis=0),
                               array.std(axis=1),
                               array.std()],
        
        'max': [array.max(axis=0),
                array.max(axis=1), 
                array.max()],
        
        'min': [array.min(axis=0),
                array.min(axis=1),
                array.min()],
        
        'sum':[array.sum(axis=0),
               array.sum(axis=1), 
               array.sum()],
        }
        return calculations
    else:
        pass
print(calculate([0,1,2,3,4,5,6,7,8]))

