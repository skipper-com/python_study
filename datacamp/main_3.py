from datacamp.user import User
from datacamp.post import Post

app_user_1 = User("nn@nn.ru", "Alex", "pwd", "MLOps Engineer")
app_user_1.get_user_info()
app_user_1.change_job_title("DevOps Engineer")
app_user_1.get_user_info()


new_post = Post("on a secret", app_user_1)
new_post.get_post_info()