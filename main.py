from InputHandler import InputHandler
from RiverPassing import Solution

if __name__ == '__main__':
    inputs = InputHandler()
    input("Press any key to solve\n")
    solution = Solution(inputs.houses, inputs.shops, inputs.ports, inputs.bridges)
    solution.solve()
    print(solution)
