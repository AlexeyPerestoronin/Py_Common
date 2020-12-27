import common
import common.log.const as const

# brief: a class implements logging logic
class Logger:
    __recipients = { "console" : { const.METHODS : [print], const.COUNTER : 0 } }

    # brief: class constructor method
    # param: init_message - message that will log at class-instance creating
    # param: close_message - message that will log at class-instance destroyed (may be callable object)
    # param: recipient - access-key of target log-recipient
    # param: is_with_new_line - flag: if true - each new message will be logged with new line; if false - vise versa
    def __init__(self, init_message=None, close_message=None, *, recipient="console", is_with_new_line=False):
        self.__init_message = init_message
        self.__close_message = close_message
        self.__recipient = recipient
        self.__is_with_new_line = is_with_new_line
        if self.__init_message:
            for method in Logger.__recipients[self.__recipient][const.METHODS]:
                method(self.__FormatMessage(self.__init_message))

    def __enter__(self):
        Logger.__recipients[self.__recipient][const.COUNTER] += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Logger.__recipients[self.__recipient][const.COUNTER] -= 1
        if self.__close_message:
            for method in Logger.__recipients[self.__recipient][const.METHODS]:
                method(self.__FormatMessage(self.__close_message() if callable(self.__close_message) else self.__close_message))

    def __GetIndent(self):
        return "".join([' ' for i in range(Logger.__recipients[self.__recipient][const.COUNTER] * 4)])

    def __FormatMessage(self, message,*, type=""):
        return "{}{}{}{}".format("\n" if self.__is_with_new_line else "", self.__GetIndent(), type, message)

    # brief: registers new log-recipient
    # param: recipient_name - access-key for new registered recipient
    # param: methods - a list or not of the methods which will be called for logging
    # note 1: each method must requests one str-param for to be called
    @staticmethod
    def RegisterRecipient(recipient_name, methods):
        if not common.IsIterable(methods):
            methods = [methods]
        for method in methods:
            if not callable(method):
                raise "all methods must be calable"
        Logger.__recipients[recipient_name] = {}
        Logger.__recipients[recipient_name][const.METHODS] = methods
        Logger.__recipients[recipient_name][const.COUNTER] = 0

    # brief: log show-message
    # param: message - target message for logging
    def LogMessage(self, message):
        for method in Logger.__recipients[self.__recipient][const.METHODS]:
            method(self.__FormatMessage(message))

    # brief: log info-message
    # param: message - target message for logging
    def LogInfo(self, message):
        for method in Logger.__recipients[self.__recipient][const.METHODS]:
            method(self.__FormatMessage(message, type="[ INFO ] "))

    # brief: log result-message
    # param: message - target message for logging
    def LogResult(self, message):
        for method in Logger.__recipients[self.__recipient][const.METHODS]:
            method(self.__FormatMessage(message, type="[RESULT] "))

    # brief: log warning-message
    # param: message - target message for logging
    def LogWarning(self, message):
        for method in Logger.__recipients[self.__recipient][const.METHODS]:
            method(self.__FormatMessage(message, type="[ WARN ] "))

    # brief: log error-message
    # param: message - target message for logging
    def LogError(self, message):
        for method in Logger.__recipients[self.__recipient][const.METHODS]:
            method(self.__FormatMessage(message, type="[ERROR ] "))
