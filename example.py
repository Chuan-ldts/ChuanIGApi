from ChuanIGApi import ChuanIGApi

bot = ChuanIGApi()
bot.Login(username='Insert your username.', password='Insert your password.')

# LIKE
# bot.like("https://www.instagram.com/p/CZ3hFeZlwdU/")
# bot.unlike("https://www.instagram.com/p/CZ3hFeZlwdU/")
# bot.like_recent("ldt.system_test_account")

# COMMENT
# bot.comment("https://www.instagram.com/p/CZ3hFeZlwdU/", "Hello,This is a Test Message")
# bot.comment_recent("ldt.system_test_account", "Hello,This is a Test Message")

# FOLLOW
# bot.follow("__cl__.py")
# bot.unfollow("__cl__.py")

# UPLOAD
# bot.upload_post("panda.jpg", caption="I Love Panda.\nThis is a post test from LDT System\nDate:2022.02.12 02:37\nCreator:CL(Chuan)")
# bot.upload_story("panda.jpg")
# bot.delete_post("Insert your post link")