
class Template:
    """
    Backtracking tends to lend itself more to recursive than iterative solutions
    """
    @staticmethod
    def solve(values, test_solution, size):
        """
        Finds a solution to a backtracking problem.
    
        values: an iterable sequence of values to test
        test_solution: the test to apply for each new permutation
        size: the maximum size of a solution

        Return the solution as a list of values.
        """
        solution = [None] * size

        def extend_solution(position):
            """
            recursively search each permutation, pruning remaining calls if condition is not met
            O(S(n)) time where S is test_solution (pruning) complexity & n is size, O(n) space
            """
            for value in values:
                solution[position] = value
                if test_solution(solution, position):
                    print("Test passed, path will continue:     %s" % solution)
                    # continue recursing until max size solution found or remaining paths exhausted
                    if position >= size-1 or extend_solution(position+1):
                        return solution
                else:
                    print("Test failed, path will be discarded: %s" % solution)
            return None
    
        return extend_solution(0)
    
    @staticmethod
    # an example test function (unique to each problem)
    def no_adjacencies(string, up_to_index):
        """
        See if the sequence filled from indices 0 to up_to_index, inclusive, is
        free of any adjancent substrings. We'll have to try all subsequences of
        length 1, 2, 3, up to half the length of the string. Return False as soon
        as we find an equal adjacent pair.
        """
        length = up_to_index+1
        for j in range(1, length//2+1):
            if string[length-2*j:length-j] == string[length-j:length]:
                return False
        return True


# test code
assert(''.join(str(v) for v in Template.solve("123", Template.no_adjacencies, 10))) == '1213123132'
