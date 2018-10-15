Words=dict()
Continue="y"
while Continue=="y":
    SearchingWord=input("Please Enter Your Word")
    if SearchingWord in Words.keys():
        print("Antonym of " + SearchingWord +":" + a[SearchingWord])
    else:
        Answer=input("I dont know.Do you Know?")
        if Answer=="y":
            Word2=input("Motezad ra vard kon:");
            Words[SearchingWord]=Word2
	    Words[Word2]=SearchingWord
    Continue=input("Continue?")
