#Time Complexity BigO(n)

memory = {}
def fibonacci_using_dynamicP_top_down(n,memory):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memory:
        memory[n] = fibonacci_using_dynamicP_top_down(n-1,memory) + fibonacci_using_dynamicP_top_down(n-2,memory)
    return memory[n]
  
  fibonacci_using_dynamicP_top_down(8,memory)
