import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../coordinates_list/coordinates_edgedetecting2.txt",sep='\t')
# print(data.describe())

#manually add the time stamp
data['time'] = [7243.1865,9053.9209,10864.6455,12675.3711,14486.1045,16296.8564,
                18107.5781,19918.2949,21729.0273,23539.7754,25350.4980,27161.2207,
                28971.9395,30782.6855,32593.4063,34404.1563,36214.8867,38025.6250,
                39836.3594,41647.0742,43457.7969,45268.5273,47079.2656,48889.9883,
                50700.7013,52511.4336,54322.1836,56132.9102,57943.6445,59754.3906,
                61565.1367,63375.8828,65186.6211,66997.3438,68808.0859,70618.8281,
                72429.5547,74240.2891,76051.0313,77861.7891,79672.5000,81483.2266,
                83293.9531,85104.6953,86915.4297,88726.1406,90536.8828,92347.6094,
                94158.3438,95969.0781]

#data.columns -> Index(['left-x', 'left-y', 'right-x', 'right-y', 'time'], dtype='object')

def distance_calculator(first_coord, second_coord):
    '''
    :param first_coord: coordinate of previous timestamp
    :param second_coord: coordinate of later timestamp
    :return: displaced distance
    '''
    return math.sqrt((first_coord[0]-second_coord[0])**2+(first_coord[1]-second_coord[1])**2)


# zip 2 columns to create left end coordinates and right end coordinates
leftend_coordinates = list(zip(data['left-x'].to_numpy(),data['left-y'].to_numpy()))
rightend_coordinates = list(zip(data['right-x'].to_numpy(),data['right-y'].to_numpy()))

#create an empty data frame
processed_data = pd.DataFrame()

#time difference
processed_data['time_gap'] = np.ediff1d(data['time'].to_numpy())

# print(processed_data['time_gap'])
left_movement = np.zeros(len(leftend_coordinates)-1)
for i in range(0,len(leftend_coordinates)-1):
    left_movement[i]=distance_calculator(leftend_coordinates[i],leftend_coordinates[i+1])

right_movement = np.zeros(len(leftend_coordinates)-1)
for i in range(0,len(rightend_coordinates)-1):
    right_movement[i]=distance_calculator(rightend_coordinates[i],rightend_coordinates[i+1])

processed_data['left_movement'] = left_movement
processed_data['right_movement'] = right_movement
processed_data['left_rate'] = processed_data['left_movement']/processed_data['time_gap']
processed_data['right_rate'] = processed_data['right_movement']/processed_data['time_gap']
# processed_data['end_time'] = data['time'][1:]
temp = np.copy(data['time'][1:])
# print(temp)
processed_data['end_time']=temp

plt.plot(processed_data['end_time'],processed_data['left_rate'])
#
# plt.scatter(processed_data['end_time'],processed_data['left_rate'],color='red')
# plt.scatter(processed_data['end_time'],processed_data['right_rate'],color='blue')

plt.show()

