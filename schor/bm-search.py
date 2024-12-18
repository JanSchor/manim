
from manim import *
import copy



def convertBitMap(returnMap):
    for i, line in enumerate(returnMap):
        pairLine = []
        for j, val in enumerate(line):
            if j <= 0:
                hmod = 0
            else:
                hmod = returnMap[i][j-1][1]
            if i <= 0:
                vmod = 0
            else:
                vmod = returnMap[i-1][j][0]

            firstVal = val*(1 + vmod)
            secondVal = val*(1 + hmod)
            pair = [firstVal, secondVal]
            returnMap[i][j] = pair

    return returnMap


# Image for showing the conversion of bitmap
# manim -pql schor/bm-search.py BitMapSearchConv
# manim -pqh -t schor/bm-search.py BitMapSearchConv
class BitMapSearchConv(Scene):
    
    def construct(self):
        # For both variants of export
        MODE = "dark"

        if MODE == "dark":
            blue = BLUE_E
            text = WHITE
        else:
            blue = BLUE_D
            text = BLACK

        bitMap = [[0, 0, 1, 1, 1],
                  [0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1]]
        
        bitmapConverted = convertBitMap(copy.deepcopy(bitMap))
        
        bitMapGroup = []
        for line in bitMap:
            newLine = []
            for i in line:
                newLine.append(Integer(i))
            
            group = VGroup(*newLine)
            total_element_width = sum(elem.width for elem in group)
            num_gaps = len(group) - 1
            buff = (2 - total_element_width) / num_gaps

            bitMapGroup.append(group.arrange(buff=buff))

        bitMapConvertedGroup = []
        for line in bitmapConverted:
            newLineC = []
            for i in line:
                group = VGroup(MathTex("("),
                               VGroup(Integer(i[0]),
                                      Integer(i[1])
                               ).arrange(buff=0.3),
                               MathTex(")")
                        )
                total_element_width = sum(elem.width for elem in group)
                num_gaps = len(group) - 1
                buff = (1 - total_element_width) / num_gaps
                newLineC.append(group.arrange(buff=buff))

            bitMapConvertedGroup.append(VGroup(*newLineC).arrange(buff=0.1))
        bitMapVGroup = VGroup(*bitMapGroup).arrange(buff=0.3, direction=DOWN)
        bitMapConvertedVGroup = VGroup(*bitMapConvertedGroup).arrange(buff=0.3, direction=DOWN)

        bitMapVGroup.move_to(4*LEFT)
        bitMapConvertedVGroup.move_to(2.8*RIGHT)

        bitMapVGroup.set_color(text)
        bitMapConvertedVGroup.set_color(text)

        bitMapConvertedVGroup[0][4][1][1].set_color(RED)
        bitMapConvertedVGroup[2][4][1][1].set_color(GREEN)
        bitMapConvertedVGroup[2][4][1][0].set_color(GREEN)
        bitMapConvertedVGroup[2][2][1][0].set_color(blue)

        bitMapVGroup[2][3:5].set_color(GREEN)
        bitMapVGroup[1][4].set_color(GREEN)

        bitMapVGroup[0][4].set_color(RED)
        bitMapVGroup[0][3].set_color(RED)
        bitMapVGroup[0][2].set_color(RED)

        bitMapVGroup[1][2].set_color(blue)
        bitMapVGroup[2][2].set_color(blue)
        

        self.add(bitMapVGroup)
        self.add(bitMapConvertedVGroup)


