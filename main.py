import mysql.connector
import setparty
import test
import setorig
import setprovince
import setDB
from setdatabase import database_setting

set_DB_using_openAPI = '1'
search_assemblyman = '2'
search_party = '3'
search_committee = '4'
search_proposal = '5'
search_province = '6'


def print_menu():
    print("*------------------------------------------------*")
    print("|         # Database Team 'Project JJ' #         |")
    print("*------------------------------------------------*")
    print("| 1. 오픈 API 를 이용한 DB 세팅                  |")
    print("| 2. 국회의원 이름 검색                          |")
    print("| 3. 정당 이름 검색                              |")
    print("| 4. 위원회 검색                                 |")
    print("| 5. 발의안 검색                                 |")
    print("| 6. 지역 검색                                   |")
    print("| else. 종료                                     |")
    print("*------------------------------------------------*")


def createView(cnx, cursor):

    # TODO 기존에 존재하는 뷰 assemblyman_view 가 존재하면 삭제
    # TODO 새로운 assemblyman_view (국회의원 view_empNm, 소속정당 view_partyNm, 당선횟수 view_reeleGbnNm, 선거구 view_origNm, 취미 view_hobbyNm, 위원회 view_comitteeNm) 생성

    query = "SELECT * " \
            "FROM assemblyman "
    cursor.execute(query)
    result_assemblyman = cursor.fetchall()

    for tup in result_assemblyman:
        view_empNm = tup[1]
        view_partyNm = tup[2]
        view_reeleGbnNm = tup[3]
        query = "SELECT runningarea.RunningAreaNm " \
                "FROM runningarea " \
                "WHERE runningarea.runningAreaCd = '" + tup[4] + "'"
        cursor.execute(query)
        result_origNm = cursor.fetchall()
        view_origNm = result_origNm[0][0]
        view_hobbyNm = ""
        if tup[5]:
            view_hobbyNm = tup[5]
        query = "SELECT comitteeCd " \
                "FROM assemblyman natural join assemblyman_has_comittee " \
                "WHERE assemblyman.empNm = '" + view_empNm + "'"
        cursor.execute(query)
        result_comitteeCd = cursor.fetchall()
        view_comitteeNm = ""
        if not len(result_comitteeCd) == 0:
            for comitteeCd in result_comitteeCd[0]:
                query = "SELECT comitteeNm " \
                        "FROM comittee " \
                        "WHERE comittee.comitteeCd = '" + comitteeCd + "'"
                cursor.execute(query)
                result_comitteeNm = cursor.fetchall()[0]
                # print("*위원회   : ", end="")
                temp_comitteeNm = ""
                for comitteeNm in result_comitteeNm:
                    temp_comitteeNm += comitteeNm + ", "
                view_comitteeNm = temp_comitteeNm
                print()
        # print(view_empNm, view_partyNm, view_reeleGbnNm, view_origNm, view_hobbyNm, view_comitteeNm)
        # TODO assemblyman_view에 위 데이터들로 행 추가


# 1. 오픈 API 를 이용한 DB 세팅
def DB_setting(cnx, cursor):
    print("*------------------------------------------------*")
    setparty.partyset(cnx, cursor)
    print("■■■", end="")
    setprovince.provinceset(cnx, cursor)
    print("■■■", end="")
    setorig.origset(cnx, cursor)
    print("■■■■■", end="")
    setDB.assemblymanset(cnx, cursor)
    createView(cnx, cursor)
    print("■■■■■")


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
        # print("*------------------------------------------------*")
        print("*국회의원 : " + tup[1])
        view_empNm = tup[1]
        print("*소속정당 : " + tup[2])
        view_partyNm = tup[2]
        print("*당선횟수 : " + tup[3])
        view_reeleGbnNm = tup[3]
        query = "SELECT runningarea.RunningAreaNm " \
                "FROM runningarea " \
                "WHERE runningarea.runningAreaCd = '" + tup[4] + "'"
        cursor.execute(query)
        result_origNm = cursor.fetchall()
        print("*선거구   : " + result_origNm[0][0])
        view_origNm = result_origNm[0][0]
        if tup[5]:
            print("*취미     : " + tup[5])
            view_hobbyNm = tup[5]
        query = "SELECT comitteeCd " \
                "FROM assemblyman natural join assemblyman_has_comittee " \
                "WHERE assemblyman.empNm = '" + search_man_name + "'"
        cursor.execute(query)
        result_comitteeCd = cursor.fetchall()
        view_comitteeNm = ""
        if not len(result_comitteeCd) == 0:
            for comitteeCd in result_comitteeCd[0]:
                query = "SELECT comitteeNm " \
                        "FROM comittee " \
                        "WHERE comittee.comitteeCd = '" + comitteeCd + "'"
                cursor.execute(query)
                result_comitteeNm = cursor.fetchall()[0]
                print("*위원회   : ", end="")
                temp_comitteeNm = ""
                for comitteeNm in result_comitteeNm:
                    temp_comitteeNm += comitteeNm + ", "
                view_comitteeNm = temp_comitteeNm
                print()
        # print(view_empNm, view_partyNm, view_reeleGbnNm, view_origNm, view_comitteeNm)
    # 기존에 존재하는 뷰 assemblyman_view 가 존재하면 삭제
    # assemblyman_view (국회의원 view_empNm, 소속정당 view_partyNm, 당선횟수 view_reeleGbnNm, 선거구 view_origNm, 취미 view_hobbyNm, 위원회 view_comitteeNm)로 구성된 뷰 만들기
    # search_man_name = input("\n 검색할 국회의원 이름 >> ")
    # query = "SELECT * " \
    #         "FROM assemblyman " \
    #         "WHERE assemblyman.empNm = '" + search_man_name + "'"
    # cursor.execute(query)
    # result_assemblyman = cursor.fetchall()
    #     if len(result_assemblyman) == 0:
    #         print("*ERROR : %s 은 존재하지 않는 국회의원입니다." % search_man_name)
    #         return
    #     elif len(result_assemblyman) > 1:
    #         print("*동명이인이 있습니다.")
    #         # TODO 동명이인 처리 필요

    # for row in result_assemblyman
    #     print("*국회의원 : " + row[0])
    #     print("*소속정당 : " + row[1])
    #     print("*당선횟수 : " + row[2])
    #     print("*선거구   : " + row[3])
    #     print("*취미     : " + row[4])
    #     print("*위원회   : " + row[5])


