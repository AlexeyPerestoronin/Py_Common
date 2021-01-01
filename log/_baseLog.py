import common
import common.log.const as const

# brief: a class implements logging logic
class Logger:
    __recipients = {
        "console" : {
            const.METHODS : [
                # list of two-elements-lists
                [
                    print, # callable method for logging of target log-message
                    False  # flag: if true - each next log-message will be logged with new line; if false - vise versa
                ]
            ],
            const.COUNTER : 0
        }
    }

    # brief: class constructor method
    # param: init_message - message that will log at class-instance creating
    # param: close_message - message that will log at class-instance destroyed (may be callable object)
    # param: recipient - access-key of target log-recipient
    def __init__(self, init_message=None, close_message=None, *, recipient=None):
        self.__init_message = init_message
        self.__close_message = close_message
        self.__recipient = recipient if recipient else "console"
        if self.__init_message:
            message, format_args = Logger.__SplitMessageFromItsArgs(self.__init_message)
            for log_method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
                message = self.__FormatMessage(message.format(*format_args))
                log_method("\n" + message if is_new_line else message)

    def __enter__(self):
        Logger.__recipients[self.__recipient][const.COUNTER] += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Logger.__recipients[self.__recipient][const.COUNTER] -= 1
        if self.__close_message:
            message, format_args = Logger.__SplitMessageFromItsArgs(self.__close_message)
            result_message = None
            if callable(message):
                result_message = message().format(*format_args)
            else:
                result_message = message.format(*format_args)
            for log_method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
                message_for_log = self.__FormatMessage(result_message)
                if is_new_line:
                    message_for_log = '\n' + message_for_log
                log_method(message_for_log)

    def __GetIndent(self):
        return "".join([' ' for i in range(Logger.__recipients[self.__recipient][const.COUNTER] * 4)])

    def __FormatMessage(self, message,*, type=""):
        return "{}{}{}".format(self.__GetIndent(), type, message)

    # brief: splits message shows like [message, arg1, arg2, ...] to the message and args-list
    # message_and_args: target message to split by args
    # return: cortege with first element is message and second is list-args for formating of the message
    @staticmethod
    def __SplitMessageFromItsArgs(message_and_args):
        result = None
        if isinstance(message_and_args, str):
            result = (message_and_args, [])
        elif isinstance(message_and_args, list):
            result = (message_and_args[0], message_and_args[1:])
        else:
            raise "input parameter must be str-type or list-type"
        return result

    # brief: log show-message
    # param: no_tag_message - target message for logging
    # param: *format_args - list of arguments for formmat target message
    def LogMessage(self, no_tag_message, *format_args):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message.format(*format_args))
            method("\n" + message if is_new_line else message)

    # brief: log info-message
    # param: no_tag_message - target message for logging
    # param: *format_args - list of arguments for formmat target message
    def LogInfo(self, no_tag_message, *format_args):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message.format(*format_args), type="[ INFO ] ")
            method("\n" + message if is_new_line else message)

    # brief: log result-message
    # param: no_tag_message - target message for logging
    # param: *format_args - list of arguments for formmat target message
    def LogResult(self, no_tag_message, *format_args):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message.format(*format_args), type="[RESULT] ")
            method("\n" + message if is_new_line else message)

    # brief: log warning-message
    # param: no_tag_message - target message for logging
    # param: *format_args - list of arguments for formmat target message
    def LogWarning(self, no_tag_message, *format_args):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message.format(*format_args), type="[ WARN ] ")
            method("\n" + message if is_new_line else message)

    # brief: log error-message
    # param: no_tag_message - target message for logging
    # param: *format_args - list of arguments for formmat target message
    def LogError(self, no_tag_message, *format_args):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message.format(*format_args), type="[ERROR ] ")
            method("\n" + message if is_new_line else message)

    # brief: registers new log-recipient
    # param: recipient_name - access-key for new registered recipient
    # param: method - a method which will be called for logging
    # param: is_new_line - flag: if true - each log-message will be logged with new line; if false - vise versa
    # return: name of registered recipients
    @staticmethod
    def RegisterRecipient(recipient_name, method, is_new_line=False):
        if recipient_name in Logger.__recipients.keys():
            raise "this class-method registers only new recipient"
        if not callable(method):
            raise "method must be calable"
        Logger.__recipients[recipient_name] = {const.METHODS : [[method, is_new_line]], const.COUNTER : 0}
        return recipient_name

    # brief: registers new method for existent log-recipient
    # param: recipient_name - access-key for new registered recipient
    # param: method - a method which will be called for logging
    # param: is_new_line - flag: if true - each log-message will be logged with new line; if false - vise versa
    # return: name of recipient for which new method was be registered
    @staticmethod
    def RegisterMethod(recipient_name, method, is_new_line=False):
        if recipient_name not in Logger.__recipients.keys():
            raise "this class-method registers new method only for existent recipients"
        if not callable(method):
            raise "registers method must be calable"
        Logger.__recipients[recipient_name][const.METHODS].append([method, is_new_line])
        return recipient_name
