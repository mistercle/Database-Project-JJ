import mysql.connector
import test
"""
오픈 API에서 데이터를 받아와서 DB를 업데이트하는 파일
"""



"""
getlist = 'getMemberCurrStateList'#국회의원 현황조회 method_num = 0
getdetail = 'getMemberDetailInfoList'#국회의원 상세조회 method_num = 1
getjungdang = 'getJungDangMemberCurrStateList'#소속정당별 국회의원 목록조회 method_num = 2
getcomm = 'getCommMemberCurrStateList'#소속위원회별 국회의원 목록조회 method_num = 3
getmethod = 'getLoOrProporMemberCurrStateList'#당선방법별 국회의원 목록 정보조회 method_num = 4
getlocalmen = 'getLocalMemberCurrStateList'#지역별 국회의원 목록 정보조회 method_num = 5
getparty = 'getPolySearch' #정당검색 method_num = 6
getlocal = 'getLocalSearch' #지역검색 method_num = 7
"""




def assemblymanset():
    cnx = mysql.connector.connect(user='root', password='flalxlem116',
                                  host='127.0.0.1',
                                  database='dbtest')
    cursor = cnx.cursor()

    table = "Assemblyman"
    table_column = "(assemblymanCd, empNm, partyNm, reeleGbnNm, origCd) "
    insert_tuple = "INSERT into " + table + table_column + "values"
    query = insert_tuple + "(%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE assemblymanCd = assemblymanCd;"
    items0 = test.getitem(0)
    #items1 = test.getitem(1)
    #items2 = test.getitem(2)
    #items3 = test.getitem(3)
    #items4 = test.getitem(4)
    #items5 = test.getitem(5)
    items6 = test.getitem(6)
    #items7 = test.getitem(7)
    for item in items0 :
        data_assemblymanCd = item['num']
        data_empNm = item['empNm']
        data_partyNm = test.getpartyCd(data_assemblymanCd, item['deptCd'])
        data_reeleGbNm = item['reeleGbnNm']
        data_origNm = item['origNm']
        #print(data_origNm)
        cursor.execute("select runningAreaCd from runningarea where runningarea.runningAreaNm = '" + data_origNm + "';")
        origCd = cursor.fetchall()
        #print(origCd)
        data_origCd = origCd[0][0]
        #print(data_origCd)
        #data_hobbyNm = test.gethobbyCd(data_assemblymanCd, item['deptCd'])
        cursor.execute(query, (data_assemblymanCd, data_empNm, data_partyNm, data_reeleGbNm, data_origCd))
        cnx.commit()


    cursor.close()
    cnx.close()

