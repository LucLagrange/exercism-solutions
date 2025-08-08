def answer(question):
    print(f"Original question is:\n ------ {question}")

    if "cubed" in question:
        raise ValueError("unknown operation")

    # Parse the question

    parsed_question = (
        question.replace("?", "")
        .replace("What is", "")
        .replace("multiplied by", "*")
        .replace("plus", "+")
        .replace("divided by", "/")
        .replace("minus", "-")
        .strip()
        .split()
    )

    print(f"Parsed question is: {parsed_question}")

    if not parsed_question:
        raise ValueError("syntax error")

    if not parsed_question[0].lstrip("-").isdigit():
        raise ValueError("syntax error")

    result = int(parsed_question[0])

    i = 1

    if len(parsed_question) == 1:
        print(result)
        return result

    if len(parsed_question) % 2 == 0:
        raise ValueError("syntax error")

    else:
        while i < len(parsed_question):

            operator = parsed_question[i]
            if not operator or operator.isdigit():
                raise ValueError("syntax error")

            operand = int(parsed_question[i + 1])

            if operator == "+":
                result = result + operand
            elif operator == "-":
                result = result - operand
            elif operator == "*":
                result = result * operand
            elif operator == "/":
                result = result / operand
            i += 2

    print(result)
    return result
