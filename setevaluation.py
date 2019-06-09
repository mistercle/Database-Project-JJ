import test
from setdatabase import database_setting


def evaluation(cnx, cursor):

    table = "evaluation"
    table_column = "(assemblymanCd, favor, content)"
    insert_tuple = "INSERT into " + table + table_column + " values"
    insert_query = insert_tuple + "(%s, %s, %s)"

    assemblymanNm = input("\n평가할 국회위원 이름을 입력하세요 >> ")
    query = "SELECT * " \
            "FROM assemblyman_view " \
            "WHERE assemblyman_view.empNm = '" + assemblymanNm + "'"
    cursor.execute(query)
    result_assemblyman = cursor.fetchall()
    if len(result_assemblyman) == 0:
        print("*ERROR : %s 은 존재하지 않는 국회의원입니다." % assemblymanNm)
        return
    elif len(result_assemblyman) > 1:
        print("*동명이인이 있습니다.")
    for i, assemblyman in enumerate(result_assemblyman):
        print("%d. %s %s %s" % (i+1, assemblyman[1], assemblyman[2], assemblyman[3]))
    assemblymannum = input("\n평가할 국회위원 번호를 입력하세요 >> ")
    if int(assemblymannum) > len(result_assemblyman):
        print("*ERROR : 잘못된 번호입니다.")
        return
    result_one = result_assemblyman[int(assemblymannum)-1]
    data_favor = int(input("\n어떻게 생각하시나요?(긍정적이라면 1, 부정적이라면 -1) >> "))
    data_content = input("\n그 이유를 입력하세요 >> ")

    cursor.execute(insert_query, (result_one[0], data_favor, data_content))
    cnx.commit()

def initrep(cnx, cursor):
    insert_query = "UPDATE assemblyman set reputation = 0 where reputation is NULL"
    cursor.execute(insert_query)
    cursor.execute("select reputation from assemblyman")
    print(cursor.fetchall())
    cnx.commit()

def setreptrigger(cnx, cursor):
    drop_query = "DROP TRIGGER IF EXISTS changerep"
    cursor.execute(drop_query)
    trigger_query = "CREATE TRIGGER changerep AFTER INSERT ON evaluation FOR EACH ROW BEGIN UPDATE assemblyman set reputation = reputation + new.favor where assemblyman.assemblymanCd = new.assemblymanCd; END;"
    cursor.execute(trigger_query)
    cnx.commit()
