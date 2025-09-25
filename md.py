# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Идет утка-маляр 🦆, идет, а тут дождь. '
        'Открыла она зонтик, налетел ветер и унес '
        'утку-маляра на Туманный Альбион. \n'
        'Заходит утка-маляр-путешествинница в бар и '
        'заказывает себе пинту Guinness 🍺.'
    )


def step2_no_umbrella():
    print(
        'Идет утка-маляр 🦆, идет, а тут дождь. '
        'Такой силы был дождь, что ее смыло в канализацию. \n'
        'Осотрелась утка-маляр-путешественница, а там черепашки нинзя '
        'пиццу 🍕 едеят. Они ее и угостили'
    )


if __name__ == '__main__':
    step1()
