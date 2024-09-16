# accepted in first attempt


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(list(map(lambda x: str(int(bin(int(x))[2:])), date.split("-"))))
