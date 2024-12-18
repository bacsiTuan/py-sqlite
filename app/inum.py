#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum
from abc import ABCMeta


class EnumInterface(enum.Enum):
    __metaclass__ = ABCMeta

    # magic methods for argparse compatibility

    def __str__(self):
        return self.name.lower()

    def __repr__(self):
        return str(self)

    @classmethod
    def argparse(cls, s):
        try:
            return cls[s.upper()]
        except KeyError:
            return s

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class HTTPStatusCode(enum.Enum):
    # Informational group
    INFORMATIONAL_CONTINUE = 100
    INFORMATIONAL_SWITCHING_PROTOCOLS = 101
    # Success group
    SUCCESS_OK = 200
    SUCCESS_CREATED = 201
    SUCCESS_ACCEPTED = 202
    SUCCESS_NON_AUTORIATIVE_INFORMATION = 203
    SUCCESS_NO_CONTENT = 204
    SUCCESS_RESET_CONTENT = 205
    SUCCESS_PARTIAL_CONTENT = 206
    # Redirect group
    REDIRECT_MULTIPLE_CHOICES = 300
    REDIRECT_MOVED_PERMANENTLY = 301
    REDIRECT_FOUND = 302
    REDIRECT_SEE_OTHER = 303
    REDIRECT_NOT_MODIFIED = 304
    REDIRECT_USE_PROXY = 305
    REDIRECT_SWITCH_PROXY = 306
    REDIRECT_TEMPORARY_REDIRECT = 307
    # Client error group
    CLIENT_ERROR_BAD_REQUEST = 400
    CLIENT_ERROR_UNAUTHORIZED = 401
    CLIENT_ERROR_PAYMENT_REQUIRED = 402
    CLIENT_ERROR_FORBIDDEN = 403
    CLIENT_ERROR_NOT_FOUND = 404
    CLIENT_ERROR_METHOD_NOT_ALLOWED = 405
    CLIENT_ERROR_NOT_ACCEPTABLE = 406
    CLIENT_ERROR_PROXY_AUTHENTICATION_REQUIRED = 407
    CLIENT_ERROR_REQUEST_TIME_OUT = 408
    CLIENT_ERROR_CONFLICT = 409
    CLIENT_ERROR_GONE = 410
    CLIENT_ERROR_LENGTH_REQUIRED = 411
    CLIENT_ERROR_PRECONDITION_FAILED = 412
    CLIENT_ERROR_PAYMENT_TOO_LARGE = 413
    CLIENT_ERROR_URI_TOO_LONG = 414
    CLIENT_ERROR_UNSUPPORTED_MEDIA_TYPE = 415
    CLIENT_ERROR_RANGE_NOT_SATISFIABLE = 416
    CLIENT_ERROR_EXPECTATION_FAILED = 417
    # Server error group
    SERVER_ERROR_INTERNAL_SERVER_ERROR = 500
    SERVER_ERROR_NOT_IMPLEMENTED = 501
    SERVER_ERROR_BAD_GATEWAY = 502
    SERVER_ERROR_SERVICE_UNAVAILABLE = 503
    SERVER_ERROR_GATEWAY_TIMEOUT = 504
    SERVER_ERROR_HTTP_VERSION_NOT_SUPPORTED = 505


class Status(EnumInterface):
    DEACTIVATE = 1
    ACTIVATE = 2


class Platform(EnumInterface):
    OPENAI = 1
    GOOGLE = 2
