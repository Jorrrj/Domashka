def get_mask_card_number(namber_card: str) -> str:
    if len(namber_card) == 16:
        namber_card_1 = namber_card[0:4] + " " + namber_card[4:6] + "** **** " + namber_card[12:]
    else:
        namber_card_1 = "Ошибка данных"

    return namber_card_1


def get_mask_account(accaund_namber: str) -> str:
    if len(accaund_namber) == 20:
        accaund_namber_1 = "**" + accaund_namber[16:]
    else:
        accaund_namber_1 = "Ошибка данных"

    return accaund_namber_1


# if __name__ == "__main__":
#     print(get_mask_account("11111111111111111111"))
