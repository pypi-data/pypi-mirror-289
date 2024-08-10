class DreamError(Exception):
    pass


class AuthenticationError(DreamError):
    pass


class CreateTaskError(DreamError):
    pass


class CheckTaskError(DreamError):
    pass


class GetStylesError(DreamError):
    pass


class GenerationTimeoutError(DreamError, TimeoutError):
    pass
