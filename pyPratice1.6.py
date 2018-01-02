diet = ['牛扒','虾仁','肉丸','米饭','github']
for x in range(0,5):
    for y in range(0,5):
        if not(x == y):
            print("{}配{}，是最棒的了".format(diet[x],diet[y]))
