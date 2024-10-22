import os
import json
from utils.get_text import get_text_from_audio, get_text_from_video, get_text_from_image
from utils.generation_conversation import generate_conversation

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\\Current Project\Voice Chabot UK\\audio\\gcp-creditial.json'

# Load prompt
with open('config/prompts.json', 'r') as f:
    prompts = json.load(f)

def find_prompt_by_id(id):
    for prompt_obj in prompts:
        if prompt_obj['id'] == id:
            return prompt_obj['prompt']
    return None

prompt_id = 1
prompt_text = find_prompt_by_id(prompt_id)

article = get_text_from_image('./media/image_1.png')

result = generate_conversation(prompt_text, article)