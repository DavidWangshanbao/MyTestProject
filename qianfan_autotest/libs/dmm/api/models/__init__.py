# coding=utf-8
from jsonobject import JsonObject, StringProperty, BooleanProperty, FloatProperty


class BLogin(JsonObject):
    """
     relative to BLogin.java in dmm-web
    """
    accountNo = StringProperty(exclude_if_none=True)
    password = StringProperty(exclude_if_none=True)
    captcha = StringProperty(exclude_if_none=True)
    captchaId = StringProperty(exclude_if_none=True)


class BAccount(JsonObject):
    """
    relative to BAccount.java in dmm-web
    """
    id = StringProperty(exclude_if_none=True)
    name = StringProperty(exclude_if_none=True)
    status = StringProperty(exclude_if_none=True)
    verified = BooleanProperty(exclude_if_none=True)
    isDefault = BooleanProperty(exclude_if_none=True)
    version = FloatProperty(exclude_if_none=True)
    settledNames = StringProperty(exclude_if_none=True)
