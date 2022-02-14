from .login import AuthLogin
from .like import LIKE
from .comment import Comment
from .follow import Follow
from .upload import Upload

class ChuanIGApi(AuthLogin, LIKE, Comment, Follow, Upload):pass