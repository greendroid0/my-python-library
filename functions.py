import time

def rick_roll():
    print("Never gonna give you up")
    time.sleep(1)
    print("Never gonna let you down")
    time.sleep(1)
    print("Never gonna run around and desert you")
    time.sleep(1)
    print("Never gonna make you cry")
    time.sleep(1)
    print("Never gonna tell a lie and hurt you")
    time.sleep(1)
    print()
    time.sleep(1)

rick_roll()
rick_roll()
rick_roll()
print ("You have been Rickrolled!")
time.sleep(1)
print ("This song is singed by: ")
time.sleep(1)

def create_name(first, last):
    first= first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("rick", "astley")

print(full_name)