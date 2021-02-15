from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.room_callback_datas import choose_callback

room_choice = InlineKeyboardMarkup(row_width=8,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text="001", callback_data=choose_callback.new(room_number="001", room="yes")),
                                           InlineKeyboardButton(text="006", callback_data=choose_callback.new(room_number="006", room="yes")),
                                           InlineKeyboardButton(text="107", callback_data=choose_callback.new(room_number="107", room="yes")),
                                           InlineKeyboardButton(text="114", callback_data=choose_callback.new(room_number="114", room="yes")),
                                           InlineKeyboardButton(text="207", callback_data=choose_callback.new(room_number="207", room="yes")),
                                           InlineKeyboardButton(text="214", callback_data=choose_callback.new(room_number="214", room="yes")),
                                           InlineKeyboardButton(text="307", callback_data=choose_callback.new(room_number="307", room="yes")),
                                           InlineKeyboardButton(text="314", callback_data=choose_callback.new(room_number="314", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="002", callback_data=choose_callback.new(room_number="002", room="yes")),
                                           InlineKeyboardButton(text="007", callback_data=choose_callback.new(room_number="007", room="yes")),
                                           InlineKeyboardButton(text="106", callback_data=choose_callback.new(room_number="106", room="yes")),
                                           InlineKeyboardButton(text="113", callback_data=choose_callback.new(room_number="113", room="yes")),
                                           InlineKeyboardButton(text="206", callback_data=choose_callback.new(room_number="206", room="yes")),
                                           InlineKeyboardButton(text="213", callback_data=choose_callback.new(room_number="213", room="yes")),
                                           InlineKeyboardButton(text="306", callback_data=choose_callback.new(room_number="306", room="yes")),
                                           InlineKeyboardButton(text="313", callback_data=choose_callback.new(room_number="313", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="003", callback_data=choose_callback.new(room_number="003", room="yes")),
                                           InlineKeyboardButton(text="008", callback_data=choose_callback.new(room_number="008", room="yes")),
                                           InlineKeyboardButton(text="105", callback_data=choose_callback.new(room_number="105", room="yes")),
                                           InlineKeyboardButton(text="112", callback_data=choose_callback.new(room_number="112", room="yes")),
                                           InlineKeyboardButton(text="205", callback_data=choose_callback.new(room_number="205", room="yes")),
                                           InlineKeyboardButton(text="212", callback_data=choose_callback.new(room_number="212", room="yes")),
                                           InlineKeyboardButton(text="305", callback_data=choose_callback.new(room_number="305", room="yes")),
                                           InlineKeyboardButton(text="312", callback_data=choose_callback.new(room_number="312", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="004", callback_data=choose_callback.new(room_number="004", room="yes")),
                                           InlineKeyboardButton(text="009", callback_data=choose_callback.new(room_number="009", room="yes")),
                                           InlineKeyboardButton(text="104", callback_data=choose_callback.new(room_number="104", room="yes")),
                                           InlineKeyboardButton(text="111", callback_data=choose_callback.new(room_number="111", room="yes")),
                                           InlineKeyboardButton(text="204", callback_data=choose_callback.new(room_number="204", room="yes")),
                                           InlineKeyboardButton(text="211", callback_data=choose_callback.new(room_number="211", room="yes")),
                                           InlineKeyboardButton(text="304", callback_data=choose_callback.new(room_number="304", room="yes")),
                                           InlineKeyboardButton(text="311", callback_data=choose_callback.new(room_number="311", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="005", callback_data=choose_callback.new(room_number="005", room="yes")),
                                           InlineKeyboardButton(text="010", callback_data=choose_callback.new(room_number="010", room="yes")),
                                           InlineKeyboardButton(text="103", callback_data=choose_callback.new(room_number="103", room="yes")),
                                           InlineKeyboardButton(text="110", callback_data=choose_callback.new(room_number="110", room="yes")),
                                           InlineKeyboardButton(text="203", callback_data=choose_callback.new(room_number="203", room="yes")),
                                           InlineKeyboardButton(text="210", callback_data=choose_callback.new(room_number="210", room="yes")),
                                           InlineKeyboardButton(text="303", callback_data=choose_callback.new(room_number="303", room="yes")),
                                           InlineKeyboardButton(text="310", callback_data=choose_callback.new(room_number="310", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="011", callback_data=choose_callback.new(room_number="011", room="yes")),
                                           InlineKeyboardButton(text="102", callback_data=choose_callback.new(room_number="102", room="yes")),
                                           InlineKeyboardButton(text="109", callback_data=choose_callback.new(room_number="109", room="yes")),
                                           InlineKeyboardButton(text="202", callback_data=choose_callback.new(room_number="202", room="yes")),
                                           InlineKeyboardButton(text="209", callback_data=choose_callback.new(room_number="209", room="yes")),
                                           InlineKeyboardButton(text="302", callback_data=choose_callback.new(room_number="302", room="yes")),
                                           InlineKeyboardButton(text="309", callback_data=choose_callback.new(room_number="309", room="yes")),
                                           InlineKeyboardButton(text="402", callback_data=choose_callback.new(room_number="402", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="101", callback_data=choose_callback.new(room_number="101", room="yes")),
                                           InlineKeyboardButton(text="108", callback_data=choose_callback.new(room_number="108", room="yes")),
                                           InlineKeyboardButton(text="201", callback_data=choose_callback.new(room_number="201", room="yes")),
                                           InlineKeyboardButton(text="208", callback_data=choose_callback.new(room_number="208", room="yes")),
                                           InlineKeyboardButton(text="301", callback_data=choose_callback.new(room_number="301", room="yes")),
                                           InlineKeyboardButton(text="308", callback_data=choose_callback.new(room_number="308", room="yes")),
                                           InlineKeyboardButton(text="401", callback_data=choose_callback.new(room_number="401", room="yes")),
                                           InlineKeyboardButton(text="408", callback_data=choose_callback.new(room_number="408", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="403", callback_data=choose_callback.new(room_number="403", room="yes")),
                                           InlineKeyboardButton(text="404", callback_data=choose_callback.new(room_number="404", room="yes")),
                                           InlineKeyboardButton(text="405", callback_data=choose_callback.new(room_number="405", room="yes")),
                                           InlineKeyboardButton(text="406", callback_data=choose_callback.new(room_number="406", room="yes")),
                                           InlineKeyboardButton(text="407", callback_data=choose_callback.new(room_number="407", room="yes")),
                                           InlineKeyboardButton(text="409", callback_data=choose_callback.new(room_number="409", room="yes")),
                                           InlineKeyboardButton(text="410", callback_data=choose_callback.new(room_number="410", room="yes")),
                                           InlineKeyboardButton(text="411", callback_data=choose_callback.new(room_number="411", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="412", callback_data=choose_callback.new(room_number="412", room="yes")),
                                           InlineKeyboardButton(text="413", callback_data=choose_callback.new(room_number="413", room="yes")),
                                           InlineKeyboardButton(text="414", callback_data=choose_callback.new(room_number="414", room="yes")),
                                           InlineKeyboardButton(text="501", callback_data=choose_callback.new(room_number="501", room="yes")),
                                           InlineKeyboardButton(text="502", callback_data=choose_callback.new(room_number="502", room="yes")),
                                           InlineKeyboardButton(text="503", callback_data=choose_callback.new(room_number="503", room="yes")),
                                           InlineKeyboardButton(text="504", callback_data=choose_callback.new(room_number="504", room="yes")),
                                           InlineKeyboardButton(text="505", callback_data=choose_callback.new(room_number="505", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="506", callback_data=choose_callback.new(room_number="506", room="yes")),
                                           InlineKeyboardButton(text="507", callback_data=choose_callback.new(room_number="507", room="yes")),
                                           InlineKeyboardButton(text="508", callback_data=choose_callback.new(room_number="508", room="yes")),
                                           InlineKeyboardButton(text="509", callback_data=choose_callback.new(room_number="509", room="yes")),
                                           InlineKeyboardButton(text="510", callback_data=choose_callback.new(room_number="510", room="yes")),
                                           InlineKeyboardButton(text="511", callback_data=choose_callback.new(room_number="511", room="yes")),
                                           InlineKeyboardButton(text="512", callback_data=choose_callback.new(room_number="512", room="yes")),
                                           InlineKeyboardButton(text="513", callback_data=choose_callback.new(room_number="513", room="yes")),
                                       ],
                                       [
                                           InlineKeyboardButton(text="514", callback_data=choose_callback.new(room_number="514", room="yes"))
                                       ],
                                       [
                                           InlineKeyboardButton(text="🔴Exit🔴", callback_data="Exit")
                                       ]
                                   ])

