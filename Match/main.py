name = input("Podaj swoje imię: ")

match name:
    case "Darek":
        print("Nie jesteś Markiem")
    case "Marek":
        print("Witaj Marku")
    case "Arek":
        print("Nie jesteś Markiem")
    case _:
        print("Kimkolwiek jesteś, na pewno nie Markiem")


http_error_code = int(input("Podaj http error code: "))

match http_error_code:
    case 404:
        print("Page not found")
    # case 400:
    #     print("Bad request")
    # case 403:
    #     print("Forbidden")
    # case 500:
    #     print("Bad gateway")
    case 400 | 403 | 500:
        print("Not allowed")
    case _:
        print("Unknown error")

