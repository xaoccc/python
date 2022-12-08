class Solution:
    def interpret(self, command: str) -> str:
        output = command.replace("()", "o")
        return output.replace("(al)", "al")
