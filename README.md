# grocery_store_app
Grocery store application
Часть 1.
part1.py 
Напишите программу, которая выводит n первых элементов последовательности 122333444455555… (число повторяется столько раз, чему оно равно).

Часть 2.
Реализовать Django проект магазина продуктов со следующим функционалом:
* Должна быть реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке.
* Категории и подкатегории обязательно должны иметь наименование, slug-имя, изображение
* Подкатегории должны быть связаны с родительской категорией
* Должен быть реализован эндпоинт для просмотра всех категорий с подкатегориями. Должны быть предусмотрена пагинация.
* Должна быть реализована возможность добавления, изменения, удаления продуктов в админке.
* Продукты должны относится к определенной подкатегории и, соответственно категории, должны иметь наименование, slug-имя, изображение в 3-х размерах, цену
* Должен быть реализован эндпоинт вывода продуктов с пагинацией. Каждый продукт в выводе должен иметь поля: наименование, slug, категория, подкатегория, цена, список изображений
* Реализовать эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.
* Реализовать эндпоинт вывода  состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.
* Реализовать возможность полной очистки корзины
* Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь
* Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной
* Реализовать авторизацию по токену


Авторизация и аутентификация пользователей реализована по токену с помощью библиотеки djoser.


### Installation

- Клонировать репозиторий
  ```
  git clone https://github.com/TatianaBelova333/grocery_store_app.git
  ```
- Создать .env файл на основе .env.example.

- Перейти из корня проекта в папку backend:
  ```
  cd backend
  ```
- Создать и активировать окружение (python3.12):

  ```
  python3 -m venv env
  ```
  ```
  source env/bin/activate
  ```
- Установить зависимости
  ```
  pip install -r requirements.txt
  ```
- Запустить миграции:
  ```
  python3 manage.py migrate
  ```

- Создать суперпользователя
  ```
  python manage.py createsuperuser
  ```
- Заполнить базу тестовыми данными
  ```
  python3 manage.py loaddata category subcategory country brand
  ```
- Запустить проект
  ```
  python3 manage.py runserver
  ```
### Some API examples:

### User registration:

```
POST /api/users/

Content-Type: application/json
{
  "username": "user_example",
  "password": "dgdgdgdg",
}

```

```
Content-Type: application/json
HTTP/1.1 201 Created

{
    "username": "user_example",
    "id": 2
}

```

### Obtain user authentication token:

```
POST /api/auth/token/login/

Content-Type: application/json
{
  "username": "user_example",
  "password": "dgdgdgdg",
}

```
Content-Type: application/json
HTTP/1.1 200 OK

{
    "auth_token": "a8b5e6408b8cde5022a3a3a80e5c310ad88339e3"
}
```


### Get a list of categories

`GET /api/categories/`

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 10,
            "name": "Детское питание",
            "slug": "detskoe-pitanie",
            "subcategories": [
                {
                    "id": 3,
                    "name": "Йогурты",
                    "slug": "jogurtyi",
                    "image": null
                }
            ],
            "image": "http://127.0.0.1:8000/media/detskoe-pitanie/Screenshot_2024-07-08_at_23.45.13.png"
        },
        {
            "id": 9,
            "name": "Закуски",
            "slug": "zakuski",
            "subcategories": [
                {
                    "id": 5,
                    "name": "Орехи",
                    "slug": "orehi",
                    "image": null
                }
            ],
            "image": null
        },
        {
            "id": 5,
            "name": "Замороженные продукты",
            "slug": "zamorozhennyie-produktyi",
            "subcategories": [
                {
                    "id": 1,
                    "name": "Мороженое",
                    "slug": "morozhenoe",
                    "image": null
                }
            ],
            "image": null
        },
}
```
### Get a single Category
`GET /api/categories/2/ `

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": 2,
    "name": "Фрукты, ягода и орехи",
    "slug": "fruktyi-yagoda-i-orehi",
    "subcategories": [
        {
            "id": 5,
            "name": "Орехи",
            "slug": "orehi",
            "image": null
        },
        {
            "id": 2,
            "name": "Фрукты",
            "slug": "fruktyi",
            "image": null
        }
    ],
    "image": null
}
```
### Get a list of all Products

`GET /api/products/`

Filter by subcategory and subcategory__categories or order by fields unit_price, discount, created

`GET /api/categories/?ordering=-created`

`GET /api/categories/?category=3`

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "name": "Йогурт Агуша, клубника",
            "slug": "jogurt-agusha-klubnika",
            "images": [
                {
                    "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-klubnika/Screenshot_2024-07-09_at_00.37.08.png"
                },
                {
                    "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-klubnika/Screenshot_2024-07-09_at_00.37.19.png"
                },
                {
                    "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-klubnika/Screenshot_2024-07-09_at_00.37.31.png"
                }
            ],
            "categories": [
                {
                    "id": 10,
                    "name": "Детское питание",
                    "slug": "detskoe-pitanie"
                },
                {
                    "id": 8,
                    "name": "Молочные продукты",
                    "slug": "molochnyie-produktyi"
                }
            ],
            "subcategory": {
                "id": 3,
                "name": "Йогурты",
                "slug": "jogurtyi"
            },
            "description": "Детский йогурт Агуша",
            "country": "Россия",
            "brand": "Агуша",
            "unit_price": "49.99",
            "discounted_price": "42.49",
            "discount": "15%",
            "unit": "шт",
            "stock_quantity": "35.000",
            "in_cart": false,
            "qty_in_cart": "0.000"
        },
        {
            "id": 1,
            "name": "Йогурт Агуша, черника",
            "slug": "jogurt-agusha-chernika",
            "images": [
                {
                    "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-chernika/Screenshot_2024-07-09_at_00.25.54.png"
                },
                {
                    "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-chernika/Screenshot_2024-07-09_at_00.26.01.png"
                },
                {
                    "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-chernika/Screenshot_2024-07-09_at_00.26.09.png"
                }
            ],
            "categories": [
                {
                    "id": 10,
                    "name": "Детское питание",
                    "slug": "detskoe-pitanie"
                },
                {
                    "id": 8,
                    "name": "Молочные продукты",
                    "slug": "molochnyie-produktyi"
                }
            ],
            "subcategory": {
                "id": 3,
                "name": "Йогурты",
                "slug": "jogurtyi"
            },
            "description": "Детский йогурт Агуша",
            "country": "Россия",
            "brand": "Агуша",
            "unit_price": "48.50",
            "discounted_price": "43.65",
            "discount": "10%",
            "unit": "шт",
            "stock_quantity": "150.000",
            "in_cart": true,
            "qty_in_cart": "2.000"
        }
    ]
}
```

