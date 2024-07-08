from fmmodel.fm_visibility import FMVisibility


class StrToEnumConverter:

    def __init__(self):
        pass

    @staticmethod
    def visibility_str_to_enum(s: str):
        if s == 'public':
            return FMVisibility.PUBLIC
        elif s == 'private':
            return FMVisibility.PRIVATE
        elif s == 'protected':
            return FMVisibility.PROTECTED
        elif s == 'package':
            return FMVisibility.PACKAGE
        elif s == 'Unspecified':
            return FMVisibility.UNSPECIFIED
        else:
            print('Unexpected value for visibility. {} is not valid value'.format(s))
            exit(-1)