# Animation for showing the algorithm process
# manim -pql schor/bm-search.py BitMapSearchAlg
# manim -pqh -t -i schor/bm-search.py BitMapSearchAlg
class BitMapSearchAlg(Scene):
    def construct(self):
        # For both variants of export
        MODE = "dark"

        if MODE == "dark":
            blue = BLUE_E
            text = WHITE
        else:
            blue = BLUE_D
            text = BLACK

        bitMap = [[0, 0, 1, 1, 1],
                  [0, 0, 1, 0, 1],
                  [1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1]]
        
        bitmapConverted = convertBitMap(copy.deepcopy(bitMap))
        
        bitMapGroup = []
        for line in bitMap:
            newLine = []
            for i in line:
                newLine.append(Integer(i))
            
            group = VGroup(*newLine)
            total_element_width = sum(elem.width for elem in group)
            num_gaps = len(group) - 1
            buff = (2 - total_element_width) / num_gaps

            bitMapGroup.append(group.arrange(buff=buff))

        bitMapConvertedGroup = []
        for line in bitmapConverted:
            newLineC = []
            for i in line:
                group = VGroup(MathTex("("),
                               VGroup(Integer(i[0]),
                                      Integer(i[1])
                               ).arrange(buff=0.3),
                               MathTex(")")
                        )
                total_element_width = sum(elem.width for elem in group)
                num_gaps = len(group) - 1
                buff = (1 - total_element_width) / num_gaps
                newLineC.append(group.arrange(buff=buff))

            bitMapConvertedGroup.append(VGroup(*newLineC).arrange(buff=0.1))
        bitMapVGroup = VGroup(*bitMapGroup).arrange(buff=0.3, direction=DOWN)
        bitMapConvertedVGroup = VGroup(*bitMapConvertedGroup).arrange(buff=0.3, direction=DOWN)

        bitMapVGroup.move_to(4*LEFT + DOWN)
        bitMapConvertedVGroup.move_to(2.8*RIGHT + DOWN)

        bitMapVGroup.set_color(text)
        bitMapConvertedVGroup.set_color(text)

        self.add(bitMapVGroup)
        self.add(bitMapConvertedVGroup)


        valsList = []
        for line in bitMapConvertedVGroup:
            valsRow = []
            for val in line:
                self.remove(val[1])
                valsRow.append(val[1])
            valsList.append(valsRow)


        equationBp = VGroup(Integer(1),
                           MathTex("\\cdot("),
                           Integer(1),
                           MathTex("+"),
                           Integer(1),
                           MathTex(")"),
                           VGroup(MathTex("="),
                                  Integer(0)
                                  ).arrange(buff=0.1)
                           ).arrange(buff=0.1)
        
        equationH = equationBp.copy()
        equationV = equationBp.copy()

        equationH.shift(UP*2.5)
        equationV.shift(UP*1.8)
        self.add(equationH)
        self.add(equationV)


        for workingRow in range(len(bitMapVGroup)):
            if workingRow > 0:
                equationV[4].set_color(GREEN)
            else:
                equationV[4].set_color(text)
            for workingCol in range(len(bitMapVGroup[workingRow])):
                if workingCol > 0:
                    equationH[4].set_color(RED)
                else:
                    equationH[4].set_color(text)

                equationV[0].set_value(bitMapVGroup[workingRow][workingCol].get_value())
                equationH[0].set_value(bitMapVGroup[workingRow][workingCol].get_value())

                bitMapConvertedVGroup.set_color(text)
                bitMapVGroup.set_color(text)
                bitMapVGroup[workingRow][workingCol].set_color(YELLOW)

                settingValV = 0
                settingValH = 0
                if workingRow > 0:
                    settingValV = bitMapConvertedVGroup[workingRow-1][workingCol][1][0].get_value()
                    bitMapConvertedVGroup[workingRow-1][workingCol][1][0].set_color(GREEN)
                if workingCol > 0:
                    settingValH = bitMapConvertedVGroup[workingRow][workingCol-1][1][1].get_value()
                    bitMapConvertedVGroup[workingRow][workingCol-1][1][1].set_color(RED)
                
                equationV[4].set_value(settingValV)
                equationH[4].set_value(settingValH)

                self.remove(equationH[0])
                self.remove(equationV[0])

                self.remove(equationH[6])
                self.remove(equationV[6])

                
                
                self.play(ReplacementTransform(bitMapVGroup[workingRow][workingCol].copy(), equationH[0]),
                        ReplacementTransform(bitMapVGroup[workingRow][workingCol].copy(), equationV[0]))
                
                equationH[6][1].set_value(valsList[workingRow][workingCol][1].get_value())
                equationV[6][1].set_value(valsList[workingRow][workingCol][0].get_value())

                self.play(FadeIn(equationH[6]),
                        FadeIn(equationV[6]))
                
                self.wait(0.5)
                self.remove(equationH[6][1]),
                self.remove(equationV[6][1]),
                self.play(FadeOut(equationH[6][0]),
                        FadeOut(equationV[6][0]),
                        ReplacementTransform(equationH[6][1].copy(), valsList[workingRow][workingCol][1]),
                        ReplacementTransform(equationV[6][1].copy(), valsList[workingRow][workingCol][0]),
                        FadeIn(valsList[workingRow][workingCol]),
                        FadeOut(equationH[0]),
                        FadeOut(equationV[0]))
                
        self.wait(5)
        
        