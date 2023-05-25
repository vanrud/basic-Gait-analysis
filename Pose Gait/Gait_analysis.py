from cProfile import label
import os
import pandas as pd

print("[INFO] Starting Gait analysis!!.......")

files = os.listdir()
if len(files) > 7:
    print('[WARNING] Already an instance of the program has been executed!..... \n [INFO] Please clear the old Output and execute this program again for the required result ')

else:
    os.system('python gait_base.py')
    os.system('python combine_base.py')
    os.system('python gait_result.py')
    os.system('python combine_result.py')
    print('[INFO] Task Completed Succesfully!!...')
    for i in range(1,202):
        os.remove('base'+str(i)+'.csv')
        os.remove('result'+str(i)+'.csv')
    print("[INFO] ASCERTAINING THE ANALYSIS...")
    df1 = pd.read_csv('out1.csv', names = ['x', 'y', 'z', 'visibility'])
    df2 = pd.read_csv('out2.csv', names = ['x', 'y', 'z', 'visibility'])
    df = (df2/df1)*100
    print(df)
    results_x = df['x'].to_list()
    results_y = df['y'].to_list()
    results_z = df['z'].to_list()
    
    x = 0
    y = 0
    z = 0

    for i in results_x:
        x += i
    for j in results_y:
        y += i
    for k in results_z:
        z += i
    x = x/len(results_x)
    y = y/len(results_y)
    z = z/len(results_z)
    if x > 70 and y>70 and z>70:
        print("The First sample and the second sample belongs to the same person")
    else:
        print("The samples provided does not match")