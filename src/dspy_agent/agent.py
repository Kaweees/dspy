import dspy

from .utils import get_token

MODEL = "gemini/gemini-2.5-pro-preview-03-25"
API_KEY = get_token("GEMINI_API_KEY")

lm = dspy.LM(MODEL, api_key=API_KEY)
dspy.configure(lm=lm)
