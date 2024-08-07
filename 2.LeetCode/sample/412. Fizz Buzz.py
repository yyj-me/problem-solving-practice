from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
    
if __name__ == "__main__":
    solution = Solution()
    test_input = 15
    print("Input:", test_input)
    result = solution.fizzBuzz(test_input)
    print("Output:", result)
    