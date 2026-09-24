import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler_masks = logging.FileHandler("logs/masks.log", mode="w", encoding="UTF-8")
file_formatter_masks = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler_masks.setFormatter(file_formatter_masks)
logger.addHandler(file_handler_masks)


def get_mask_card_number(namber_card: str) -> str:
    if len(namber_card) == 16:
        namber_card_1 = namber_card[0:4] + " " + namber_card[4:6] + "** **** " + namber_card[12:]
        logger.info("Карта замаскирована")
    else:
        namber_card_1 = "Ошибка данных"
        logger.error("Ошибка данных")

    return namber_card_1


def get_mask_account(accaund_namber: str) -> str:
    if len(accaund_namber) == 20:
        accaund_namber_1 = "**" + accaund_namber[16:]
        logger.debug("Счет замаскирован")
    else:
        accaund_namber_1 = "Ошибка данных"
        logger.error("Ошибка данных")

    return accaund_namber_1
