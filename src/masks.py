def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    nums = ""
    coding_card_number = str(card_number)
    for num in coding_card_number:
        if num == " ":
            continue
        else:
            nums += num
    start_of_counting = nums[:6]
    end_of_counting = nums[-4:]
    middle_of_counting = len(nums) - 10
    coding_middle = "*" * middle_of_counting
    masked_count = start_of_counting + coding_middle + end_of_counting
    groups_of_str = []
    for numb in range(0, len(masked_count), 4):
        groups_of_str.append(masked_count[numb : numb + 4])
    return " ".join(groups_of_str)


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счёта."""
    digits = ""
    account_str = str(account_number)
    for char in account_str:
        if char == " ":
            continue
        digits += char

    last_six = digits[-6:] if len(digits) >= 6 else digits

    prefix = "*" * len(last_six[:2])
    suffix = last_six[-4:]

    return prefix + suffix
