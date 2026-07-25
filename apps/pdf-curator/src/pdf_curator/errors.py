"""Domain errors raised by the curator pipeline."""


class PdfCuratorError(Exception):
    """Base error for user-visible pipeline failures."""


class ValidationError(PdfCuratorError):
    """Raised when source provenance or output invariants are invalid."""


class ConfigurationError(PdfCuratorError):
    """Raised when a required runtime setting is missing."""
