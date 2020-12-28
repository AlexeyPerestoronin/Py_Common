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
    # param: is_with_new_line - flag: if true - each new message will be logged with new line; if false - vise versa
    def __init__(self, init_message=None, close_message=None, *, recipient=None, method=None, is_with_new_line=False):
        self.__init_message = init_message
        self.__close_message = close_message
        self.__recipient = "console" if not recipient else self.RegisterRecipient(recipient, method, is_with_new_line)
        if self.__init_message:
            for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
                message = self.__FormatMessage(self.__init_message)
                method("\n" + message if is_new_line else message)

    def __enter__(self):
        Logger.__recipients[self.__recipient][const.COUNTER] += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        Logger.__recipients[self.__recipient][const.COUNTER] -= 1
        if self.__close_message:
            for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
                message = self.__FormatMessage(self.__close_message() if callable(self.__close_message) else self.__close_message)
                method("\n" + message if is_new_line else message)

    def __GetIndent(self):
        return "".join([' ' for i in range(Logger.__recipients[self.__recipient][const.COUNTER] * 4)])

    def __FormatMessage(self, message,*, type=""):
        return "{}{}{}".format(self.__GetIndent(), type, message)

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
        Logger.__recipients[recipient_name] = {const.METHODS : [method, is_new_line], const.COUNTER : 0}
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

    # brief: log show-message
    # param: no_tag_message - target message for logging
    def LogMessage(self, no_tag_message):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message)
            method("\n" + message if is_new_line else message)

    # brief: log info-message
    # param: no_tag_message - target message for logging
    def LogInfo(self, no_tag_message):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message, type="[ INFO ] ")
            method("\n" + message if is_new_line else message)

    # brief: log result-message
    # param: no_tag_message - target message for logging
    def LogResult(self, no_tag_message):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message, type="[RESULT] ")
            method("\n" + message if is_new_line else message)

    # brief: log warning-message
    # param: no_tag_message - target message for logging
    def LogWarning(self, no_tag_message):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message, type="[ WARN ] ")
            method("\n" + message if is_new_line else message)

    # brief: log error-message
    # param: no_tag_message - target message for logging
    def LogError(self, no_tag_message):
        for method, is_new_line in Logger.__recipients[self.__recipient][const.METHODS]:
            message = self.__FormatMessage(no_tag_message, type="[ERROR ] ")
            method("\n" + message if is_new_line else message)
