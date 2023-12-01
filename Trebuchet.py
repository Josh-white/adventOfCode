import string


def get_calibration_value(text_document) -> int:
    split_document = text_document.split('\n')

    return len(split_document)

