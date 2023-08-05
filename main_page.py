import pydirectinput

pydirectinput.click(x=710, y=618)
print("arduino fans on and fans off are not done")
a = input("HELLO! ARE YOU NEW TO J.A.R.V.I.S. (y/n) : ").lower()
a = a.strip()
if a == "y" or a == "yes":
    try:
        import JARVIS
        JARVIS.start_of_jarvis()
    except:
        print("Could not start JARVIS, please try again.")

else:
    try:
        import new_try_jarvis
        new_try_jarvis.start_of_jarvis()
    except:
        print("Could not start JARVIS, please try again.")

    # import new_try_jarvis
    # new_try_jarvis.start_of_jarvis()

# JARVIS.start_of_jarvis()
# fibonacci series
# l = []
# a = 0
# b = 1
# l.append(a)
# l.append(b)
# for i in range(0, 11):
#     c = a + b
#     a = b
#     b = c
#     l.append(c)
#     if i not in l:
#         print(i)
