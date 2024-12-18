#!/usr/bin/env python
# -*- coding: utf-8 -*-
error_codes = {
    1000: "Error_code_1000",
    1001: "Service ID does not exists",
    1002: "Resource does not exists",
    1003: "Resource Code is required",
    1004: "Resource Code is already exists",
    404: "Not Found",
}

# API response code
UNKNOWN_ERROR = 1
NO_QUOTA_LEFT = 2
API_KEY_NOT_FOUND = 3
INVALID_MODEL = 4
INVALID_PROMPT = 5
INVALID_FILE = 6
INPUT_TOKEN_LIMIT_EXCEEDED = 7
INVALID_SERVER_ID = 8
UNAUTHORIZED = 9
BLOCKED_BY_AI_SERVER = 10
