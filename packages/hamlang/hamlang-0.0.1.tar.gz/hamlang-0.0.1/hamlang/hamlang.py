import re
import sys

class HamLang:
    def __init__(self):
        self.strData = [0]*256
        self.intData = [0]*256

    def toPrint(self, code):
        boolresult = False

        pattern = r'함 (.*) 하'
        varpattern = r'\{.*?\}'

        matches = re.findall(pattern, code)

        if matches:
            result = matches[0]
            varmatches = re.findall(varpattern, result)
            length = len(varmatches)

            for i in range(0, length):
                if (self.strData[varmatches[i].count('흐')]):
                    test = self.varToStr(varmatches[i]) # {흐흠}의 값
                    if boolresult == False:
                        result = matches[0].replace(varmatches[i], test)
                        boolresult = True
                    else:
                        result = result.replace(varmatches[i], test)
                elif (self.intData[varmatches[i].count('후')]):
                    test = self.varToInt(varmatches[i]) # {흐흠}의 값
                    if boolresult == False:
                        result = matches[0].replace(varmatches[i], str(test))
                        boolresult = True
                    else:
                        result = result.replace(varmatches[i], str(test))
                else:
                    print(f'그런 변수는 없습니다. {varmatches[i]}')
                    sys.exit(1)
            return result
        else:
            print('매칭된 결과가 없습니다.')
            sys.exit(1)

    def varToStr(self, value):
        temp = str(self.strData[value.count('흐')])
        return temp

    def varToInt(self, value):
        if (self.intData[value.count('후')]):
            temp = int(self.intData[value.count('후')])
            return temp
        print('자료형 오류입니다.')
        sys.exit(1)
        
    def toStrVar(self, cmd):
        pattern, temp = cmd.split(' ~')
        varpattern = r'\{.*?\}'
        varmatches = re.findall(varpattern, pattern)
        length = len(varmatches)
        boolresult = False
        result = pattern
        for i in range(0, length):
            if (self.strData[varmatches[i].count('흐')]):
                test = self.varToStr(varmatches[i]) # {흐흠}의 값
                if boolresult == False:
                    result = pattern.replace(varmatches[i], test)
                    boolresult = True
                else:
                    result = result.replace(varmatches[i], test)
            elif (self.intData[varmatches[i].count('후')]):
                test = self.varToInt(varmatches[i]) # {흐흠}의 값
                if boolresult == False:
                    result = pattern.replace(varmatches[i], str(test))
                    boolresult = True
                else:
                    result = result.replace(varmatches[i], str(test))
            else:
                print(f'그런 변수는 없습니다. {varmatches[i]}')
                sys.exit(1)
        return result
    
    def toIntVar(self, cmd):
        pattern, temp = cmd.split(' ~')
        varpattern = r'\{.*?\}'
        varmatches = re.findall(varpattern, pattern)
        length = len(varmatches)
        boolresult = False
        result = pattern
        for i in range(0, length):
            if (self.strData[varmatches[i].count('흐')]):
                print('자료형 오류입니다. 감히 훗 자료형에 흠을 넣다니??')
                sys.exit(1)
            elif (self.intData[varmatches[i].count('후')]):
                test = self.varToInt(varmatches[i]) # {흐흠}의 값
                if boolresult == False:
                    result = pattern.replace(varmatches[i], str(test))
                    boolresult = True
                else:
                    result = result.replace(varmatches[i], str(test))
            else:
                print(f'그런 변수는 없습니다. {varmatches[i]}')
                sys.exit(1)
        return result

    def calculateNum(self, var, num):
        varpattern = r'\{.*?\}'
        varmatches = re.findall(varpattern, num)
        length = len(varmatches)
        boolresult = False
        tempResult = num
        for i in range(0, length):
            if (self.strData[varmatches[i].count('흐')]):
                print('자료형 오류입니다. 감히 훗 자료형에 흠을 넣다니??')
                sys.exit(1)
            elif (self.intData[varmatches[i].count('후')]):
                test = self.varToInt(varmatches[i]) # {흐흠}의 값
                if boolresult == False:
                    tempResult = num.replace(varmatches[i], str(test))
                    boolresult = True
                else:
                    tempResult = tempResult.replace(varmatches[i], str(test))
            else:
                print(f'그런 변수는 없습니다. {varmatches[i]}')
                sys.exit(1)
        #num은 문자열 +++--- 이런거
        tokens = tempResult.split('*')
        result = 1
        for token in tokens:
            tempNum = token.count('+') - token.count('-')
            result *= tempNum
        
        real = int(var) + int(result)
        return real
            

    @staticmethod
    def type(code):
        if '함 ' in code and ' 하' in code:
            return 'PRINT'
        if '흠 ' in code and ' ~' in code:
            return 'DEFSTR'
        if '훗 ' in code and ' ~' in code:
            return 'DEFINT'
        if '훗 ' in code and ' !' in code:
            return 'CALCULATE'
        if '헤 ' in code and ' ? ' in code:
            return 'IF'
        if '호 ' in code:
            return 'MOVE'
        
    def compileLine(self, code):
        if code == '':
            return None
        TYPE = self.type(code)

        if TYPE == 'PRINT':
            print(self.toPrint(code))
        elif TYPE == 'DEFSTR':
            var, cmd = code.split('흠 ')
            self.strData[var.count('흐')] = self.toStrVar(cmd)
        elif TYPE == 'DEFINT':
            var, cmd = code.split('훗 ')
            self.intData[var.count('후')] = self.toIntVar(cmd)
        elif TYPE == 'IF':
            cond, cmd = code.replace('헤 ', '').split(' ? ')
            if self.varToInt(cond) == 0: #TODO 이거 변수만 인식하도록 해결 또는 숫자만
                return cmd
        elif TYPE == 'CALCULATE':
            var, num, temp = code.replace(' !', '훗 ').split('훗 ')
            self.intData[var.count('후')] = self.calculateNum(self.intData[var.count('후')], num)
        elif TYPE == 'MOVE':
            return int(code.replace('호 ', ''))

    
    def compile(self, code, check=True, errors=40000):
        ham = False
        recode = ''
        spliter = '\n' if '\n' in code else '~'
        code = code.rstrip().split(spliter)
        if check and (code[0].replace(" ","") != '시작과' or code[-1] != '끝이다' or not code[0].startswith('시작과')):
            raise SyntaxError('함랭이려면 어떻게 시작해야할까?')
        index = 0
        error = 0
        while index < len(code):
            errorline = index
            c = code[index].strip()
            res = self.compileLine(c)
            if ham:
                ham = False
                code[index] = recode
            if isinstance(res, int):
                index = res-2
            if isinstance(res, str):
                recode = code[index]
                code[index] = res
                index -= 1
                ham = True
            index += 1
            error += 1
            if error == errors:
                raise RecursionError(str(errorline+1) + '번째 줄에서 무한 루프가 감지되었습니다.')
            
    def compilePath(self, path):
        with open(path) as file:
            code = ''.join(file.readlines())
            self.compile(code)
