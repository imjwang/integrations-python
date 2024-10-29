# src/restackio/integrations/gemini/__init__.py
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .functions.generate_content import gemini_generate_content, GeminiGenerateContentInput
from .service import GeminiServiceOptions, GeminiServiceInput, gemini_service

__all__ = [
    'gemini_generate_content',
    'GeminiGenerateContentInput',
    'GeminiServiceOptions',
    'GeminiServiceInput',
    'gemini_service'
]