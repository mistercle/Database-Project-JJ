import mysql.connector

set_DB_using_openAPI = '1'
search_assemblyman = '2'
search_party = '3'
search_committee = '4'
search_proposal = '5'


def print_menu():
    print("-------------------------------------------")
    print("|      * Database Team 'Project JJ' *     |")
    print("-------------------------------------------")
    print("| 1. 오픈 API 를 이용한 DB 세팅           |")
    print("| 2. 국회의원 이름 검색                   |")
    print("| 3. 정당 이름 검색                       |")
    print("| 4. 위원회 검색                          |")
    print("| 5. 발의안 검색                          |")
    print("| else. 종료                              |")
    print("-------------------------------------------")


def DB_setting():
    pass


def assemblyman_searching():
    search_party_name = input("검색할 당명 >> ")
    cnx = mysql.connector.connect(user='root', password='123123', host='127.0.0.1', database='mydb')
    cursor = cnx.cursor()

    query = "select * from Party where Party.partyNm = '" + search_party_name + "'"
    cursor.execute(query)

    for tuple in cursor:
        print(tuple[1] + "의 국회 의석 수 : " + str(tuple[2]) + ", 당대표 : " + tuple[3] + ", 창당일 : " + tuple[4])
    query = "select empNm from Assemblyman natural join Party where Party.partyNm = '" + search_party_name + "'"
    cursor.execute(query)
    print("-------" + search_party_name + "에 소속한 국회의원----")
    for tuple in cursor:
        print(tuple[0])
    cursor.close()
    cnx.close()

    pass


def party_searching():
    pass


def committee_searching():
    pass


def proposal_searching():
    pass


if __name__ == '__main__':
    while True:
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
        else:
            print("프로그램 종료")
            break
