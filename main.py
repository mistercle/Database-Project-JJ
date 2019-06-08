import mysql.connector

set_DB_using_openAPI = '1'
search_assemblyman = '2'
search_party = '3'
search_committee = '4'
search_proposal = '5'
search_province = '6'


def print_menu():
    print("-------------------------------------------")
    print("|      * Database Team 'Project JJ' *     |")
    print("-------------------------------------------")
    print("| 1. 오픈 API 를 이용한 DB 세팅           |")
    print("| 2. 국회의원 이름 검색                   |")
    print("| 3. 정당 이름 검색                       |")
    print("| 4. 위원회 검색                          |")
    print("| 5. 발의안 검색                          |")
    print("| 6. 지역 검색                            |")
    print("| else. 종료                              |")
    print("-------------------------------------------")


# 1. 오픈 API 를 이용한 DB 세팅
def DB_setting():
    pass


# 2. 국회의원 이름 검색
def assemblyman_searching():
    search_man_name = input("\n검색할 국회의원 이름 >> ")
    query = "SELECT * " \
            "FROM assemblyman " \
            "WHERE assemblyman.empNm = '" + search_man_name + "'"
    cursor.execute(query)
    result_assemblyman = cursor.fetchall()
    if len(result_assemblyman) == 0:
        print("*ERROR : %s 은 존재하지 않는 국회의원입니다." % search_man_name)
        return
    elif len(result_assemblyman) > 1:
        print("*동명이인이 있습니다.")
        # TODO 동명이인 처리 필요
    for tup in result_assemblyman:
        print("----------------------")
        print("*국회의원 : " + tup[1])
        print("*소속정당 : " + tup[2])
        print("*당선횟수 : " + tup[3])
        query = "SELECT runningarea.RunningAreaNm " \
                "FROM runningarea " \
                "WHERE runningarea.runningAreaCd = '" + tup[4] + "'"
        cursor.execute(query)
        result_origNm = cursor.fetchall()
        print("*선거구   : " + result_origNm[0][0])
        print("*취미     : " + tup[5])
        query = "SELECT comitteeCd " \
                "FROM assemblyman natural join assemblyman_has_comittee " \
                "WHERE assemblyman.empNm = '" + search_man_name + "'"
        cursor.execute(query)
        result_comitteeCd = cursor.fetchall()
        if not len(result_comitteeCd) == 0:
            for comitteeCd in result_comitteeCd[0]:
                query = "SELECT comitteeNm " \
                        "FROM comittee " \
                        "WHERE comittee.comitteeCd = '" + comitteeCd + "'"
                cursor.execute(query)
                result_comitteeNm = cursor.fetchall()[0]
                print("*위원회   : ", end="")
                for comitteeNm in result_comitteeNm:
                    print(comitteeNm, end=", ")
                print()


# 3. 정당 이름 검색
def party_searching():
    query = "SELECT Party.partyNm " \
            "FROM Party"
    cursor.execute(query)
    print("------ 검색 가능한 당명 -------")
    for tup in cursor:
        print(tup[0])
    search_party_name = input("\n검색할 당명 >> ")

    query = "SELECT * " \
            "FROM Party " \
            "WHERE Party.partyNm = '" + search_party_name + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        print("*ERROR : %s 은 없는 정당명입니다." % search_party_name)
        return

    for tup in result:
        print(tup[1] + "의 국회 의석 수 : " + str(tup[2]) + ", 당대표 : " + tup[3] + ", 창당일 : " + tup[4])

    query = "SELECT empNm " \
            "FROM Assemblyman natural join Party " \
            "WHERE Party.partyNm = '" + search_party_name + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    print("-------" + search_party_name + "에 소속한 국회의원----")
    for i, tup in enumerate(result):
        print("%3d. %s" % (i+1, tup[0]))


# 4. 위원회 검색
def committee_searching():
    query = "SELECT comittee.comitteeNm " \
            "FROM comittee"
    cursor.execute(query)
    print("------ 검색 가능한 당명 -------")
    for tup in cursor:
        print(tup[0])
    search_comittee_name = input("\n검색할 위원회 >> ")

    query = "SELECT comitteeCd, chairmanCd " \
            "FROM comittee where comittee.comitteeNm = '" + search_comittee_name + "'"
    cursor.execute(query)
    result_comittee = cursor.fetchall()[0]
    if len(result_comittee) == 0:
        print("*ERROR : %s 은 없는 위원회입니다." % search_comittee_name)
        return
    query = "SELECT assemblyman.empNm " \
            "FROM assemblyman " \
            "where assemblyman.assemblymanCd = '" + result_comittee[1] + "'"
    cursor.execute(query)
    result_chairmanNm = cursor.fetchall()[0][0]
    query = "SELECT empNm " \
            "FROM assemblyman " \
            "where assemblymanCd in (SELECT assemblymanCd " \
            "FROM assemblyman_has_comittee where comitteeCd = '" + result_comittee[0] + "')"
    cursor.execute(query)
    result_memberNm = cursor.fetchall()[0]

    print("\n" + search_comittee_name + " 인원수 : " + str(len(result_memberNm)) + "명, 의원회장 : " + result_chairmanNm)
    print("-----" + search_comittee_name + "에 소속한 국회의원------")
    for memberNm in result_memberNm:
        print(memberNm)


# 5. 발의안 검색
def proposal_searching():
    pass


# 6. 지역 검색
def province_searching():
    query = "SELECT * " \
            "FROM province"
    cursor.execute(query)
    print("------ 검색 가능한 지역 -------")
    for tup in cursor:
        print(tup[1])
    search_province_name = input("\n검색할 지역 >> ")

    query = "select empNm " \
            "from assemblyman " \
            "where origNm in " \
            "(SELECT runningAreaCd " \
            "FROM runningarea natural join province " \
            "where provinceNm = '" + search_province_name + "')"
    cursor.execute(query)
    result_manNm = cursor.fetchall()
    if len(result_manNm) == 0:
        print("*ERROR : %s 은 없는 지역입니다." % search_province_name)
        return
    print("-----" + search_province_name + "에 소속한 국회의원------")
    for manNm in result_manNm:
        print(manNm[0])


if __name__ == '__main__':
    while True:
        cnx = mysql.connector.connect(user='root', password='123123', host='127.0.0.1', database='mydb')
        cursor = cnx.cursor()
        print_menu()
        menuNum = input(">> ")
        if menuNum == set_DB_using_openAPI:
            DB_setting()
        elif menuNum == search_assemblyman:
            assemblyman_searching()
        elif menuNum == search_party:
            party_searching()
        elif menuNum == search_committee:
            committee_searching()
        elif menuNum == search_proposal:
            proposal_searching()
        elif menuNum == search_province:
            province_searching()
        else:
            print("프로그램 종료")
            break
        cursor.close()
        cnx.close()
