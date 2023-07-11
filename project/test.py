import unittest
from my_sum import sum

user_data = []
uInput = 0


class TestSum(unittest.TestCase):
    def test_sum(self,numVal):
        result = sum(numVal)
        print(result)
        self.assertEqual(result,6)


def user_input():
    uInput = input("Input number (N to quit):")
    uInput = uInput.lower()

    if uInput != "n":
        uInput = int(uInput)
        user_data.append(uInput)
        print(user_data)
        user_input()
    else:
        ts = TestSum()
        ts.test_sum(user_data)



if __name__ == '__main__':
    user_input()