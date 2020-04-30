def generateSrcAddrFeaturesConnectionBased(dataFrame, srcAddr, windowSize):
    '''
        this function is used to generate connection-based features using
        the given source ip address and window size
    '''

    srcAddr_dis = labelEncoder32(dataFrame, srcAddr, 'SrcAddr_Dis', 'Src IP')

    dataFrame['A_TotBytes_S'] = dataFrame['Tot Bytes'].rolling(windowSize).mean()  # Average TotBytes
    dataFrame['A_SrcBytes_S'] = dataFrame['TotLen Fwd Pkts'].rolling(windowSize).mean()  # Average SrcBytes
    dataFrame['A_TotPkts_S'] = dataFrame['Tot Pkts'].rolling(windowSize).mean()  # Average TotPkts

    dataFrame['Dct_Sport_S'] = dataFrame['Src Port'].rolling(windowSize).apply(lambda x: len(np.unique(x)),
                                                                               raw=False)  # Disctinct Source ports
    dataFrame['Dct_Dport_S'] = dataFrame['Dst Port'].rolling(windowSize).apply(lambda x: len(np.unique(x)), 
                                                                                raw=False)  # Disctinct Destination ports

    dataFrame['Dct_SrcAddr_S'] = dataFrame['SrcAddr_Dis'].rolling(windowSize).apply(lambda x: len(np.unique(x)),
                                                                                    raw=False)  # Disctinct SrcAddr

    dataFrame['Nbr_App_S'] = dataFrame['SrcAddr_Dis'].rolling((windowSize // 10)).apply(
        lambda x: np.count_nonzero(np.where(x == srcAddr_dis)),
        raw=False)  # number of apperance of SrcAddr in (windowSize/10) netflows

    deleteNullRow(dataFrame, 'A_TotBytes_S')

    return dataFrame


def generateDstAddrFeaturesConnectionBased(dataFrame, dstAddr, windowSize):
    '''
        this function is used to generate connection-based features using
        the given destination ip address and window size
    '''

    dstAddr_dis = labelEncoder32(dataFrame, dstAddr, 'DstAddr_Dis', 'Dst IP')

    dataFrame['A_TotBytes_D'] = dataFrame['Tot Bytes'].rolling(windowSize).mean()
    dataFrame['A_SrcBytes_D'] = dataFrame['TotLen Fwd Pkts'].rolling(windowSize).mean()
    dataFrame['A_TotPkts_D'] = dataFrame['Tot Pkts'].rolling(windowSize).mean()

    dataFrame['Dct_Sport_D'] = dataFrame['Src Port'].rolling(windowSize).apply(lambda x: len(np.unique(x)), raw=False)
    dataFrame['Dct_Dport_D'] = dataFrame['Dst Port'].rolling(windowSize).apply(lambda x: len(np.unique(x)), raw=False)

    dataFrame['Dct_DstAddr_D'] = dataFrame['DstAddr_Dis'].rolling(windowSize).apply(lambda x: len(np.unique(x)),
                                                                                    raw=False)

    dataFrame['Nbr_App_D'] = dataFrame['DstAddr_Dis'].rolling((windowSize // 10)).apply(
        lambda x: np.count_nonzero(np.where(x == dstAddr_dis)), raw=False)

    deleteNullRow(dataFrame, 'A_TotBytes_D')

    return dataFrame