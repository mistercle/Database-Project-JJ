
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
    pass


def party_searching():
    pass





if __name__ == '__main__':
    while True:
        print_menu()
        menuNum = input(">> ")
        if menuNum == set_DB_using_openAPI:
            DB_setting()
        elif menuNum == search_assemblyman:
            pass
        elif menuNum == search_party:
            pass
        elif menuNum == search_committee:
            pass
        elif menuNum == search_proposal:
            pass
        else:
            print("프로그램 종료")
            break
