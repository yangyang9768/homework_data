
# 3.   	The read lines from this file and print out ONLY those lines that have a word ‘still’ in them.

# 1.   	Write the lyrics to a new file called song.txt
with open('song.txt', 'w+') as text_file:
    song = "You could never know what it's like\nYour blood like winter freezes just like ice\nAnd there's a cold lonely light that shines from you\nYou'll wind up like the wreck you hide behind that mask you use\nAnd did you think this fool could never win?\nWell look at me, I'm coming back again\nI got a taste of love in a simple way\nAnd if you need to know while I'm still standing, you just fade away\nDon't you know I'm still standing better than I ever did\nLooking like a true survivor, feeling like a little kid\nI'm still standing after all this time\nPicking up the pieces of my life without you on my mind\nI'm still standing(Yeah, yeah, yeah)\nI'm still standing(Yeah, yeah, yeah)"
    text_file.write(song)
# 2.   	Check that a file has been created successfully.
with open('song.txt', 'r') as text_file:
    contents = text_file.read()
    print(contents)

# 3.   	The read lines from this file and print out ONLY those lines that have a word ‘still’ in them.
with open('song.txt', 'r') as text_file:
    lines = text_file. readlines()
    for line in lines:
        if 'still' in line:
            print(line)
