'''
    Connection Based Feature
    The window here is X number of connections preceding the current netflow.
'''

'''
generateSourceConnectionBased function generates connection-based features using:
    - source ip
    - window size
'''
def generateSourceConnectionBased(dataFrame, srcAddr, windowSize):

    srcAddr_dis = labelEncoder32(dataFrame, srcAddr, 'SrcAddr_Dis', 'Src IP')
    # Average TotBytes
    dataFrame['A_TotBytes_S'] = dataFrame['Tot Bytes'].rolling(windowSize).mean()
    # Average SrcBytes  
    dataFrame['A_SrcBytes_S'] = dataFrame['TotLen Fwd Pkts'].rolling(windowSize).mean()
    # Average TotPkts  
    dataFrame['A_TotPkts_S'] = dataFrame['Tot Pkts'].rolling(windowSize).mean()
    # Disctinct Source ports  
    dataFrame['Dct_Sport_S'] = dataFrame['Src Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)  
    # Disctinct Destination ports
    dataFrame['Dct_Dport_S'] = dataFrame['Dst Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)),raw=False)  
    # Disctinct SrcAddr
    dataFrame['Dct_SrcAddr_S'] = dataFrame['SrcAddr_Dis'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)  
    # number of apperance of SrcAddr in (windowSize/10) netflows
    dataFrame['Nbr_App_S'] = dataFrame['SrcAddr_Dis'].rolling((windowSize // 10)).apply(
        lambda x: np.count_nonzero(np.where(x == srcAddr_dis)), raw=False)  

    return dataFrame


'''
generateDestinationConnectionBased function generates connection-based features using:
    - Destination ip
    - window size
'''
def generateDestinationConnectionBased(dataFrame, dstAddr, windowSize):

    dstAddr_dis = labelEncoder32(dataFrame, dstAddr, 'DstAddr_Dis', 'Dst IP')

    dataFrame['A_TotBytes_D'] = dataFrame['Tot Bytes'].rolling(windowSize).mean()
    dataFrame['A_SrcBytes_D'] = dataFrame['TotLen Fwd Pkts'].rolling(windowSize).mean()
    dataFrame['A_TotPkts_D'] = dataFrame['Tot Pkts'].rolling(windowSize).mean()
    dataFrame['Dct_Sport_D'] = dataFrame['Src Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)
    dataFrame['Dct_Dport_D'] = dataFrame['Dst Port'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)
    dataFrame['Dct_DstAddr_D'] = dataFrame['DstAddr_Dis'].rolling(windowSize).apply(
        lambda x: len(np.unique(x)), raw=False)
    dataFrame['Nbr_App_D'] = dataFrame['DstAddr_Dis'].rolling((windowSize // 10)).apply(
        lambda x: np.count_nonzero(np.where(x == dstAddr_dis)), raw=False)

    return dataFrame