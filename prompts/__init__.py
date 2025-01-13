from .constants import TEXT_STYLES, BASE_PROMPT
from .formal_prompts import FORMAL_PROMPT
from .business_prompts import BUSINESS_PROMPT
from .superior_prompts import SUPERIOR_PROMPT
from .comfort_prompts import COMFORT_CASUAL_PROMPT, COMFORT_FORMAL_PROMPT
from .apology_prompts import APOLOGY_PROMPT
from .kindergarten_prompts import KINDERGARTEN_TEACHER_PROMPT, KINDERGARTEN_PARENT_PROMPT
from .refund_prompts import REFUND_PROMPT
from .professor_prompts import PROFESSOR_PROFESSOR_PROMPT, PROFESSOR_STUDENT_PROMPT

STYLE_PROMPTS = {
    'formal': FORMAL_PROMPT,
    'business': BUSINESS_PROMPT,
    'apology': APOLOGY_PROMPT,
    'superior': SUPERIOR_PROMPT,
    'comfort_casual': COMFORT_CASUAL_PROMPT,
    'comfort_formal': COMFORT_FORMAL_PROMPT,
    'professor_professor': PROFESSOR_PROFESSOR_PROMPT,
    'professor_student': PROFESSOR_STUDENT_PROMPT,
    'refund': REFUND_PROMPT,
    'kindergarten_teacher': KINDERGARTEN_TEACHER_PROMPT,
    'kindergarten_parent': KINDERGARTEN_PARENT_PROMPT
}

def get_prompt(style):
    """필요한 스타일의 프롬프트만 로드"""
    if style in STYLE_PROMPTS:
        return f"{BASE_PROMPT}\n{STYLE_PROMPTS[style]}"
    return BASE_PROMPT

__all__ = ['TEXT_STYLES', 'get_prompt']
