def show_words(**kwargs):
    print(kwargs['pies'], kwargs['kot'])

    for key, value in kwargs.items():
        print(key + "->" + value)


show_words(pies="Dog", kot="Cat", sowa="Owl", mysz="Mouse")

