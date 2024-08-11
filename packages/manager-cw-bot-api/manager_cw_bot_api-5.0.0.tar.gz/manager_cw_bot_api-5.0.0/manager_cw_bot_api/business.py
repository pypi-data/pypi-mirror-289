"""
Module of the Manager-Business-Helper Bot.
"""
import datetime
import json
import pymysql

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command
from aiogram.types import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from manager_cw_bot_api.analytics import Analytic
from manager_cw_bot_api.business_answers import Answers
from manager_cw_bot_api.business_handler import BusinessHandler, router_business
from manager_cw_bot_api.buttons import Buttons
from manager_cw_bot_api.create_table import CreateTable
from manager_cw_bot_api.fsm_handler import GetTicketDataByIDTCK
from manager_cw_bot_api.giga_images import GigaCreator, router_ai_img
from manager_cw_bot_api.gigachatai import GigaChatAI, router_chat_ai
from manager_cw_bot_api.handler_db_sub_operations import SubOperations, HandlerDB
from manager_cw_bot_api.handler_email import HandlerEM, router_handler_em
from manager_cw_bot_api.handler_promo import HandlerEP, router_promo
from manager_cw_bot_api.handler_successful_payment import HandlerSP
from manager_cw_bot_api.mysql_connection import Connection
from manager_cw_bot_api.refund import Refund, router_refund
from manager_cw_bot_api.send_invoice import ChooseMethodOfPayment, router_send_invoice
from manager_cw_bot_api.tickets import (TicketAnswersToUsers, TicketAnswersToAdmin, TicketUserView, TicketAdminView,
                                        router)


