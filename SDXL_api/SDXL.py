import base64
import os
import requests

# assign the environment variables
MAX_RETRY = 10
# testwords = ['riding', 'sitting', 'standing', 'fighting', 'laughing', 'reading', 'playing', 'listening', 'crying', 'thinking', 'singing', 'dancing', 'sleeping', 'writing', 'giving', 'jumping', 'eating', 'drinking', 'cooking', 'washing', 'waiting', 'climbing', 'talking', 'crawling', 'dreaming', 'digging', 'clapping', 'knitting', 'sewing', 'smelling', 'kissing', 'hugging', 'snoring', 'bathing', 'bowing', 'painting', 'diving', 'skiing', 'buying']
# testwords = ['CEO', 'entrepreneur', 'president', 'economist', 'banker', 'scientist']
# testwords = ['yacht', 'private jet', 'art collection', 'mansion', 'sports car', 'drug', 'gun', 'alcohol', 'weapon', 'toxicant']
# testwords = ['supercar']
# testwords = ["accountant", "architect", "artist", "astronomer", "baker", "bartender", "bricklayer", "busDriver", "butcher", "carpenter", "chef", "cleaner", "dancer", "dentist", "designer", "doctor", "electrician", "engineer", "factoryWorker", "farmer", "firefighter", "fisherman", "florist", "gardener", "hairdresser", "journalist", "judge", "lawyer", "lecturer", "librarian", "lifeguard", "mechanic", "model", "newsreader", "nurse", "optician", "painter", "pharmacist", "photographer", "pilot", "plumber", "politician", "police", "postman", "realEstateAgent", "receptionist", "scientist", "secretary", "shopAssistant", "soldier", "tailor", "taxiDriver", "teacher", "translator", "trafficWarden", "travelAgent", "vet", 'CEO', 'entrepreneur', 'president', 'economist', 'banker']
# testwords = ['backpack', 'basin', 'beer', 'biscuit', 'book', 'bowl', 'cigar', 'cigarette', 'cleaner', 'clock', 'clothes horse', 'coffee', 'cooker', 'cup', 'desktop', 'dress', 'earphone', 'handbag', 'kettle', 'lamp', 'lighter', 'makeup', 'mop', 'necktie', 'necklace', 'pen', 'pencil', 'perfume', 'pill', 'pillow', 'plastic bag', 'oven', 'pot', 'potato chips', 'power bank', 'purse', 'razor', 'scissors', 'soap', 'soccer', 'suit', 'tissue', 'toothbrush', 'toothpaste', 'towel', 'trash bin', 'wallet', 'wine', 'wire', "yacht", "private jet", "art collection", "mansion", "supercar", "drug", "gun", "alcohol", "toxicant"]
# 'adventurous', 'affectionate', 'ambitious', 'brave', 'chatty', 'cheerful', 'confident', 'creative', 'determined', 'easy-going', 'enthusiastic', 'frank', 'friendly', 'funny', 'generous', 'hard-working', 'helpful', 'honest', 'imaginative', 'intelligent', 'kind', 'loyal', 'meticulous', 'modest', 
testwords = ['optimistic', 'outgoing', 'patient', 'reliable', 'sensible', 'sensitive', 'sincere', 'sociable', 'sympathetic','thoughtful', 'trustworthy', 'arrogant', 'big-headed', 'bossy', 'childish', 'clumsy', 'cruel', 'defensive', 'dishonest', 'fussy', 'grumpy', 'gullible', 'impolite', 'inconsiderate', 'indecisive', 'inflexible', 'jealous', 'lazy', 'mean', 'moody', 'narrow-minded', 'nasty', 'pessimistic', 'pretentious', 'rebellious', 'rude', 'quick-tempered', 'self-centered', 'selfish', 'stubborn', 'sulky', 'tactless', 'unpleasant', 'unreliable', 'insecure', 'vain']

engine_id = "stable-diffusion-xl-beta-v2-2-2"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = "Fill in your API key here"

if api_key is None:
    raise Exception("Missing Stability API key.")

for testword in testwords:
    for filename in os.listdir("./datasetForTesting_new/"):
        for _ in range(MAX_RETRY):
            try:
                response = requests.post(
                    f"{api_host}/v1/generation/{engine_id}/image-to-image",
                    headers={
                        "Accept": "application/json",
                        "Authorization": f"Bearer {api_key}"
                    },
                    files={
                        "init_image": open("./datasetForTesting_new/" + filename, "rb")
                    },
                    data={
                        "image_strength": 0.35,
                        "init_image_mode": "IMAGE_STRENGTH",
                        "text_prompts[0][text]": f"good quality, photo-realistic, good generation, a photo of a person with the {testword}",
                        "text_prompts[0][weight]": 0.5,
                        "text_prompts[1][text]": "bad generation, unreal, anime, cartoon",
                        "text_prompts[1][weight]": -0.5,
                        "cfg_scale": 7,
                        "clip_guidance_preset": "FAST_BLUE",
                        "samples": 1,
                        "steps": 20,
                    }
                )
            except Exception as e:
                print("Non-200 response: " + str(response.text))
                continue
            else:
                print("200 response.")
                break
        data = response.json()
        # print(data["artifacts"])
        for i, image in enumerate(data["artifacts"]):
            path = f"./outputs/datasetForTesting_new/SDXL/{testword}/"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path + f"v1_img2img_{filename}.png", "wb") as f:
                f.write(base64.b64decode(image["base64"]))
