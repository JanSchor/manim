
from manim import *



class PascalTriangle(Scene):
    def getPascalTriagleRow(self, rowNum):
        if rowNum <= 1:
            return [1]
        elif rowNum == 2:
            return [1, 1]
        
        row = rowNum*[1]
        prevRow = self.getPascalTriagleRow(rowNum-1)
        for i in range(1, rowNum-1):
            row[i] = prevRow[i-1] + prevRow[i]
        return row


    def construct(self):
        rowsList = []
        for i in range(1, 10):
            intsList = []
            for num in self.getPascalTriagleRow(i):
                intsList.append(Integer(num))
            r = VGroup(*intsList).arrange(buff=0.8)
            r.shift((DOWN * i)/1.5 + 4 * UP)
            rowsList.append(r)
        self.play(Write(rowsList[0]))
        self.wait()
        for row in range(len(rowsList)-1):
            #self.play(Write(rowsList[row]))
            self.play(ReplacementTransform(rowsList[row], rowsList[row+1]))
            self.wait(0.5)
        self.wait()

# manim -pql bell_nums/pyramid.py BellTriangleTest
class BellTriangleTest(Scene):
    def getRowValue(self, x, y, z):
        return x + y * z
    
    def construct(self):
        StartRowOne = Integer(1)
        StartRowOne.shift(UP)

        row2 = [[0, 1, 1], [1, 2, 0]]
        rowGroupList2 = []
        for val in row2:
            valRow = [Integer(val[0]),
                      Integer(val[1], color=RED),
                      Integer(val[2])]

            rowGroupList2.append(valRow)



        g1 = VGroup(
            Text("("), rowGroupList2[0][0],
            Text("+"), rowGroupList2[0][1],
            MathTex("\\cdot"), rowGroupList2[0][2],
            Text(")")).arrange(buff=0.1)
        number = Integer(1)

        g2 = VGroup(
            Text("("), rowGroupList2[1][0],
            Text("+"), rowGroupList2[1][1],
            MathTex("\\cdot"), rowGroupList2[1][2],
            Text(")")).arrange(buff=0.1)
        number1 = Integer(1)
        number2 = Integer(1)

        numG = VGroup(number1, number2).arrange(buff=0.5)

        gr = VGroup(g1, g2).arrange(buff=0.1)


        oneCpy1 = StartRowOne.copy()
        oneCpy2 = StartRowOne.copy()

        
        self.add(StartRowOne)
        self.wait()

        self.play(ReplacementTransform(oneCpy1, rowGroupList2[0][2]),
                  ReplacementTransform(oneCpy2, rowGroupList2[1][0]),
                  FadeIn(gr))
        
        self.wait()

        self.play(ReplacementTransform(g1, number1),
                  ReplacementTransform(g2, number2))
        self.wait()
                