class Manager(Bot):
    """
    Manager of the Admin Account and helper 'AI'.
    """
    def __init__(
            self,
            bot_token: str,
            business_conn_id: str,
            admin_id: int,
            mysql_data: dict,
            gigachat_data: dict,
            admin_username: str
    ) -> None:
        super().__init__(bot_token)
        self.__dp = Dispatcher()
        self.router = Router()

        self.router.message.register(
            self.__get_id_ticket_for_show,
            GetTicketDataByIDTCK.id_ticket
        )

        self.__business_connection_id: str = business_conn_id
        self.__admin_id: int = admin_id
        self.__mysql_data: dict = mysql_data
        self.__gigachat_data: dict = gigachat_data
        self.__admin_username: str = admin_username

    async def __privacy(self, message: types.Message) -> None:
        """
        Privacy for the users.

        :param message: Message / Command Privacy.
        :return: None.
        """
        var: InlineKeyboardBuilder = await Buttons.get_language_privacy_menu()
        await self.send_message(
            chat_id=message.from_user.id,
            text=f"Choose your language:",
            reply_markup=var.as_markup()
        )

    async def __eng_privacy(self, call_query: types.CallbackQuery) -> None:
        """
        Explore to show ENG Privacy.

        :param call_query: Callback Query.
        :return: None.
        """
        await self.send_document(
            chat_id=call_query.from_user.id,
            document="https://acdn.cwr.su/src/acdn/new_user_agreement_manager_cw_bot.pdf",
            caption=f"🇬🇧 ENG"
                    f"🗣 <b>{call_query.from_user.first_name}</b>, you must follow these rules, which are indicated in "
                    f"the attached document. It also indicates what we charge, what data we transfer to the "
                    f"server for data processing / analysis, and the like.\n"
                    f"You also <b>automatically</b> accept the user agreement specified in the attachment.\n\n"
                    f"👑 The rules for signing up for a PLUS ➕ subscription are listed <a "
                    f"href='https://acdn.cwr.su/src/acdn/Agreement_and_Terms_of_Use_for_the_Manager_CW_Bot_Service.pdf'"
                    f">here</a>.\n\n🔥 The paid PLUS ➕subscription period is 30 days.\nPLUS's price:\n"
                    f"⭐ 2 TG Stars;\n"
                    f"💳 65 RUB - Different payment options are available.\n\n"
                    f"#UserAgreement #privacy_manager_cw_bot_and_include_api\n"
                    f"#privacy_bot #privacy",
            parse_mode="HTML"
        )

    async def __rus_privacy(self, call_query: types.CallbackQuery) -> None:
        """
        Explore to show RUS Privacy.

        :param call_query: Callback Query.
        :return: None.
        """
        await self.send_document(
            chat_id=call_query.from_user.id,
            document="https://acdn.cwr.su/src/acdn/new_user_agreement_manager_cw_bot.pdf",
            caption=f"🇷🇺 RUS"
                    f"🗣 <b>{call_query.from_user.first_name}</b>, вы должны соблюдать эти правила, которые указаны в "
                    f"прикреплённом док-те. Там также указано какие данные мы собираем и передаем на "
                    f"сервер для обработки / анализа и т.п.\n"
                    f"Вы также автоматически принимаете пользовательское соглашение, указанное во вложении.\n\n"
                    f"👑 Смотрите перечисленные правила оформления подписки PLUS ➕ <a "
                    f"href='https://acdn.cwr.su/src/acdn/Agreement_and_Terms_of_Use_for_the_Manager_CW_Bot_Service.pdf'"
                    f">здесь</a>.\n\n🔥 Срок действия платной подписки PLUS ➕ составляет 30 дней.\nПРАЙС PLUS'а:\n"
                    f"⭐ 2 TG Stars;\n"
                    f"💳 65 RUB - Доступны различные варианты оплаты.\n\n"
                    f"#UserAgreement #privacy_manager_cw_bot_and_include_api\n"
                    f"#privacy_bot #privacy",
            parse_mode="HTML"
        )

    async def __standard_message(self, message: types.Message) -> None:
        """
        Answer to the users and admin.

        :param message: Message.
        :return: None.
        """
        var: InlineKeyboardBuilder = await Buttons.back_on_main()
        await self.send_message(
            chat_id=message.from_user.id,
            text=f"⚡ *{message.from_user.first_name}*, click on the button below to *go to the main menu*.",
            parse_mode="Markdown",
            reply_markup=var.as_markup()
        )

    async def __answer_to_user(self, message: types.Message) -> None:
        """
        Answer to a user from admin-account (as admin).

        :param message: Message of a user.
        :return: None.
        """
        answers: Answers = Answers(
            business_connection_id=self.__business_connection_id,
            admin_id=self.__admin_id
        )
        await answers.answer_to_user(
            self, message
        )

    async def __explore_show_users_ticket(self, call_query: types.CallbackQuery, state: FSMContext) -> None:
        """
        Explore to show user's ticket by id.

        :param call_query: Callback Query.
        :param state: FSM.

        :return: None.
        """
        await state.set_state(GetTicketDataByIDTCK.id_ticket)
        await self.edit_message_text(
            text=f"👌🏻 Please, tell me <b>ID Ticket</b>, which you want to look at.",
            chat_id=call_query.from_user.id,
            message_id=call_query.message.message_id,
            parse_mode="HTML"
        )

    async def __get_id_ticket_for_show(self, message: types.Message, state: FSMContext) -> None:
        """
        Get id ticket for admin answer/view or user view.

        :param message: Message (ID ticket) from admin/the user.
        :param state: FSM.

        :return: None.
        """
        connection: pymysql.connections.Connection | str = await Connection.get_connection(
            self.__mysql_data
        )
        cursor = connection.cursor()
        await state.clear()
        id_ticket = message.text

        var: InlineKeyboardBuilder = await Buttons.back_on_main()
        if len(id_ticket) == 5:
            query: str = f"""SELECT username, tg_id_sender, ticket_data, create_at, status, 
            subject FROM users WHERE id_ticket = %s;"""
            cursor.execute(query, (id_ticket,))
            result: tuple = cursor.fetchall()
            if len(result) == 0:
                await self.send_message(
                    chat_id=message.from_user.id,
                    text=f"Sorry! Data is none!\n"
                         f"Your message: {message.text}",
                    reply_markup=var.as_markup()
                )
            else:
                response: tuple = result[0]

                username: str = response[0]
                id_user_tg: int = int(response[1])
                content_ticket_data: str = response[2]
                create_at: str = response[3]
                status: str = response[4]
                subject: str = response[5]

                await self.send_message(
                    chat_id=message.from_user.id,
                    text=f"👤 Sender: @{username}\n"
                         f"#️⃣ ID Sender: {id_user_tg}\n\n"
                         f"#️⃣ ID Ticket: {id_ticket}\n"
                         f"⌚ Create at {create_at}\n"
                         f"🌐 STATUS: {status}\n"
                         f"✉ Subject: {subject}\n"
                         f"📩 Content: \n\n      {content_ticket_data}",
                    reply_markup=var.as_markup()
                )

        else:
            await self.send_message(
                chat_id=message.from_user.id,
                text=f"Sorry! It's not ID Ticket, because length of your message isn't 5 symbols!\n"
                     f"Your message: {message.text}",
                reply_markup=var.as_markup()
            )

        connection.close()

    async def __explore_answer_users_ticket(self, call_query: types.CallbackQuery, state: FSMContext) -> None:
        """
        Handler (call-handler) for get id ticket for answer to user.

        :param call_query: Callback Query.
        :param state: FSM.

        :return: None.
        """
        ticket_answer: TicketAnswersToUsers = TicketAnswersToUsers(
            self, self.__admin_id, self.__mysql_data
        )
        await ticket_answer.explore_answer_users_ticket(
            call_query,
            state
        )

    async def __explore_answer_admin_by_ticket(self, call_query: types.CallbackQuery, state: FSMContext) -> None:
        """
        Handler (call-handler) for get id ticket for answer to admin.

        :param call_query: Callback Query.
        :param state: FSM.

        :return: None.
        """
        ticket_answer: TicketAnswersToAdmin = TicketAnswersToAdmin(
            self, self.__admin_id, self.__mysql_data
        )
        await ticket_answer.explore_answer_admin_by_ticket(
            call_query,
            state
        )

    async def __ai_assistance(self, call_query: types.CallbackQuery, state: FSMContext) -> None:
        """
        Handler (callback-handler) for go to the AI-Menu.

        :param call_query: Callback Query.
        :param state: FSM.

        :return: None.
        """
        giga_chat_ai_helper: GigaChatAI = (
            GigaChatAI(
                self, call_query,
                self.__mysql_data,
                self.__admin_id
            )
        )
        await giga_chat_ai_helper.show_info_edit_text(state)

    async def __user_menu_tickets(self, call_query: types.CallbackQuery) -> None:
        """
        Handler (callback-handler) for go to the Tickets-Menu.

        :param call_query: Callback Query.
        :return: None.
        """
        result: tuple = await HandlerDB.get_email_data(call_query.from_user.id)
        if result[0] is True:
            ticket: TicketUserView = TicketUserView(
                self,
                self.__mysql_data
            )
            await ticket.show_user_menu(call_query)
        else:
            var: InlineKeyboardBuilder = await Buttons.get_add_new_email()
            await self.edit_message_text(
                text=f"🤔 <b>{call_query.from_user.first_name}</b>, sorry! But your email address is not in the system."
                     f"\n"
                     f"<em>Add your email address to manage TicketSystem in <b>CWBot UI</b>, click on the button below!"
                     f"</em>.",
                message_id=call_query.message.message_id,
                chat_id=call_query.from_user.id,
                parse_mode="HTML",
                reply_markup=var.as_markup()
            )

    async def __admin_menu_tickets(self, call_query: types.CallbackQuery) -> None:
        """
        Handler (callback-handler) for show tickets to admin.

        :param call_query: Callback Query.
        :return: None.
        """
        ticket: TicketAdminView = TicketAdminView(
            self,
            self.__mysql_data
        )
        await ticket.show_admin_menu(call_query)

    async def __analytic_data(self, call_query: types.CallbackQuery) -> None:
        """
        Handler of the analytic-menu (UI) for admin.

        :param call_query: Callback Query.
        :return: None.
        """
        analytic: Analytic = Analytic(
            self,
            self.__mysql_data,
            call_query
        )
        await analytic.analyse()

    async def __business_handler(self, call_query: types.CallbackQuery) -> None:
        """
        Handler (call-query) for admin (with business) - start main handler.

        :param call_query: Callback Query.
        :return: None.
        """
        handler: BusinessHandler = BusinessHandler(
            self, call_query
        )
        await handler.run()

    async def __get_or_lk_plus(self, call_query: types.CallbackQuery) -> None:
        """
        Get Plus or view (look at) "MY PLUS".

        :param call_query: Callback Query.
        :return: None.
        """
        try:
            result: tuple = await HandlerDB.get_email_data(call_query.from_user.id)
            if result[0] is True or call_query.from_user.id == self.__admin_id:
                checked: tuple = await HandlerDB.check_subscription(call_query)
                if checked[0] is False:
                    var: InlineKeyboardBuilder = await Buttons.get_plus()
                    await self.edit_message_text(
                        chat_id=call_query.from_user.id,
                        text=f"💡 To <b>get a subscription with an invitation discount</b>, <b>click on the button</b> "
                             f"below. If you have "
                             f"any questions or would like to clarify something, write to us: {self.__admin_username}."
                             f"\n\nℹ If you want to <i>test</i> the PLUS (<i>5 days is a trial period</i>), please, "
                             f"write to the admin about it ({self.__admin_username} | help@cwr.su).\n"
                             f"<i>By registering the PLUS, you agree to the terms of use of the service.</i>\n\n"
                             f"#️⃣ My ID: <code>{call_query.from_user.id}</code>",
                        message_id=call_query.message.message_id,
                        reply_markup=var.as_markup(),
                        parse_mode="HTML"
                    )
                elif checked[0] is True:
                    var: InlineKeyboardBuilder = await Buttons.back_on_main()

                    remains = round(await SubOperations.sec_to_days(checked[1]))
                    d = "days"

                    if remains > 1:
                        d = "days"
                    elif remains == 1:
                        d = "day"

                    refund_token: str | bool = await HandlerDB.check_refund_token(call_query)
                    if refund_token:
                        await self.edit_message_text(
                            chat_id=call_query.from_user.id,
                            text=f"🔥 <b>{call_query.from_user.first_name}</b>, the subscription is "
                                 f"still active <b>{remains} {d}</b>.\n\n"
                                 f"🔐 My REFUND Token: <code>{refund_token}</code>.\n"
                                 f"#️⃣ My ID: <code>{call_query.from_user.id}</code>",
                            message_id=call_query.message.message_id,
                            parse_mode="HTML",
                            reply_markup=var.as_markup()
                        )
                    else:
                        await self.edit_message_text(
                            chat_id=call_query.from_user.id,
                            text=f"🔥 <b>{call_query.from_user.first_name}</b>, the subscription is "
                                 f"still active <b>{remains} {d}</b>.\n\n"
                                 f"💡 Ask the admin for your token.\n"
                                 f"#️⃣ My ID: <code>{call_query.from_user.id}</code>",
                            message_id=call_query.message.message_id,
                            parse_mode="HTML",
                            reply_markup=var.as_markup()
                        )
            else:
                var: InlineKeyboardBuilder = await Buttons.get_add_new_email()
                await self.edit_message_text(
                    text=f"🤔 <b>{call_query.from_user.first_name}</b>, sorry! But your email address is not in the "
                         f"system.\n"
                         f"<em>Add your email address to manage your PLUS in <b>CWBot UI</b>, click on the button below"
                         f"!</em>.",
                    message_id=call_query.message.message_id,
                    chat_id=call_query.from_user.id,
                    parse_mode="HTML",
                    reply_markup=var.as_markup()
                )
        except Exception as ex:
            print(ex)

    async def __continue_subscribe_plus(self, call_query: types.CallbackQuery) -> None:
        """
        Continue to subscribe PLUS. Choose method of payment.

        :param call_query: Callback Query.
        :return: None.
        """
        choose: ChooseMethodOfPayment = ChooseMethodOfPayment(
            self, self.__admin_id
        )
        await choose.choose_step1(call_query)

    async def __show_promo_menu_admin(self, call_query: types.CallbackQuery) -> None:
        """
        Show PROMO Menu. | Control ADMIN.

        :param call_query: Callback Query.
        :return: None.
        """
        promo: HandlerEP = HandlerEP(
            self, self.__admin_id
        )
        await promo.show_promo_menu_admin(call_query)

    async def __enter_promo_code(self, call: types.CallbackQuery, state: FSMContext) -> None:
        """
        Func 'ENTER' a promo code from user. | Step 1.

        :param call: CallbackQuery.
        :param state: FSM.

        :return: None.
        """
        checked: tuple = await HandlerDB.check_subscription(call)
        if checked[1] == "ex_sub":
            var: InlineKeyboardBuilder = await Buttons.back_on_main()
            await self.edit_message_text(
                chat_id=call.from_user.id,
                text=f"💖 {call.from_user.first_name}, you have already been a PLUS subscriber ➕.\n"
                     f"💡 The *promo* code is only *for those users who have never used promo* codes in our system.",
                message_id=call.message.message_id,
                reply_markup=var.as_markup(),
                parse_mode="Markdown"
            )
        else:
            promo: HandlerEP = HandlerEP(
                self, self.__admin_id
            )
            await promo.enter_promo(call, state)

    async def __pre_checkout_query(self, pre_checkout_query: types.PreCheckoutQuery) -> None:
        await self.answer_pre_checkout_query(
            pre_checkout_query_id=pre_checkout_query.id, ok=True
        )

    async def __successful_payment(self, message: types.Message) -> None:
        """
        Handler for successful payment.

        :param message: Message from user.
        :return: None.
        """
        await HandlerSP.add_new_record(
            self,
            message,
            self.__admin_id
        )

    async def __refund(self, call: types.CallbackQuery) -> None:
        """
        Refund-menu for admin use / control.

        :param call: Callback Query.
        :return: None.
        """
        var: InlineKeyboardBuilder = await Buttons.sure_refund()
        await self.edit_message_text(
            chat_id=call.from_user.id,
            text=f"⚠️ {call.from_user.first_name}, are you sure?"
                 f"\n\nAfter the star(s) are returned, the *subscription will be disabled*!\n"
                 f"But *user can resume* it at any other time by clicking on *Get PLUS* in main menu.",
            message_id=call.message.message_id,
            parse_mode="Markdown",
            reply_markup=var.as_markup()
        )

    async def __refunding_step1(self, call: types.CallbackQuery, state: FSMContext) -> None:
        """
        Call-Handler for refund stars | Step 1.

        :param call: Callback Query.
        :param state: FSM.

        :return: None.
        """
        refund: Refund = Refund(self)
        await refund.refunding_step1_confirmation(
            call,
            state
        )

    async def __generate_image_for_plus_user(self, call: types.CallbackQuery, state: FSMContext) -> None:
        """
        Generate image for plus-user.

        :param call: Callback Query.
        :param state: FSM.

        :return: None.
        """
        checked: bool | tuple = await HandlerDB.check_subscription(call)
        if checked[0] is False:
            await self.answer_callback_query(
                callback_query_id=call.id,
                text=f"{call.from_user.first_name}, if you want to use this feature 🔥, subscribe to Manager Plus ➕!",
                show_alert=True
            )
        elif checked[0] is True:
            creator: GigaCreator = GigaCreator(
                bot=self
            )
            await creator.get_query(
                call,
                state
            )

    async def __back_on_main(self, call: types.CallbackQuery) -> None:
        """
        Handler for return to main-menu.

        :param call: Callback Query.
        :return: None.
        """
        if call.from_user.id == self.__admin_id:
            var: InlineKeyboardBuilder = await Buttons.get_menu_admin()
            await self.edit_message_text(
                chat_id=call.from_user.id,
                text=f"👑 *{call.from_user.first_name}*,\nYou are in the main menu. Select the desired item below!\n"
                     f"\nUsing the services CWR.SU (CW), you accept all the rules and the agreement. [SEE]("
                     f"https://acdn.cwr.su/src/acdn/Agreement_and_Terms_of_Use_for_the_Manager_CW_Bot_Service.pdf)."
                     f"",
                message_id=call.message.message_id,
                reply_markup=var.as_markup(),
                parse_mode="Markdown"
            )
        else:
            var: InlineKeyboardBuilder = await Buttons.get_menu_without_plus()
            checked: bool | tuple = await HandlerDB.check_subscription(call)
            if checked[0] is False:
                await self.edit_message_text(
                    chat_id=call.from_user.id,
                    text="💡 You are in the main menu. Select the desired item below!\n"
                         f"\nUsing the services CWR.SU (CW), you accept all the rules and the agreement. [SEE]("
                         f"https://acdn.cwr.su/src/acdn/Agreement_and_Terms_of_Use_for_the_Manager_CW_Bot_Service.pdf)."
                         f"",
                    message_id=call.message.message_id,
                    reply_markup=var.as_markup(),
                    parse_mode="Markdown"
                )
            elif checked[0] is True:
                var: InlineKeyboardBuilder = await Buttons.get_menu_with_plus()
                await self.edit_message_text(
                    chat_id=call.from_user.id,
                    text=f"👑 *{call.from_user.first_name}*,\n"
                         f"You are in the main menu. Select the desired item below!\n"
                         f"\nUsing the services CWR.SU (CW), you accept all the rules and the agreement. [SEE]("
                         f"https://acdn.cwr.su/src/acdn/Agreement_and_Terms_of_Use_for_the_Manager_CW_Bot_Service.pdf)."
                         f"",
                    message_id=call.message.message_id,
                    reply_markup=var.as_markup(),
                    parse_mode="Markdown"
                )

    async def __get_main_menu(self, message: types.Message) -> None:
        """
        Handler for go to main-menu.

        :param message: Message.
        :return: None.
        """
        if message.from_user.id == self.__admin_id:
            var: InlineKeyboardBuilder = await Buttons.get_menu_admin()
            await self.send_message(
                chat_id=message.from_user.id,
                text=f"👑 *{message.from_user.first_name}*,\nYou are in the main menu. Select the desired item below!\n"
                     f"\nUsing the services CWR.SU (CW), you accept all the rules and the agreement. [SEE]("
                     f"https://acdn.cwr.su/src/acdn/new_user_agreement_manager_cw_bot.pdf).",
                reply_markup=var.as_markup(),
                parse_mode="Markdown"
            )
        else:
            checked: bool | tuple = await HandlerDB.check_subscription(message)
            if checked[0] is False:
                var: InlineKeyboardBuilder = await Buttons.get_menu_without_plus()
                await self.send_message(
                    chat_id=message.from_user.id,
                    text="💡 You are in the main menu. Select the desired item below!\n"
                         f"\nUsing the services CWR.SU (CW), you accept all the rules and the agreement. [SEE]("
                         f"https://acdn.cwr.su/src/acdn/new_user_agreement_manager_cw_bot.pdf).",
                    reply_markup=var.as_markup(),
                    parse_mode="Markdown"
                )
            elif checked[0] is True:
                var: InlineKeyboardBuilder = await Buttons.get_menu_with_plus()
                await self.send_message(
                    chat_id=message.from_user.id,
                    text=f"👑 *{message.from_user.first_name}*,\n"
                         f"You are in the main menu. Select the desired item below!\n"
                         f"\nUsing the services CWR.SU (CW), you accept all the rules and the agreement. [SEE]("
                         f"https://acdn.cwr.su/src/acdn/new_user_agreement_manager_cw_bot.pdf).",
                    reply_markup=var.as_markup(),
                    parse_mode="Markdown"
                )

    async def __add_new_email(self, call_query: types.CallbackQuery, state: FSMContext) -> None:
        """
        Handler (callback-handler) for add a new EMail.

        :param call_query: Callback Query.
        :param state: FSM.

        :return: None.
        """
        try:
            email: HandlerEM = HandlerEM(self, self.__admin_id)
            await email.add_new_email(call_query, state)

        except Exception as ex:
            print(ex)

    async def __ai_two_in_one_main_menu(self, call_query: types.CallbackQuery) -> None:
        """
        Handler (callback-handler) for explore to AI-menu.

        :param call_query: Callback Query.
        :return: None.
        """
        result: tuple = await HandlerDB.get_email_data(call_query.from_user.id)
        if result[0] is True or call_query.from_user.id == self.__admin_id:
            var: InlineKeyboardBuilder = await Buttons.get_ai_menu()
            await self.edit_message_text(
                chat_id=call_query.from_user.id,
                message_id=call_query.message.message_id,
                text=f"🔥 <b>{call_query.from_user.first_name}</b>, you are in the main menu of the AI functionality.\n"
                     f"⚡ Please select the appropriate item for you to fulfill your task / desire.",
                reply_markup=var.as_markup(),
                parse_mode="HTML"
            )
        else:
            var: InlineKeyboardBuilder = await Buttons.get_add_new_email()
            await self.edit_message_text(
                text=f"🤔 <b>{call_query.from_user.first_name}</b>, sorry! But your email address is not in the system."
                     f"\n"
                     f"<em>Add your email address to manage your AI-Functions in <b>CWBot UI</b>, click on the button "
                     f"below!</em>.",
                message_id=call_query.message.message_id,
                chat_id=call_query.from_user.id,
                parse_mode="HTML",
                reply_markup=var.as_markup()
            )

    async def __business_and_money(self, call_query: types.CallbackQuery) -> None:
        """
        Handler (callback-handler) for explore to BusinessAndMoney-menu.

        :param call_query: Callback Query.
        :return: None.
        """
        var: InlineKeyboardBuilder = await Buttons.get_business_and_money_menu_admin()
        await self.edit_message_text(
            chat_id=call_query.from_user.id,
            message_id=call_query.message.message_id,
            text=f"🔥 <b>{call_query.from_user.first_name}</b>, you are in the main menu of the your Business "
                 f"functionality and money (and promo-datas).\n"
                 f"⚡ Please select the appropriate item for you to fulfill your task / desire.",
            reply_markup=var.as_markup(),
            parse_mode="HTML"
        )

    async def __email_settings_menu(self, call_query: types.CallbackQuery) -> None:
        """
        Menu of EMail Settings for any users and admin.

        :param call_query: Callback Query.
        :return: None.
        """
        result: tuple = await HandlerDB.get_email_data(call_query.from_user.id)
        if result[0] is True or call_query.from_user.id == self.__admin_id:
            email: HandlerEM = HandlerEM(self, self.__admin_id)
            await email.show_email_settings_menu(call_query)
        else:
            var: InlineKeyboardBuilder = await Buttons.get_add_new_email()
            await self.edit_message_text(
                text=f"🤔 <b>{call_query.from_user.first_name}</b>, sorry! But your email address is not in the system."
                     f"\n"
                     f"<em>Add your email address to manage your AI-Functions in <b>CWBot UI</b>, click on the button "
                     f"below!</em>.",
                message_id=call_query.message.message_id,
                chat_id=call_query.from_user.id,
                parse_mode="HTML",
                reply_markup=var.as_markup()
            )

    async def run(self) -> None:
        """
        Run-function Bot.
        """
        try:
            connection: pymysql.Connection = await Connection.get_connection(self.__mysql_data)
            cursor = connection.cursor()
            creator_mysql = CreateTable(connection, cursor)
            creator_mysql.create()

        except Exception as e:
            with open("logs.txt", 'a') as logs:
                logs.write(
                    f"{datetime.datetime.now()} | {e} | "
                    f"The error of database in __init__ of "
                    f"business.py of Manager-Class.\n"
                )

        self.router.message.register(
            self.__get_main_menu, Command(commands=["main", "start"])
        )
        self.router.message.register(
            self.__privacy, Command("privacy")
        )
        self.router.callback_query.register(
            self.__eng_privacy,
            F.data == "eng_privacy_mode"
        )
        self.router.callback_query.register(
            self.__rus_privacy,
            F.data == "rus_privacy_mode"
        )

        self.router.business_message.register(
            self.__answer_to_user,
            F.content_type == ContentType.TEXT
        )

        self.router.callback_query.register(
            self.__ai_assistance,
            F.data == "ai_assistance_request"
        )
        self.router.callback_query.register(
            self.__generate_image_for_plus_user,
            F.data == "kandinsky_generate"
        )
        self.router.callback_query.register(
            self.__ai_two_in_one_main_menu,
            F.data == "ai_two_in_one_main_menu"
        )
        self.router.callback_query.register(
            self.__admin_menu_tickets,
            F.data == "explore_admin_tickets_menu"
        )
        self.router.callback_query.register(
            self.__user_menu_tickets,
            F.data == "explore_user_tickets_menu"
        )

        self.router.callback_query.register(
            self.__explore_answer_users_ticket,
            F.data == "explore_answer_to_user"
        )
        self.router.callback_query.register(
            self.__explore_answer_admin_by_ticket,
            F.data == "explore_answer_to_admin"
        )

        self.router.callback_query.register(
            self.__explore_show_users_ticket,
            F.data == "explore_show_ticket_by_id"
        )

        self.router.callback_query.register(
            self.__business_and_money,
            F.data == "business_and_money"
        )
        self.router.callback_query.register(
            self.__analytic_data,
            F.data == "analytic_data"
        )
        self.router.callback_query.register(
            self.__business_handler,
            F.data == "business_handler"
        )
        self.router.callback_query.register(
            self.__email_settings_menu,
            F.data == "email_settings_menu"
        )
        self.router.callback_query.register(
            self.__refund,
            F.data == "start_refund"
        )
        self.router.callback_query.register(
            self.__refunding_step1,
            F.data == "refund"
        )
        self.router.callback_query.register(
            self.__show_promo_menu_admin,
            F.data == "show_menu_promo_admin"
        )

        self.router.callback_query.register(
            self.__get_or_lk_plus,
            F.data == "get_or_lk_plus"
        )
        self.router.callback_query.register(
            self.__continue_subscribe_plus,
            F.data == "continue_subscribe_plus"
        )
        self.router.callback_query.register(
            self.__enter_promo_code,
            F.data == "continue_subscribe_plus_with_promo"
        )

        self.router.callback_query.register(
            self.__back_on_main,
            F.data == "back_on_main"
        )

        self.router.callback_query.register(
            self.__add_new_email,
            F.data == "add_new_email"
        )

        self.router.pre_checkout_query.register(
            self.__pre_checkout_query,
            F.func(lambda query: True)
        )
        self.router.message.register(
            self.__successful_payment,
            F.content_type == ContentType.SUCCESSFUL_PAYMENT
        )
        self.router.message.register(
            self.__standard_message,
            F.content_type == ContentType.TEXT
        )

        self.__dp.include_routers(
            router,
            router_ai_img,
            router_business,
            router_chat_ai,
            router_handler_em,
            router_refund,
            router_promo,
            router_send_invoice,
            self.router
        )
        await self.__dp.start_polling(self)


