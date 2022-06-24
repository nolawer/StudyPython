import os.path
import csv
from post import Post

# def file_read():

file_path = "./blog/post.csv"
file = os.path.isfile(file_path)

post_list = []

# 파일이 있으면 파일을 읽어와서 인스턴스에 저장
if file:    
    f = open(file_path, 'r', encoding='utf8', newline='')
    reader = csv.reader(f)
    
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))        
        post_list.append(post)
        
# 파일이 없으면 파일 생성
else:    
    f = open(file_path, mode='w', encoding='utf8', newline='')
    f.close()