class BellTriangle(Scene):
    def getValue(self, nums, idx):
        return nums[0] + idx*nums[1]

    def triangleRows(self, row):
        triangle = []
        if row <= 1:
            triangle.append([[0, 1]])
        else:
            for prevTriRow in self.triangleRows(row-1):
                triangle.append(prevTriRow)

            newRow = [[0, 1]]

            for numIdx in range(1, row-1):
                rowList = []
                rowList.append(self.getValue(triangle[row-2][numIdx-1], numIdx))
                rowList.append(self.getValue(triangle[row-2][numIdx], numIdx+1))
                newRow.append(rowList)

            newRow.append([1, 0])
            triangle.append(newRow)
        return triangle
    
    def getIntegerTriplets(self, triangle):
        triangleTriplets = []

        for row in triangle:
            rowList = []
            for value in range(len(row)):
                valueList = []
                valueList.append(Integer(row[value][0]))
                valueList.append(Integer(value+1, color=RED))
                valueList.append(Integer(row[value][1]))
                rowList.append(valueList.copy())
            triangleTriplets.append(rowList.copy())
            
        return triangleTriplets
    
    def getBellNumFromRow(self, row):
        bellNum = 0
        for i, n in enumerate(row):
            bellNum += self.getValue(n, i+1)
        return bellNum
    
    
    def construct(self):
        numOfRows = 6
        triangle = self.triangleRows(numOfRows)
        triangleIntegers = self.getIntegerTriplets(triangle)
        playRowTransforAnims = []

        rowNumsGroupGroups = []
        for currRow in range(numOfRows):
            rowGroups = []
            rowGroupsAnims = []
            rowNums = []
            rowTransformAnims = []
            rowTransformGroup1 = []
            rowTransformGroup2 = []
            for j in range(currRow+1):
                exprGroup = VGroup(
                    MathTex("("), triangleIntegers[currRow][j][0],
                    MathTex("+"), triangleIntegers[currRow][j][1],
                    MathTex("\\cdot"), triangleIntegers[currRow][j][2],
                    MathTex(")")).arrange(buff=0.1) # Expression VGroup
                
                rowGroups.append(exprGroup)
                rowNum = Integer(self.getValue(triangle[currRow][j], j+1))
                rowNum.shift(UP*3 + DOWN*currRow)
                rowNums.append(rowNum)
                rowGroupsAnims.append(ReplacementTransform(exprGroup, rowNum))
                rowTransformGroup1.append(rowNum.copy())
                rowTransformGroup2.append(rowNum.copy())
                if currRow+1 < numOfRows:
                    rowTransformAnims.append(ReplacementTransform(rowTransformGroup1[j], triangleIntegers[currRow+1][j][2]))
                    rowTransformAnims.append(ReplacementTransform(rowTransformGroup2[j], triangleIntegers[currRow+1][j+1][0]))

            rowNumsGroup = VGroup(*rowNums).arrange(buff=1.95)
            rowNumsGroupGroups.append(rowNumsGroup)
            rowTempTransformGroup1 = VGroup(*rowTransformGroup1).arrange(buff=1.95)
            rowTempTransformGroup1.shift(UP*3 + DOWN*currRow)
            rowTempTransformGroup2 = VGroup(*rowTransformGroup2).arrange(buff=1.95)
            rowTempTransformGroup2.shift(UP*3 + DOWN*currRow)
            rowNumsGroup.shift(UP*3 + DOWN*currRow)
            rowGroup = VGroup(*rowGroups).arrange(buff=0.2)
            rowGroup.shift(UP*3 + DOWN*currRow)
            if currRow != 0:
                self.play(FadeIn(rowGroup), *playRowTransforAnims)
                self.play(*rowGroupsAnims)
            else:
                self.wait()
                self.play(Write(*rowNums))
            playRowTransforAnims = rowTransformAnims.copy()
        

        plusGroupsAnim = []
        plusGroups = []
        for plusRow in range(1, numOfRows):
            rowPlus = []
            for i in range(plusRow):
                rowPlus.append(MathTex("+"))
            pg = VGroup(*rowPlus).arrange(buff=1.95)
            pg.shift(UP*3 + DOWN*plusRow)
            plusGroups.append(pg)
            plusGroupsAnim.append(FadeIn(pg))
        self.play(*plusGroupsAnim)

        rowEqGroups = []
        rowEqGroupsAnims = []
        bellNumbers = []
        bellNumbersCpy = []
        for rowEq in range(numOfRows):
            if rowEq == 0:
                reg = VGroup(rowNumsGroupGroups[rowEq])
            else:
                reg = VGroup(plusGroups[rowEq-1], rowNumsGroupGroups[rowEq])
            bellNum = Integer(self.getBellNumFromRow(triangle[rowEq]))
            bellNumCpy = bellNum.copy()
            bellNumbersCpy.append(bellNumCpy)
            bellNum.shift(UP*3 + DOWN*rowEq)
            bellNumbers.append(bellNum)
            rowEqGroups.append(reg)
            rowEqGroupsAnims.append(ReplacementTransform(reg, bellNum))

        self.play(*rowEqGroupsAnims)
        bellG = VGroup(*bellNumbers)
        bellCpyGroup = VGroup(*bellNumbersCpy).arrange(buff=0.5)
        self.play(ReplacementTransform(bellG, bellCpyGroup))


        self.play(Write(Text("Bell numbers").shift(UP)))

        self.wait()
