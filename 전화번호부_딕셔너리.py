# 이름, 전화번호로 구성된 전화번호부 만들기
# 1.전화번호 추가(이름과 전화번호 직접 입력)
# 2.전화번호 검색(이름 또는 전화번호로 검색하여 이름, 전화번호 출력)
# 3.전화번호 삭제(이름과 전화번호를 입력하여 전화번호부 삭제)
# 4.전화번호부 전체 출력

phoneList = {} # 딕셔너리로 구현

# def searchData():
#     name_find = input("@ 찾으시는 이름 : ")
#     conform = name_find in phoneList.keys()
#     if conform == True:
#         print("{}님의 전화번호 : ".format(name_find), phoneList[name_find])
#     else:
#         print("일치하는 정보가 없습니다.")

# def deleteData():
#     name_del = input("@ 삭제할 이름 : ")
#     num_del = input("@ 삭제할 전화번호 : ")
#
#     conform = name_del in phoneList.keys()
#     conform2 = num_del in phoneList.values()
#
#     if conform == True & conform2 == True:
#         del phoneList[name_del]
#         print("{}님의 전화번호를 삭제했습니다.".format(name_del))
#     else:
#         print("일치하는 정보가 없습니다.")

# def allData():
#     i = 0
#     name_list = list(phoneList.keys())
#     num_list = list(phoneList.values())
#
#     for i in name_list:
#         print("이름 : ", i)
#         print("전화번호 : ", phoneList[i])
#
#         print("총 {}개의 전화번호가 출력되었습니다.".format(len(name_list)))

while True:
    print("===== 전화번호부 =====")
    print("1.전화번호 추가")
    print("2.전화번호 검색")
    print("3.전화번호 삭제")
    print("4.전화번호 전체출력")
    print("5.전화번호부 종료")
    print("=================")
    print("등록된 전화번호 수 : ", len(phoneList))
    print("=================")

    # 사용할 번호 입력 시 예외처리
    try:
        menu = int(input("사용할 기능의 번호를 입력하세요 >>"))
        if 0 < menu <= 5:
            pass
        else:
            print("사용할 수 있는 기능이 아닙니다.")
    except (ValueError, ZeroDivisionError):
        print("숫자만 입력해주세요")


    if menu == 1: #입력
        name = input("@ 이름 : ")
        number = input("@ 전화번호 : ")
        phoneList[name] = number
        print("입력이 완료 되었습니다.")

    elif menu == 2: #이름으로 전화번호 검색
        name_find = input("@ 찾으시는 이름 : ")
        conform = name_find in phoneList.keys()
        if conform == True:
            print("{}님의 전화번호 : ".format(name_find), phoneList[name_find])
        else:
            print("일치하는 정보가 없습니다.")

    elif menu == 3: #삭제
        name_del = input("@ 삭제할 이름 : ")
        num_del = input("@ 삭제할 전화번호 : ")

        conform = name_del in phoneList.keys()
        conform2 = num_del in phoneList.values()

        if conform == True & conform2 == True:
            del phoneList[name_del]
            print("{}님의 전화번호를 삭제했습니다.".format(name_del))
        else:
            print("일치하는 정보가 없습니다.")

    elif menu == 4: #전체출력
        i = 0
        name_list = list(phoneList.keys())
        num_list = list(phoneList.values())

        for i in name_list:
            print("이름 : ", i)
            print("전화번호 : ", phoneList[i])

            print("총 {}개의 전화번호가 출력되었습니다.".format(len(name_list)))

    elif menu == 5: #종료
        print("전화번호부가 종료되었습니다.")
        break
    else:
        continue

