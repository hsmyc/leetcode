# 18.2.24
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = [''] * numRows
        if numRows == 1 or numRows >= len(s):
            return s
        for i in range(len(s)):
            row = i % (2 * numRows - 2)
            print(row, numRows)
            if row >= numRows:
                row = 2 * numRows - 2 - row
                print(i, row)
            array[row] += s[i]
            print(array)
        return ''.join(array)


Solution().convert('PAYPALISHIRING', 5)
