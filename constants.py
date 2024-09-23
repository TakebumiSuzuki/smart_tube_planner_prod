from vertexai.generative_models import HarmCategory, HarmBlockThreshold, SafetySetting

GC_PROJECT_NAME = 'arvato-developments'
LOCATION = 'us-central1'


YOUTUBE_API_KEY = 'YOUTUBE_API_KEY'
GEMINI_API_KEY = 'GEMINI_API_KEY'
GEMINI_MODEL_NAME = 'models/gemini-1.5-pro-latest'

MAX_TOP_VIDEOS = 7

TAB_TITLE = 'SmartTube Planner'
TITLE = 'SmartTube Planner'
TITLE_TOP7 = '### **The most viewed video in the past year**  \n'
INPUT_HOLDER = 'Enter YouTube channel url.'
NOW_PROCESSING = 'Thinking...'
AI = 'AI'
# USER = 'USER' 使われていない


# PROMPT_TEMPLATE = """You are an expert YouTube content consultant. Below is a list of the most viewed videos from a specific channel over the past year. Based on this list, please generate 10 sets of video topic ideas with some title ideas for each idea, in the same language as the provided list, that are likely to attract a large audience for this channel in the future.
# 1. Always start with the following line: "### **10 Sets of YouTube Video Ideas Based on Your Popular Videos:**\n"
# 2. For all the rest, you have to write your topic ideas and title ideas in exactly the same language as the provided list.
# Here is the list of videos:
# """

PROMPT_TEMPLATE = """You are an expert YouTube content consultant. Below is a list of the most viewed videos from a specific channel over the past year. Based on this list, please generate 10 sets of abstract video topic ideas for each idea, in the same language as the provided list, that are likely to attract a large audience for this channel in the future.
1. Always start with the following line: "### **10 Sets of YouTube Video Ideas Based on Your Popular Videos:**\n"
2. For all the rest, you have to write your abstract topic ideas in exactly the same language as the provided list.
Here is the list of videos:
"""


CSS = """
    <style>
        header {visibility: hidden;}
        div[class^='block-container'] { padding-top: 2rem; }
        h1 {
            text-align: center;
        }
    </style>
    """


GENERATION_CONFIG = {"temperature": 0.8}

SAFTY_SETTINGS = [
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        method=SafetySetting.HarmBlockMethod.SEVERITY,
        threshold=HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HARASSMENT,
        method=SafetySetting.HarmBlockMethod.SEVERITY,
        threshold=HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        method=SafetySetting.HarmBlockMethod.SEVERITY,
        threshold=HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
    SafetySetting(
        category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        method=SafetySetting.HarmBlockMethod.SEVERITY,
        threshold=HarmBlockThreshold.BLOCK_ONLY_HIGH,
    ),
]