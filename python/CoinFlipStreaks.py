from random import randint
H = []
sampleSize = 1000000
for i in range(sampleSize):
    var = randint(0,1)
    if var== 0:
        H.append("H")
    else:
        H.append("T")
streaks = 0
countH = 0
for i in H:
    if i == "H":
        countH += 1
    else:
        countH = 0
    if countH == 6:
        streaks +=1
print(H) 
print(countH)
print("chance of streak: {:.2f}".format((streaks/sampleSize)*100))