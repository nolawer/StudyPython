class Post:
    """
    id, title, content, view_count
    """
    
    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count
        
    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count
    
    def add_view_count(self):
        self.view_count += 1
        
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_content(self):
        return self.content
    
    def get_view_count(self):
        return self.view_count
    

if __name__ == "__main__":
    post = Post(1, "title1", "content1", 0)
    print(f"{post.get_id()} {post.get_title()}")