# 3. 정당 이름 검색
def party_searching():
    query = "SELECT Party.partyNm FROM Party"
    cursor.execute(query)
    temp_party = cursor.fetchall()
    searchable_party = []
    print("*-----------------검색 가능한 당명---------------*")
    for tup in temp_party:
        print("%26s" % tup)
        searchable_party.append(tup[0])
    print("*------------------------------------------------*")
    search_party_name = input("\n검색할 당명 >> ")
    if search_party_name not in searchable_party:
        print("*ERROR : %s 은 없는 정당명입니다." % search_party_name)
        return
    query = "SELECT * " \
            "FROM Party " \
            "WHERE Party.partyNm = '" + search_party_name + "'"
    cursor.execute(query)
    result = cursor.fetchall()

    for tup in result:
        print(tup[1] + "의 국회 의석 수 : " + tup[2] + ", 당대표 : " + tup[3] + ", 창당일 : " + tup[4])

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
    temp_comittee = cursor.fetchall()
    searchable_comittee = []
    print("*-------------검색 가능한 위원회 명--------------*")
    for tup in temp_comittee:
        print("%26s" % tup[0])
        searchable_comittee.append(tup[0])
    print("*------------------------------------------------*")
    search_comittee_name = input("\n검색할 위원회 >> ")
    if search_comittee_name not in searchable_comittee:
        print("*ERROR : %s 은 없는 위원회입니다." % search_comittee_name)
        return

    query = "SELECT comitteeCd, chairmanCd " \
            "FROM comittee where comittee.comitteeNm = '" + search_comittee_name + "'"
    cursor.execute(query)
    result_comittee = cursor.fetchall()[0]
    query = "SELECT assemblyman.empNm " \
            "FROM assemblyman " \
            "WHERE assemblyman.assemblymanCd = '" + result_comittee[1] + "'"
    cursor.execute(query)
    result_chairmanNm = cursor.fetchall()[0][0]
    query = "SELECT empNm " \
            "FROM assemblyman " \
            "WHERE assemblymanCd in " \
            "(SELECT assemblymanCd " \
            "FROM assemblyman_has_comittee " \
            "WHERE comitteeCd = '" + result_comittee[0] + "')"
    cursor.execute(query)
    result_memberNm = cursor.fetchall()[0]

    print("\n" + search_comittee_name + " 인원수 : " + str(len(result_memberNm)) + "명, 의원회장 : " + result_chairmanNm)
    print("-----" + search_comittee_name + "에 소속한 국회의원------")
    for memberNm in result_memberNm:
        print(memberNm)


# 5. 발의안 검색
def proposal_searching():
    createView(cnx, cursor)
    pass


# 6. 지역 검색
def province_searching():
    query = "SELECT * FROM province"
    cursor.execute(query)
    temp_province = cursor.fetchall()
    searchable_province = []
    print("*-----------------검색 가능한 지역---------------*")
    for tup in temp_province:
        print("%26s" % tup[1])
        searchable_province.append(tup[1])
    print("*------------------------------------------------*")
    search_province_name = input("\n검색할 지역 >> ")
    if search_province_name not in searchable_province:
        print("*ERROR : %s 은 없는 지역입니다." % search_province_name)
        return

    query = "select empNm, partyNm " \
            "from assemblyman " \
            "where origCd in " \
            "(SELECT runningAreaCd " \
            "FROM runningarea natural join province " \
            "WHERE provinceNm = '" + search_province_name + "')"
    cursor.execute(query)
    result_manNm = cursor.fetchall()

    print("*------%7s에 소속한 국회의원 %2d명-----*" % (search_province_name, len(result_manNm)))
    for manNm in result_manNm:
        print("%12s %16s" % (manNm[0], manNm[1]))
    print()


if __name__ == '__main__':
    cnx, cursor = database_setting()
    while True:
        print_menu()
        menuNum = input(">> ")
        if menuNum == set_DB_using_openAPI:
            DB_setting(cnx, cursor)
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
            print("*프로그램 종료")
            cursor.close()
            cnx.close()
            break

