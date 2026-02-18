class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            Fizz = "Fizz" if i % 3 == 0 else ""
            Buzz = "Buzz" if i % 5 == 0 else ""
            res.append(Fizz + Buzz if  (Fizz + Buzz) else str(i))
        return res
        