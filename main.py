def eval_attempt(secret_code="00000", inserted_code="00000"):
    passed_digits = ""
    secret_rest = ""
    inserted_rest = ""

    for my_pointer in range(0, len(secret_code)):
        if inserted_code[my_pointer] == secret_code[my_pointer]:
            passed_digits += secret_code[my_pointer]
        else:
            secret_rest += secret_code[my_pointer]
            inserted_rest += inserted_code[my_pointer]

    black_stick = len(passed_digits)
    secret_rest = list(secret_rest)
    white_stick = 0

    for compared_digit in inserted_rest:
        if compared_digit in secret_rest:
            white_stick += 1
            secret_rest.remove(compared_digit)

    # print(passed_digits, secret_rest, inserted_rest, black_stick, white_stick)
    # print(100 * "-")


eval_attempt("654321", "123456")
eval_attempt("123456", "123456")
eval_attempt("445123", "451433")
eval_attempt("2222", "4444")
