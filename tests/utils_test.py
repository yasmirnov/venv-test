import pytest
from main import ticket_price, get_circle_square, get_grade, get_period

# test_value = [
#     (
#         0, "Бесплатно"
#     ),
#     (
#         1, "Бесплатно"
#     ),
#     (
#         7, "100 рублей"
#     ),
#     (
#         18, "200 рублей"
#     ),
#     (
#         25, "300 рублей"
#     ),
#     (
#         60, "Бесплатно"
#     ),
#     (
#         0.5, "Бесплатно"
#     ),
#     (
#         -1, "Ошибка"
#     )
# ]
#
# @pytest.mark.parametrize('test_input, expetected', test_value)
# def test_ticket_price(test_input, expetected):
#     assert ticket_price(test_input) == expetected


# def test_get_circle_square_zero():
#     square = get_circle_square(0)
#     assert square == 0, "Неверное значение для 0"
#
# def test_get_circle_square_one():
#     square = get_circle_square(1)
#     assert round(square, 2) == 3.14
#
# def test_get_circle_square_normal():
#     square = get_circle_square(3)
#     assert round(square, 2) == 28.27
#
# def test_get_circle_square_value_error():
#     with pytest.raises(ValueError):
#         get_circle_square(-2)
#
# def test_get_circle_square_type_error():
#     with pytest.raises(TypeError):
#         get_circle_square("2")


# grade_parameters = [
#     (19, 2),
#     (39, 3),
#     (79, 4),
#     (80, 5),
# ]
#
# @pytest.mark.parametrize('grade_int, grade_get', grade_parameters)
# def test_get_grade(grade_int, grade_get):
#     assert get_grade(grade_int) == grade_get
#
#
# grade_exceptions = [
#     (-1, ValueError),
#     (101, ValueError),
#     ("5", TypeError),
#     (19.5, TypeError)
# ]


# time_parameters = [
#     (6, 'ночь'),
#     (11, 'утро'),
#     (17, 'день'),
#     (20, 'вечер'),
# ]
#
# @pytest.mark.parametrize('time, part_of_day', time_parameters)
# def test_get_period(time, part_of_day):
#     assert get_period(time) == part_of_day


time_exceptions = [
    (25, ValueError),
    (-4, ValueError),
    ("5", TypeError),
    (19.5, TypeError)
]


@pytest.mark.parametrize('time, exception', time_exceptions)
def test_get_time_exceptions(time, exception):
    with pytest.raises(exception):
        get_period(time)
