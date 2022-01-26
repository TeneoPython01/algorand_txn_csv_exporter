import pandas as pd
from pandas.io.json import json_normalize
import requests
from datetime import datetime

#enter one or more wallet addresses, then run the code.  CSVs will export to the working directory of the code.
#the wallets below are some wallet addresses I found by searching google.  they are here to demo the code only.
my_wallets = [
    'Y76M3MSY6DKBRHBL7C3NNDXGS5IIMQVQVUAB6MP4XEMMGVF2QWNPL226CA',
    'WLWWUUU2HNSYE7L5MY5CH5PMEU2IDC32UMREY363YMJU5JGILTW3WE3UFI'
    ]

#loop through the wallets
for my_wallet in my_wallets:

    try:
        del df_full
    except:
        pass

    df_full = pd.DataFrame()

    looper = 1
    iteration = 0

    #loop through all of the transcations in the wallet, 100 at a time.  (the API has a limit of 100 txns per pull)
    while looper == 1:

        range_start = 100 * iteration
        range_increment = 100
        range_end = range_start + range_increment - 1

        print('get wallet', my_wallet, 'txn in range', range_start, 'to', range_end)

        my_range = str(range_start) + '/to/' + str(range_end)

        #this is the API:
        my_url = 'https://api.algoexplorer.io/v1/account/'+my_wallet+'/transactions/from/'+my_range

        r = requests.get(my_url)
        df_iteration = json_normalize(r.json())

        #when the API call results in zero records, then end the loop.
        if len(df_iteration) == 0:
            looper = 0
            print(str(len(df_full)), ' total txns found in this wallet.')

        df_full = pd.concat([df_full, df_iteration], sort=True)

        iteration = iteration + 1

    #create variables for date and time in yyyymmdd and hhmmss format to use in the exported CSV filename
    my_date = datetime.now().year*10000+datetime.now().month*100+datetime.now().day
    my_time = datetime.now().hour*10000+datetime.now().minute*100+datetime.now().second
    
    #filename syntax is "algo_export_[first 6 chars of wallet address]_[date]_[time].csv"
    filename = './algo_export_'+my_wallet[0:6]+'_'str(my_date)+'_'+str(my_time)+'.csv'
    df_full.to_csv(filename)
    print('export complete: ' + filename + '\n\n')
