import mysql.connector
import setparty
import test
import setorig
import setprovince
import setDB
import setcomittee
import setproposal
import setevaluation
from setdatabase import database_setting

set_DB_using_openAPI = '1'
search_assemblyman = '2'
search_party = '3'
search_committee = '4'
search_proposal = '5'
search_province = '6'
evaluate = '7'


def print_menu():
    print("*--------------------------------------------------------------*")
    print("|                 # Database Team 'Project JJ' #               |")
    print("*--------------------------------------------------------------*")
    print("| 1. 오픈 API 를 이용한 DB 세팅                                |")
    print("| 2. 국회의원 이름 검색                                        |")
    print("| 3. 정당 이름 검색                                            |")
    print("| 4. 위원회 검색                                               |")
    print("| 5. 발의안 검색                                               |")
    print("| 6. 지역 검색                                                 |")
    print("| 7. 국회의원 평가                                             |")
    print("| else. 종료                                                   |")
    print("*--------------------------------------------------------------*")


def createView(cnx, cursor):
    query = "SELECT * " \
            "FROM assemblyman " \
            # "where assemblyman.empNm = '나경원' "
    cursor.execute(query)
    result_assemblyman = cursor.fetchall()
    for tup in result_assemblyman:
        view_assemblymanCd = tup[0]
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
            for comitteeCd in result_comitteeCd:
                query = "SELECT comitteeNm " \
                        "FROM comittee " \
                        "WHERE comittee.comitteeCd = '" + comitteeCd[0] + "'"
                cursor.execute(query)
                result_comitteeNm = cursor.fetchall()[0]
                # print("*위원회   : ", end="")
                temp_comitteeNm = ""
                for comitteeNm in result_comitteeNm:
                    view_comitteeNm += comitteeNm + ", "
        # print(view_empNm, view_partyNm, view_reeleGbnNm, view_origNm, view_hobbyNm, view_comitteeNm)
        view_query = "CREATE OR REPLACE VIEW assemblyman_view AS " \
                     "SELECT distinct assemblyman.assemblymanCd, assemblyman.empNm, assemblyman.partyNm, assemblyman.reeleGbnNm, runningarea.RunningAreaNm AS origNm, assemblyman.hobbyNm " \
                     "FROM assemblyman, runningarea " \
                     "WHERE assemblyman.origCd = runningarea.runningAreaCd;"
        cursor.execute(view_query)
        cnx.commit()


# 1. 오픈 API 를 이용한 DB 세팅
def DB_setting(cnx, cursor):
    print("*--------------------------------------------------------------*")
    setparty.partyset(cnx, cursor)
    print("■■", end="")
    setprovince.provinceset(cnx, cursor)
    print("■■", end="")
    setorig.origset(cnx, cursor)
    print("■■", end="")
    setDB.assemblymanset(cnx, cursor)
    setcomittee.comitteeset(cnx, cursor)
    print("■■", end="")
    setcomittee.assemblyman_has_comitteeset(cnx, cursor)
    print("■■", end="")
    setproposal.proposalset(cnx, cursor)
    print("■■", end="")
    setproposal.assemblyman_has_proposal(cnx, cursor)
    print("■■", end="")
    createView(cnx, cursor)
    print("■■", end="")
    setevaluation.initrep(cnx, cursor)
    print("■■■", end="")
    setevaluation.setreptrigger(cnx, cursor)
    print("■■■")


# 2. 국회의원 이름 검색
def assemblyman_searching():
    search_man_name = input("\n검색할 국회의원 이름 >> ")
    query = "SELECT * " \
            "FROM assemblyman_view " \
            "WHERE assemblyman_view.empNm = '" + search_man_name + "'"
    cursor.execute(query)
    result_assemblyman = cursor.fetchall()
    if len(result_assemblyman) == 0:
        print("*ERROR : %s 은 존재하지 않는 국회의원입니다." % search_man_name)
        return
    elif len(result_assemblyman) > 1:
        print("*동명이인이 있습니다.")
    for tup in result_assemblyman:
        print("*--------------------------------------------------------------*")
        print("*국회의원 : " + tup[1])
        print("*소속정당 : " + tup[2])
        print("*당선횟수 : " + tup[3])
        print("*선거구   : " + tup[4])
        print("*취미     : " + tup[5])
        print("*위원회   : ", end="")
        query = "SELECT comitteeCd " \
                "FROM assemblyman natural join assemblyman_has_comittee " \
                "WHERE assemblyman.assemblymanCd = '" + tup[0] + "'"
        cursor.execute(query)
        result_comitteeCd = cursor.fetchall()
        view_comitteeNm = ""
        if not len(result_comitteeCd) == 0:
            for comitteeCd in result_comitteeCd:
                query = "SELECT comitteeNm " \
                        "FROM comittee " \
                        "WHERE comittee.comitteeCd = '" + comitteeCd[0] + "'"
                cursor.execute(query)
                result_comitteeNm = cursor.fetchall()[0]
                temp_comitteeNm = ""
                for comitteeNm in result_comitteeNm:
                    view_comitteeNm += comitteeNm + ", "
            if len(result_comitteeCd) == 0:
                print("X", end="")
            else:
                print(view_comitteeNm, end="")
        print()
        query = "SELECT reputation " \
                "FROM assemblyman " \
                "WHERE assemblyman.assemblymanCd = '" + tup[0] + "'"
        cursor.execute(query)
        result_reputation = cursor.fetchall()
        print("*평판점수 : " + str(result_reputation.pop()[0]))

        query = "SELECT content " \
                "FROM evaluation " \
                "WHERE evaluation.assemblymanCd = '" + tup[0] + "'"
        cursor.execute(query)
        result_content = cursor.fetchall()
        if len(result_content) != 0:
            print("*코멘트   : " + result_content[0][0])
        print()


