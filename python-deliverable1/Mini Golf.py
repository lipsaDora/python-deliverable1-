i = 1
score = 0
user_name = input("Welcome to GC Golf! What's your name?")
holes = input("Hi," + user_name + "!" + "Would you like to play 3 or 6 holes?")
for golf in range(int(holes)):
    putts = input("How many putts for hole " + str(i) + "? " + "(par is 3)")
    i += 1
    score = score + int(putts)
course_par = int(holes) * 3
final_score = score - course_par
if final_score > 0:
    print("Nice try," + user_name + "! " + "Your total score was: +" + str(final_score))
if final_score < 0:
    print("Great job," + user_name + "! " + "Your total score was: " + str(final_score))
if final_score == 0:
    print("Good game," + user_name + "! " + "Your total score was: 0")
