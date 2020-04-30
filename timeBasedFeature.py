'''
    Time Based Feature
    The window here is X minutes preceding the current netflow timestamp.
'''

'''
generateSourceTimeBased function generates time-based features using:
    - source ip
    - windowSize
'''
def generateSourceTimeBased(dataFrame, srcAddr, windowSize):
   
    # make the window size in secods
    windowSize = str(windowSize * 60) + 's'

    # create the rolling window
    dataFrame['timeStampIndex'] = pd.to_datetime(dataFrame['Timestamp'])  

    dataFrame.set_index('timeStampIndex', inplace=True).sort_index()

    srcAddr_dis = labelEncoder32(dataFrame, srcAddr, 'SrcAddr_Dis', 'Src IP')

    dataFrame['A_TotBytes_S_t'] = dataFrame['Tot Bytes'].rolling(windowSize).mean()
    dataFrame['A_SrcBytes_S_t'] = dataFrame['TotLen Fwd Pkts'].rolling(windowSize).mean()
    dataFrame['A_TotPkts_S_t'] = dataFrame['Tot Pkts'].rolling(windowSize).mean()
    dataFrame['Dct_Sport_S_t'] = dataFrame['Src Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)
    dataFrame['Distinct_Dport (DstAddr)_t'] = dataFrame['Dst Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)  
    dataFrame['Dct_SrcAddr_S_t'] = dataFrame['SrcAddr_Dis'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)
    dataFrame['Nbr_App_S_t'] = dataFrame['SrcAddr_Dis'].rolling(windowSize).apply(
        lambda x: np.count_nonzero(np.where(x == srcAddr_dis)), raw=False)

    return dataFrame


'''
generateDestinationTimeBased function generates time-based features using:
    - source ip
    - windowSize
'''
def generateDestinationTimeBased(dataFrame, dstAddr, windowSize):
    
    # make the window size in secods
    windowSize = str(windowSize * 60) + 's'

    # create the rolling window
    dataFrame['timeStampIndex'] = pd.to_datetime(dataFrame['Timestamp'])  

    dataFrame.set_index('timeStampIndex', inplace=True).sort_index()

    dstAddr_dis = labelEncoder32(dataFrame, dstAddr, 'DstAddr_Dis', 'Dst IP')

    dataFrame['A_TotBytes_D_t'] = dataFrame['Tot Bytes'].rolling(windowSize).mean()
    dataFrame['A_SrcBytes_D_t'] = dataFrame['TotLen Fwd Pkts'].rolling(windowSize).mean()
    dataFrame['A_TotPkts_D_t'] = dataFrame['Tot Pkts'].rolling(windowSize).mean()
    dataFrame['Dct_Sport_D_t'] = dataFrame['Src Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)
    dataFrame['Distinct_Dport (DstAddr)_t'] = dataFrame['Dst Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)),raw=False) 
    dataFrame['Dct_DstAddr_t'] = dataFrame['DstAddr_Dis'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)
    dataFrame['Nbr_App_D_t'] = dataFrame['DstAddr_Dis'].rolling(windowSize).apply(
        lambda x: np.count_nonzero(np.where(x == dstAddr_dis)), raw=False)

    return dataFrame