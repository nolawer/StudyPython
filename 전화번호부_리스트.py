# 이름, 전화번호로 구성된 전화번호부 만들기
# 1.전화번호 추가(이름과 전화번호 직접 입력)
# 2.전화번호 검색(이름 또는 전화번호로 검색하여 이름, 전화번호 출력)
# 3.전화번호 삭제(이름과 전화번호를 입력하여 전화번호부 삭제)
# 4.전화번호부 전체 출력

phoneList = [{'name': 'aaa', 'num': '111'},{'name': 'bbb', 'num': '222'}, {'name': 'ccc', 'num': '333'}, {'name': 'aaa', 'num': '444'}] # 리스트로 구현

while True:
    print("===============")
    print("1.전화번호 추가")
    print("2.전화번호 검색")
    print("3.전화번호 삭제")
    print("4.전화번호 전체 출력")
    print("5.종료")
    print("===============")
    print("등록된 전화번호 수 : {}".format(len(phoneList)))
    print("===============")

    try:
        ft_num = int(input("사용할 기능의 번호를 입력하세요 >> "))
        if 0 < ft_num <= 5:
            pass
        else:
            print("사용할 수 있는 기능이 아닙니다.")
    except (ValueError, ZeroDivisionError):
        print("숫자만 입력해주세요")


    # 1.전화번호 추가
    if ft_num == 1:
        name_append = input("@ 이름 : ")
        num_append = input("@ 전화번호 : ")
        phoneList.append({'name' : name_append, 'num' : num_append})
        print("{}:{}입력이 완료 되었습니다.".format(name_append, num_append))

    # 2.전화번호 검색
    elif ft_num == 2:
        print("검색할 이름을 입력해주세요.")
        name_find = input("@ 이름 : ")

        f_check = 0

        for i in range(0, len(phoneList)):

            if name_find == phoneList[i]['name']:
                 print("이름 : ", phoneList[i]['name'])
                 print("전화번호 : ", phoneList[i]['num'])
                 print("==============")
                 f_check =+ 1
            else:
                pass

        if f_check == 0:
            print("검색한 이름이 전화본호부에 없습니다.")
        else:
            pass

    # 3.전화번호 삭제
    elif ft_num == 3:
        print("삭제할 이름과 전화번호를 입력해주세요.")
        name_del = input("@ 이름 : ")
        num_del = input("@ 전화번호 : ")

        del_chek = 0

        data_range = len(phoneList)

        for i in range(0, data_range):
            if i < data_range-1:
                if name_del == phoneList[i]['name'] and num_del == phoneList[i]['num']:
                    print("{}:{}를 삭제했습니다.".format(phoneList[i]['name'], phoneList[i]['num']))
                    del phoneList[i]
                    del_chek =+ 1
                else:
                    pass
            else:
                pass

        if del_chek == 0:
            print("입력하신 정보와 일치하는 내역이 없습니다.")
        else:
            pass

    # 4. 전화번호 전체출력
    elif ft_num == 4:
        for data in phoneList:
            print("===============")
            print("이름 : ", data["name"])
            print("번호 : ", data["num"])
            print("===============")
    else:
        print("전화번호부를 종료 합니다.")
        break