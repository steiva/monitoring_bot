from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_grid(x: int, string_list: list):
    """
    Function generates grid for keyboard.

    Notes to self: move to a dependencies module,
    upgrade to use not only InlineKeyboardButton.

    Args:
        x (int): Amount of buttons on the xaxis.
        string_list (list): Names of buttons go in here
        like so: ['name1', 'name2', ..., etc.]
    """    
  
    y = len(string_list) // x
    if len(string_list) % x != 0:
        y += 1

    counter = 0
    outer_list = []
    for i in range(y):
        inner_list = []
        for j in range(x):
            try:
                inner_list.append(InlineKeyboardButton(text=string_list[counter], callback_data=buttons[counter]))
            except Exception as e:
                break
            counter+=1
        outer_list.append(inner_list)
    return outer_list

buttons = ['Авто', 'Бизнес, Менеджмент', 'Дети', 'Здоровье', 'ИТ', 'Ивент-индустрия',
           'Индустрия красоты', 'Инновации, наука', 'Искусство, индустрия развлечений',
           'Малый бизнес', 'Маркетинг', 'Мода, стиль', 'Недвижимость', 'Образование',
           'Общепит', 'Перевозки и логистика', 'Политика и общество', 'Право',
           'Промышленность', 'Психология', 'Спорт', 'Стартапы', 'Торговля',
           'Туризм, отели', 'Увлечения, хобби', 'Управление персоналом',
           'Финансы', 'Эзотерика и астрология']

threshold = 15
too_long = []
for button in buttons:
    if len(button) > threshold:
        too_long.append(button)

for to_remove in too_long:
    buttons.remove(to_remove)

initial_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Спикер", callback_data="speaker")
        ],
        [
            InlineKeyboardButton(text="Журналист", callback_data="journalist")
        ]
    ]
)


categories = InlineKeyboardMarkup(
    inline_keyboard=generate_grid(2,buttons) + generate_grid(1,too_long)
)

yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Все верно", callback_data="affirmative"),
            InlineKeyboardButton(text="Ввести заново", callback_data="add_user")
        ]
    ]
)