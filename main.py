from datetime import datetime
import requests

def logger(path):

    def decorator(func_to_decorate):

        def wrapper(*args, **kwargs):

            dttm = str(datetime.now())
            args_ = str(args)
            kwargs_ = '; '.join([f'{key}: {value}' for key, value in kwargs.items()])
            arguments = args_ + ' ,' + kwargs_
            func_name = func_to_decorate.__name__
            result = func_to_decorate(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as f:
                f.write(dttm + '; ')
                f.write(arguments + '; ')
                f.write(func_name + '; ')
                f.write(result)
                f.write('\n')
                f.close()

            return result

        return wrapper

    return decorator

if __name__ == '__main__':

    heroes_pick = ['Hulk', 'Captain America', 'Thanos']

    @logger('logs.txt')
    def most_int_hero(list):
        r = requests.get('https://akabab.github.io/superhero-api/api/all.json')
        heroes_int_list = {}
        for hero in r.json():
            if hero['name'] in heroes_pick:
                heroes_int_list[hero['name']] = hero['powerstats']['intelligence']
        return max(heroes_int_list)

    most_int_hero(heroes_pick)

