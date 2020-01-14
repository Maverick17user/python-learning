def christmasTreePainter(treeMaxSize):
    for count in range(treeMaxSize):
        if count % 2 == 1:
            perLineIndentValue = (treeMaxSize - count) / 2
            perLineIndent = ' ' * perLineIndentValue
            treeLineParticles = '*' * count

            print(perLineIndent + treeLineParticles)

christmasTreePainter(20)