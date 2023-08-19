spam =["apples","bananas","tofu","cats"]
string = ", ".join(spam[:len(spam)-1]) + " and " + "".join(spam[len(spam)-1:])
print(string)