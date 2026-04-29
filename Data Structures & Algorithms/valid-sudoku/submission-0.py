class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows first
        for i in range(len(board)):
            myHashMap = {} # keep track of counts 
            for j in range(len(board)):
                digit = board[i][j]
                if digit == ".":
                    continue
                elif int(digit) not in myHashMap:
                    print(f"checking digit {digit}")
                    myHashMap[int(digit)] = 1
                else:
                    print("returned false in rows check")
                    print(myHashMap)
                    return False
        


        # check columns second
        for i in range(len(board)):
            myHashMap = {}
            for j in range(len(board[i])):
                digit = board[j][i]
                if digit == ".":
                    continue
                elif int(digit) not in myHashMap:
                    myHashMap[int(digit)] = 1
                else:
                    print("returned false in column check")
                    return False

        for boxRow in range(3):
            for boxCol in range(3):
                myHashMap = {}
                for i in range(3):
                    for j in range(3):
                        digit = board[boxRow*3 + i][boxCol*3 + j]
                        if digit == ".":
                            continue
                        elif int(digit) not in myHashMap:
                            myHashMap[int(digit)] = 1
                        else:
                            return False
        return True
            