### Get a single Product
`GET /api/products/<pk>/`
```
{
    "id": 1,
    "name": "Йогурт Агуша, черника",
    "slug": "jogurt-agusha-chernika",
    "images": [
        {
            "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-chernika/Screenshot_2024-07-09_at_00.25.54.png"
        },
        {
            "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-chernika/Screenshot_2024-07-09_at_00.26.01.png"
        },
        {
            "image": "http://127.0.0.1:8000/media/products/jogurt-agusha-chernika/Screenshot_2024-07-09_at_00.26.09.png"
        }
    ],
    "categories": [
        {
            "id": 10,
            "name": "Детское питание",
            "slug": "detskoe-pitanie"
        },
        {
            "id": 8,
            "name": "Молочные продукты",
            "slug": "molochnyie-produktyi"
        }
    ],
    "subcategory": {
        "id": 3,
        "name": "Йогурты",
        "slug": "jogurtyi"
    },
    "description": "Детский йогурт Агуша",
    "country": "Россия",
    "brand": "Агуша",
    "unit_price": "48.50",
    "discounted_price": "43.65",
    "discount": "10%",
    "unit": "шт",
    "stock_quantity": "150.000",
    "in_cart": false,
    "qty_in_cart": "0.000"
}

```
### Add a Product to cart (authorization required)
`POST /api/products/<pk>/to_cart/`
```
Content-Type: application/json
{
  "quantity": 10
}

```

```
HTTP/1.1 200 OK

"Товар добавлен в корзину"
```
`POST /api/products/<pk>/to_cart/`
```
Content-Type: application/json
{
  "quantity": 10.5
}



### Get the current user's shopping cart (authorization required).

`GET /api/users/cart/`

```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "cart_id": 1,
    "items": [
        {
            "id": 1,
            "product": {
                "id": 1,
                "name": "Йогурт Агуша, черника",
                "unit": "шт",
                "unit_price": "48.50",
                "discounted_price": 43.65
            },
            "quantity": 1,
            "subtotal": 43.65
        },
        {
            "id": 2,
            "product": {
                "id": 3,
                "name": "Томаты, сливка",
                "unit": "кг",
                "unit_price": "350.90",
                "discounted_price": 350.9
            },
            "quantity": 100,
            "subtotal": 35090.0
        }
    ],
    "total": "35133.65"
}
```
### Clear the current user's shopping cart (authorization required).

`DELETE /api/users/cart/`

```
HTTP/1.1 204 No Content
Content-Type: application/json
{
    "cart_id": 1,
    "items": [],
    "total": null
}
```

### Attepmting to get or delete the cart by an anonymous user

```
HTTP/1.1 401 Unauthorized
{
    "detail": "Учетные данные не были предоставлены."
}
```