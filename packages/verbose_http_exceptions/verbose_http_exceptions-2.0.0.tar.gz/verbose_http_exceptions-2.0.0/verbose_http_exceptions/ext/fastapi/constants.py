from typing import Any

BASE_VERBOSE_HTTP_VALIDATION_ERROR = {
    "properties": {
        "code": {
            "title": "Error code",
            "type": "string",
            "example": "multiple",
            "description": "Error code represented as string to display on frontend.",
        },
        "type": {
            "title": "Error type",
            "type": "string",
            "example": "multiple",
            "description": (
                "Error type - covariant of error code, "
                "represented as string to display on frontend."
            ),
        },
        "message": {
            "title": "Message",
            "type": "string",
            "example": "Multiple errors ocurred. Please check list for nested_errors.",
            "description": "Error message to display on frontend.",
        },
        "attr": {
            "title": "Attribute name",
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "example": None,
            "description": (
                "Attribute name - additional context to to clarify the object of action."
            ),
        },
        "location": {
            "title": "Location of attribute",
            "anyOf": [{"type": "string"}, {"type": "null"}],
            "example": None,
            "description": (
                "Location of attribute - additional context to to clarify the place of action."
            ),
        },
    },
    "title": "RequestValidationHTTPExceptionWithNestedErrors",
    "description": "Element of request validation to use in VerboseHTTPValidationError.",
    "type": "object",
    "required": ["code", "type", "message"],
}
VERBOSE_HTTP_VALIDATION_ERROR = {
    "allOf": [
        {"$ref": "#/components/schemas/RequestValidationHTTPExceptionWithNestedErrors"},
        {
            "properties": {
                "nested_errors": {
                    "items": {
                        "$ref": (
                            "#/components/schemas/RequestValidationHTTPExceptionWithNestedErrors"
                        ),
                    },
                    "type": "array",
                    "title": "Specific errors of request validation",
                    "description": (
                        "List of errors, which specify all request errors from user request."
                    ),
                    "example": [
                        {
                            "code": "validation_error",
                            "type": "literal_error",
                            "message": (
                                "Input should be 1, 2 or 3 "
                                "(this is example only. Not real message)"
                            ),
                            "attr": "a",
                            "location": "query",
                        },
                        {
                            "code": "validation_error",
                            "type": "literal_error",
                            "message": (
                                "Input should be 25 (this is example only. Not real message)"
                            ),
                            "attr": "b",
                            "location": "query",
                        },
                    ],
                },
            },
        },
    ],
    "title": "VerboseHTTPValidationError",
    "description": "Override of FastAPI HTTPValidationError in 422 status code.",
    "type": "object",
}


INFO_START_DIGIT = 1
SUCCESS_START_DIGIT = 2
REDIRECT_START_DIGIT = 3
CLIENT_ERROR_START_DIGIT = 4
SERVER_ERROR_START_DIGIT = 5
ERROR_MAPPING: dict[int, dict[str, Any]] = {
    INFO_START_DIGIT: {
        "code": "info",
        "type": "info",
        "location": None,
        "attr": None,
    },
    SUCCESS_START_DIGIT: {
        "code": "success",
        "type": "success",
        "location": None,
        "attr": None,
    },
    REDIRECT_START_DIGIT: {
        "code": "redirect",
        "type": "redirect",
        "location": None,
        "attr": None,
    },
    CLIENT_ERROR_START_DIGIT: {
        "code": "client_error",
        "type": "client_error",
        "location": None,
        "attr": None,
    },
    SERVER_ERROR_START_DIGIT: {
        "code": "server_error",
        "type": "server_error",
        "location": None,
        "attr": None,
    },
}
