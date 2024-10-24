score=int(input("Enter your score: "))
if score<60:
    print("F")
elif 60 <= score <70:
    print("D")
elif 70 <= score <80:
    print("C")
elif 80 <= score <90:
    print("B")
elif 90 <= score <=100:
    print("A")
else:
    print("INVALID SCORE")