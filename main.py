from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store
from transportation import Transport

shop = Shop(items={
    'печенька': 3,
    'апельсин': 10,
    'ёлка': 1,
    'резиновая курица': 2,
    'зонт': 1,
},)

store = Store(items={
    'печенька': 10,
    'апельсин': 20,
    'телефон': 1
})

storages = {
    'магазин': shop,
    'склад': store,
}

def main():
    while True:
        # вывести содержимое складов
        for storage_name in storages:
            print(f'В {storage_name} храниться: {storages[storage_name].get_items()}')

        # Запросить у пользователя строку
        user_input = input('ВВедите строку в формате"Доставить 3 печенька из склад в магазин".\n'
                           'Введите "stop" или "стоп", чтобы продолжить:\n'
                           )
        if user_input in ('stop', 'стоп'):
            break
        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        delivery = Transport(request=request, storages=storages)
        try:

            delivery.move()
        except BaseError as error:
            delivery.cancel()
            print(error.message)




if __name__ == '__main__':
    main()

