class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for n in range(1,n+1):
            if n%5 == 0 and n%3==0:
                arr.append("FizzBuzz")
            elif n%3==0:
                arr.append("Fizz")
            elif n%5==0:
                arr.append("Buzz")
            else:
                arr.append(str(n))
        return arr
            

        