def get_data(file_path="bot.json") -> dict:
    """
    Get data of the Alex's Manager Bot.

    :param file_path: File Path of JSON-API-keys for Bot.

    :return: Dict with data.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        data: dict = json.load(file)

        dct = dict()
        dct["BOT_TOKEN"] = data["BOT_TOKEN"]
        dct["business_connection_id"] = data["business_connection"]["id"]
        dct["business_connection_is_enabled"] = data["business_connection"]["is_enabled"]
        dct["ADMIN_ID"] = data["business_connection"]["user"]["id"]
        dct["ADMIN_USERNAME"] = data["business_connection"]["user"]["username"]
        dct["ADMIN_EMAIL_FOR_CHECK"] = data["EMAIL_DATA"]["ADMIN_EMAIL"]

        dct["MYSQL"] = data["MYSQL"]

        dct["GIGACHAT"] = data["GIGACHAT"]

        dct["BUSINESS_HANDLER"] = data["BUSINESS_HANDLER"]

        return dct


async def run() -> None:
    """
    Run Function of the main-file.

    :return: None.
    """
    try:
        data: dict = get_data()
        if data["business_connection_is_enabled"] == "True" and len(data["ADMIN_EMAIL_FOR_CHECK"]) >= 7:
            bot: Manager = Manager(data["BOT_TOKEN"], data["business_connection_id"],
                                   data["ADMIN_ID"], data["MYSQL"], data["GIGACHAT"], data["ADMIN_USERNAME"])
            await bot.run()

        else:
            print("Business Connection isn't enabled!")
    except Exception as ex:
        with open("logs.txt", 'a') as logs:
            logs.write(f"\n{datetime.datetime.now()} | {ex} | The error in run-function of "
                       f"business.py.\n")
        print(f"The Error (ex-run-func): {ex}")
