class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # In each step, if we have k operators we can perform k different computations
        # For each option, replace the part of the string "x?y" with the result "z" = str(int(x)?int(y))
        evaluated_expressions = {}
        return self.rec(expression, evaluated_expressions)

    def rec(self, expression, hashed_expressions):
        # Base case where there is only a single value left
        if expression.isdigit(): 
            return [int(expression)]

        # Use cached memorisation
        if expression in hashed_expressions:
            return hashed_expressions[expression]

        output = []
        # Iterate through each element to find operators (can't just go every other since some digits take two chars)
        for i,x in enumerate(expression):
            if x == '+' or x == '-' or x == '*':
                # Using operator as pivot, recursively get all possible values acquired to its left and right
                all_lefts = self.rec(expression[:i], hashed_expressions)
                all_rights = self.rec(expression[i+1:], hashed_expressions)
                # Append all combinations available to output
                for left_val in all_lefts:
                    for right_val in all_rights:
                        if x == '+':
                            output.append(left_val + right_val)
                        elif x == '-':
                            output.append(left_val - right_val)
                        else:
                            output.append(left_val * right_val)
        # Add result from this expression to dict for potential duplicates
        hashed_expressions[expression] = output
        return output
