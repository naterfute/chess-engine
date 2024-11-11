'''
images.__init__

A module containing nothing but images relevent to the bot

contains images such as

- Chess board
- All Pieces

'''
import os
class images:
    __basePath = os.path.join("images")
    board = os.path.join(__basePath, "standardboard.png")
