def generateResponse(message):
    return {
        "status": "200",
        "data": message
    }


def generateError(code, message):
    return (
        {
            "status": code,
            "error": message
        },
        code
    )