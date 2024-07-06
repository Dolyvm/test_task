from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from keyboards import start_kb, url_kb, back_kb
from config import PAYMENT_PROVIDER_TOKEN
from table_ctrl import is_valid_date, update_table, get_a2
from utils import start_text, but_f_text, photo_url, img_text, img_desc_text, at_text, nice_data, bad_data, suc_pay_text

#Объявляем нужные роутеры
start_router = Router()
button_router = Router()
payment_router = Router()
text_router = Router()

#Стартовое сообщение и клавиатура
@start_router.message(CommandStart())
async def start_word(message: Message):
    await message.answer(start_text, reply_markup=start_kb())

#Основной обработчик событий, реагирует на колбеки кнопок, тут мы выполняем функционал  4 кнопок
@button_router.callback_query()
async def call_start(call: CallbackQuery):
    data = call.data
    match data:
        case "but_1":
            #Крепим ссылку в виде текста и ввиде url кнопки
            await call.message.edit_text(but_f_text, reply_markup=url_kb())
        case "but_2":
            #Крепим меню оплаты, указываем все данные(2 рубля не разрешило, поставил 200)
            PRICE = LabeledPrice(label="Оплата", amount=200 * 100)
            await call.message.bot.send_invoice(
                chat_id=call.message.chat.id,
                title="Оплата",
                description="Описание платежа",
                provider_token=PAYMENT_PROVIDER_TOKEN,
                currency="RUB",
                prices=[PRICE],
                start_parameter="test-payment",
                payload="test-invoice-payload",
            )
        case "but_3":
            #Крепим картинку
            await call.message.edit_text(text=img_text)
            await call.message.reply_photo(
                photo=photo_url,
                caption=img_desc_text
            )
            await call.message.answer(start_text, reply_markup=start_kb())
        case "but_4":
            #Выводим значение ячейки А2
            await call.message.edit_text(text=at_text+get_a2(), reply_markup=back_kb())
        case "back":
            # Обрабатывваем все случаи с колбеком back, чтобы вернуться в начальное меню
            await call.message.edit_text(start_text, reply_markup=start_kb())

#Роутер реагирует на любое текстовое сообщение
@text_router.message(F.text)
async def any_text(message: Message):
    text = message.text
    match is_valid_date(text):
        case True:
            # В случае если введена дата и она корректна вносим изменения в таблицу
            update_table(text)
            await message.answer(text=nice_data)
            await message.answer(start_text, reply_markup=start_kb())
        case False:
            # Во всех остальных случаях пишем что дата не верна и выводим основное меню
            await message.answer(text=bad_data)
            await message.answer(start_text, reply_markup=start_kb())

#Роутер проверяет статус оплаты
@payment_router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: PreCheckoutQuery):
    await pre_checkout_q.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

#Роутер срабатывает на успешуню опалту
@payment_router.message(F.successful_payment)
async def successful_payment(message: Message):
    # Выводим сообщение о том, что оплата прошла успешно
    await message.reply(suc_pay_text, reply_markup=back_kb(), parse_mode=ParseMode.HTML)
