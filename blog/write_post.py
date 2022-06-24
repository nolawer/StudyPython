import file_reader as fr
from post import Post
import csv


# 마지막 게시글 id 값 확인
def last_id():
    if not fr.post_list:
        result = 1
    else:
        result = fr.post_list[-1].get_id()
        
    return result
    

print("\n\n-- 게시글 쓰기 --")
write_id = last_id()
write_title = input("제목을 입력해주세요 >>")
if not write_title:
    write_title = input("제목을 입력해주세요 >>")
else:
    pass
write_content = input("본문을 입력해 주세요 >>>")
if not write_content:
    write_content = input("본문을 입력해 주세요 >>>")
else:
    pass
write_view_count = 0

post = Post(write_id, write_title, write_content, write_view_count)
fr.post_list.append(post)
f= open(fr.file_path, 'w', encoding='utf8', newline='')
wr = csv.writer(f)
wr.writerow(post)
f.close()
