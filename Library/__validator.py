class Validation:

    @staticmethod
    def text_empty_string_or_white_space(text: str, message: str):
        if len(text.strip()) == 0:
            raise ValueError(message)

    @staticmethod
    def number_is_less_than_0(number: float, message: str):
        if number < 0:
            raise ValueError(message)

    @staticmethod
    def item_duplicity(searched_parameter, list_with_objects, message: str):
        if any(searched_parameter == object.searched_parameter for object in list_with_objects):
            raise Exception(message)

    @staticmethod
    def correct_type(type_: str, correct_types_: dict, message: str):
        if type_ not in correct_types_:
            raise Exception(message)

    @staticmethod
    def item_not_found(item: object, message: str):
        if not item:
            raise Exception(message)
