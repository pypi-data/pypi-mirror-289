"""Module of the FSM-classes."""
from aiogram.fsm.state import State, StatesGroup


class GetTicketDataByIDTCK(StatesGroup):
    """Get Ticket Data By Ticket ID."""
    id_ticket: State = State()


class GetDataForSendNewTicket(StatesGroup):
    """Get Ticket-Data for send new ticket."""
    ticket_data: State = State()


class GetTicketDataForAnswerToUser(StatesGroup):
    """Get Ticket-Data for answer to user."""
    ticket_data: State = State()


class GetTicketDataForAnswerToAdmin(StatesGroup):
    """Get Ticket-Data for answer to the admin."""
    ticket_data: State = State()


class BusinessHandlerThanksFunctions(StatesGroup):
    """Get BH-Data for thanks-func."""
    only_text: State = State()
    only_sticker: State = State()
    message_and_sticker_step1_message: State = State()
    message_and_sticker_step2_sticker: State = State()


class BusinessHandlerCongratulationFunctions(StatesGroup):
    """Get BH-Data for congratulation-func."""
    only_text: State = State()
    only_sticker: State = State()
    message_and_sticker_step1_message: State = State()
    message_and_sticker_step2_sticker: State = State()


class BusinessHandlerProblemWithBotFunctions(StatesGroup):
    """Get BH-Data for PWB-func."""
    only_text: State = State()
    only_sticker: State = State()
    message_and_sticker_step1_message: State = State()
    message_and_sticker_step2_sticker: State = State()


class GigaImage(StatesGroup):
    """Get request from user to AI-Generate-IMG."""
    request: State = State()


class ProcessGigaChatAI(StatesGroup):
    """Get request from user to AI-Chat."""
    request: State = State()


class ProcessEditingEmailAfterConfirmation(StatesGroup):
    """Get new email from user / admin."""
    new_email: State = State()


class ProcessAddNewEmail(StatesGroup):
    """Get new email to add in DB / Account Manager CW Bot."""
    new_email: State = State()


class ProcessEnterTheCodeForAddNewEMailForVerifyEmail(StatesGroup):
    """Get verify-code for email-confirmation."""
    code: State = State()


class ProcessEnteringPromoST1(StatesGroup):
    """Get promo-data | Step 1."""
    promo: State = State()


class ProcessAddNewPromoPromoST2(StatesGroup):
    """Add new promo-data | Step 2."""
    promo: State = State()


class ProcessDeletePromoPromoST2(StatesGroup):
    """Delete new promo-data | Step 2."""
    promo: State = State()


class ProcessRefundingGetREFTokenST1(StatesGroup):
    """Get REFUND-Token | Step 1."""
    token: State = State()


class ProcessEmergencyRefundingGetREFTokenST1(StatesGroup):
    """Get user_id for refund (emergency-refund) | Step 1."""
    user_id: State = State()
