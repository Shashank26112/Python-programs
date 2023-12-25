from PIL import Image im=Image.open("a.jpg") a=im.rotate(60)
a.thumbnail((200,300)) a

im=Image.open("a.jpg").convert('L')
im.thumbnail((300,400))
im
