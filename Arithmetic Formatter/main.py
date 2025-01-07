
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        parts = problem.split()

        if not (parts[0].isdigit() and parts[2].isdigit()):
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

    if show_answers:
        return dec_with_answer(problems)
    else:
        return dec_without_answer(problems)

def dec_without_answer(problems):
    first_line = ""
    second_line = ""
    third_line = ""
    for problem in problems:
        parts = problem.split()
        space = max(len(parts[0]), len(parts[2])) + 2

        first_line += parts[0].rjust(space) + "    "
        second_line += parts[1] + parts[2].rjust(space - 1) + "    "
        third_line += "-" * space + "    "

    return f"{first_line.rstrip()}\n{second_line.rstrip()}\n{third_line.rstrip()}"

def dec_with_answer(problems):
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for problem in problems:
        parts = problem.split()
        space = max(len(parts[0]), len(parts[2])) + 2

        first_line += parts[0].rjust(space) + "    "
        second_line += parts[1] + parts[2].rjust(space - 1) + "    "
        third_line += "-" * space + "    "

        if parts[1] == "+":
            result = int(parts[0]) + int(parts[2])
        elif parts[1] == "-":
            result = int(parts[0]) - int(parts[2])
        fourth_line += str(result).rjust(space) + "    "

    return f"{first_line.rstrip()}\n{second_line.rstrip()}\n{third_line.rstrip()}\n{fourth_line.rstrip()}"


if __name__ == "__main__":
    print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')