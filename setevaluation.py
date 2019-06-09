import test
from setdatabase import database_setting


def evaluation(cnx, cursor):

    table = "evaluation"
    table_column = "(assemblymanCd, favor, content)"
    insert_tuple = "INSERT into " + table + table_column + " values"
    insert_query = insert_tuple + "(%s, %s, %s)"

    assemblymanNm = input("\n평가할 국회위원 이름을 입력하세요 >> ")
    data_assemblymanCd = test.getCd(assemblymanNm, cnx, cursor)
    print(data_assemblymanCd)
    data_favor = int(input("\n어떻게 생각하시나요?(긍정적이라면 1, 부정적이라면 -1) >> "))
    print(data_favor)
    data_content = input("\n그 이유를 입력하세요 >> ")
    print(data_content)

    cursor.execute(insert_query, (data_assemblymanCd, data_favor, data_content))
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

cnx, cursor = database_setting()
setreptrigger(cnx, cursor)