def eval_attempt(secret_code="00000", inserted_code="00000"):
    passed_digits = ""
    secret_rest = []
    inserted_rest = ""

    for my_pointer in range(0, len(secret_code)):
        if inserted_code[my_pointer] == secret_code[my_pointer]:
            passed_digits += secret_code[my_pointer]
        else:
            secret_rest.append(secret_code[my_pointer])
            inserted_rest += inserted_code[my_pointer]

    black_stick = len(passed_digits)
    white_stick = 0

    for compared_digit in inserted_rest:
        if compared_digit in secret_rest:
            white_stick += 1
            secret_rest.remove(compared_digit)

    return black_stick, white_stick


hit, color = eval_attempt("654321", "123456")
print(f"Cernych: {hit} , Bilych: {color}")
hit, color = eval_attempt("123456", "123456")
print(f"Cernych: {hit} , Bilych: {color}")
hit, color = eval_attempt("445123", "451433")
print(f"Cernych: {hit} , Bilych: {color}")
hit, color = eval_attempt("2222", "4444")
print(f"Cernych: {hit} , Bilych: {color}")
hit, color = eval_attempt("12345", "54321")
print(f"Cernych: {hit} , Bilych: {color}")
