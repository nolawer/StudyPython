import file_reader as fr

while True:
    print("\n\n-- 성훈스 블로그 --")
    print("\n-- 메뉴를 입력해주세요 --")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해주세요.")
    else:
        if choice == 1:
            print("게시글 쓰기")
        elif choice == 2:
            print("게시글 목록")
        elif choice == 3:
            print("프로그램 종료")
            break
        
# print(fr.post_list[0].get_title())