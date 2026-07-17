import sender_stand_request
import data

# Андрей Середа, 44-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_order_and_get_info_by_track():
    # Шаг 1. Выполнить запрос на создание заказа
    create_response = sender_stand_request.post_new_order(data.order_body)
    assert create_response.status_code == 201

    # Шаг 2. Сохранить номер трека заказа
    track_number = create_response.json()["track"]

    # Шаг 3. Выполнить запрос на получение заказа по треку
    order_info_response = sender_stand_request.get_order_info(track_number)

    # Шаг 4. Проверить, что код ответа равен 200
    assert order_info_response.status_code == 200