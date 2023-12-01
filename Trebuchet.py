def get_calibration_value(text_document: str) -> int:
    split_document: list[str] = text_document.split('\n')
    sum_of_values: int = 0
    for text_line in split_document:
        numbers_from_string: list[int] = [int(i) for i in text_line if i.isdigit()]
        if len(numbers_from_string) >= 1:
            first_number = numbers_from_string[0]
            last_number = numbers_from_string[-1]
            combined_number = int(str(first_number) + str(last_number))
            sum_of_values += combined_number
    return sum_of_values