# 3. 정당 이름 검색
def party_searching():
    query = "SELECT Party.partyNm FROM Party"
    cursor.execute(query)
    temp_party = cursor.fetchall()
    searchable_party = []
    print("*------------------------검색 가능한 당명----------------------*")
    for tup in temp_party:
        print("%26s" % tup)
        searchable_party.append(tup[0])
    print("*--------------------------------------------------------------*")
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
    print("--------------" + search_party_name + "에 소속한 국회의원-----------")
    for i, tup in enumerate(result):
        print("%3d. %s" % (i+1, tup[0]))


# 4. 위원회 검색
def committee_searching():
    query = "SELECT comittee.comitteeNm " \
            "FROM comittee"
    cursor.execute(query)
    temp_comittee = cursor.fetchall()
    searchable_comittee = []
    print("*--------------------검색 가능한 위원회 명---------------------*")
    for tup in temp_comittee:
        print("%26s" % tup[0])
        searchable_comittee.append(tup[0])
    print("*--------------------------------------------------------------*")
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
    query = "SELECT empNm, partyNm " \
            "FROM assemblyman " \
            "WHERE assemblymanCd in " \
            "(SELECT assemblymanCd " \
            "FROM assemblyman_has_comittee " \
            "WHERE comitteeCd = '" + result_comittee[0] + "')"
    cursor.execute(query)
    result_memberNm = cursor.fetchall()
    print("\n*--------------------------------------------------------------*")
    print("%16s 인원수 : %s명, 의원회장 : %s" % (search_comittee_name, str(len(result_memberNm)), result_chairmanNm))
    print("*----------------" + search_comittee_name + "에 소속한 국회의원------------------*")
    for memberNm in result_memberNm:
        print("%15s%15s" % (memberNm[0], memberNm[1]))


# 5. 발의안 검색
def proposal_searching():
    query = "SELECT proposalNm " \
            "FROM proposal"
    cursor.execute(query)
    temp_comittee = cursor.fetchall()
    searchable_proposal = []
    print("*--------------------검색 가능한 발의안 명---------------------*")
    for i, tup in enumerate(temp_comittee):
        print("%2d. %s" % (i+1, tup[0]))
        searchable_proposal.append(tup[0])
    print("*--------------------------------------------------------------*")
    search_proposal_name = input("\n검색할 발의안 키워드 >> ")
    query = "SELECT proposalCd, proposalNm, proposerCd " \
            "FROM proposal where proposalNm like '%" + search_proposal_name + "%'"
    cursor.execute(query)
    search_result = cursor.fetchall()
    if len(search_result) == 0:
        print("*ERROR : %s 은 없는 위원회입니다." % search_proposal_name)
        return
    while True:
        print("*-------------------- 검색 결과 %d개 ---------------------*" % len(search_result))
        for i, tup in enumerate(search_result):
            print("%2d. %s" % (i+1, tup[1]))
        print("*--------------------------------------------------------------*")
        search_proposal_num = input("\n검색할 발의안 번호(숫자만 입력) >> ")
        if int(search_proposal_num) <= len(search_result):
            break
        else:
            print("*ERROR : %s 는 잘못된 번호입니다." % search_proposal_num)
    search_one = search_result[int(search_proposal_num)-1]
    query = "SELECT assemblyman.empNm " \
            "FROM assemblyman " \
            "WHERE assemblyman.assemblymanCd = '" + search_one[2] + "'"
    cursor.execute(query)
    result_chairmanNm = cursor.fetchall()
    query = "SELECT empNm, partyNm " \
            "FROM assemblyman " \
            "WHERE assemblymanCd in " \
            "(SELECT assemblymanCd " \
            "FROM assemblyman_has_proposal " \
            "WHERE proposalCd = '" + search_one[0] + "')"
    cursor.execute(query)
    result_memberNm = cursor.fetchall()
    print("\n*--------------------------------------------------------------*")
    print("%16s 발의자수 : %s명, 대표 발의자 : %s" % (search_one[1], str(len(result_memberNm)), result_chairmanNm.pop()[0]))
    print("*-------" + search_one[1] + " 발의 국회의원 목록----------*")
    for memberNm in result_memberNm:
        print("%15s%15s" % (memberNm[0], memberNm[1]))


# 6. 지역 검색
def province_searching():
    query = "SELECT * FROM province"
    cursor.execute(query)
    temp_province = cursor.fetchall()
    searchable_province = []
    print("*----------------------검색 가능한 지역--------------------*")
    for tup in temp_province:
        print("%26s" % tup[1])
        searchable_province.append(tup[1])
    print("*----------------------------------------------------------*")
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

    print("*-----------%7s에 소속한 국회의원 %2d명----------*" % (search_province_name, len(result_manNm)))
    for manNm in result_manNm:
        print("%12s %16s" % (manNm[0], manNm[1]))
    print()


# 7. 국회의원 평가
def evaluate_assemblyman():
    setevaluation.evaluation(cnx, cursor)
    pass


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
        elif menuNum == evaluate:
            evaluate_assemblyman()
        else:
            print("*프로그램 종료")
            cursor.close()
            cnx.close()
            break

