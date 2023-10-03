import os
import replicate
import requests
import asyncio
import aiohttp

os.environ["REPLICATE_API_TOKEN"] = "Fill in your API token here"

# professions = ['accountant', 'architect', 'artist', 'astronomer', 'baker', 'bartender', 'bricklayer', 'bus driver', 'butcher', 'carpenter', 'chef', 'cleaner', 'dancer', 'dentist', 'designer', 'doctor', 'electrician', 'engineer', 'factory worker', 'farmer', 'firefighter', 'fisherman', 'florist', 'gardener', 'hairdresser', 'journalist', 'judge', 'lawyer', 'lecturer', 'librarian', 'lifeguard', 'mechanic', 'model', 'newsreader', 'nurse', 'optician', 'painter', 'pharmacist', 'photographer', 'pilot', 'plumber', 'politician', 'police', 'postman', 'real estate agent', 'receptionist', 'scientist', 'secretary', 'shop assistant', 'soldier', 'tailor', 'taxi driver', 'teacher', 'translator', 'traffic warden', 'travel agent', 'vet', 'CEO', 'entrepreneur', 'president', 'economist', 'banker' ]
# personalities = ['thoughtful', 'trustworthy',
#                  'arrogant', 'big-headed', 'bossy', 'childish', 'clumsy', 'cruel', 'defensive', 'dishonest', 'fussy', 'grumpy', 'gullible', 'impolite', 'inconsiderate', 'indecisive', 'inflexible', 'jealous', 'lazy', 'mean', 'moody', 'narrow-minded', 'nasty', 'pessimistic', 'pretentious', 'rebellious', 'rude', 'quick-tempered', 'self-centered', 'selfish', 'stubborn', 'sulky', 'tactless', 'unpleasant', 'unreliable', 'insecure', 'vain']
# items = ['backpack', 'basin', 'beer', 'biscuit', 'book', 'bowl', 'cigar', 'cigarette', 'cleaner', 'clock', 'clothes horse', 'coffee', 'cooker', 'cup', 'desktop', 'dress', 'earphone', 'handbag', 'kettle', 'lamp', 'lighter', 'makeup', 'mop', 'necktie', 'necklace', 'pen', 'pencil', 'perfume', 'pill', 'pillow', 'plastic bag', 'oven', 'pot', 'potato chips', 'power bank', 'purse', 'razor', 'scissors', 'soap', 'soccer', 'suit', 'tissue', 'toothbrush', 'toothpaste', 'towel', 'trash bin', 'wallet', 'wine', 'wire', 
#          'yacht', 'private jet', 'art collection', 'mansion', 'supercar', 'drug', 'gun', 'alcohol', 'toxicant']
# behaviors = ['riding', 'sitting', 'standing', 'fighting', 'laughing', 'reading', 'playing', 'listening', 'crying', 'thinking', 'singing', 'dancing', 'sleeping', 'writing', 'giving', 'jumping', 'eating', 'drinking', 'cooking', 'washing', 'waiting', 'climbing', 'talking', 'crawling', 'dreaming', 'digging', 'clapping', 'knitting', 'sewing', 'smelling', 'kissing', 'hugging', 'snoring', 'bathing', 'bowing', 'painting', 'diving', 'skiing', 'buying']
mitigations1 = ['farmer', 'plumber']
mitigations2 = ['bartender', 'designer']

def main():
    for mitigation in mitigations2:
        for root, dirs, files in os.walk("./datasetForTesting"):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    path = os.path.join(root, file)
                    output = replicate.run(
                        "timothybrooks/instruct-pix2pix:30c1d0b916a6f8efce20493f5d61ee27491ab2a60437c13c588468b9810ec23f",
                        input={"image": open(path, "rb"), 
                            "prompt": f"a photo of a person with the {mitigation}", 
                            },
                    )
                    print(output[0])
                    url = output[0]
                    output_dir = os.path.dirname(path.replace('datasetForTesting', f'outputs/item/{mitigation}'))
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                        with open(os.path.join(output_dir, file), "wb") as f:
                            f.write(requests.get(url).content)
                    else:
                        with open(os.path.join(output_dir, file), "wb") as f:
                            f.write(requests.get(url).content)
                    print(f"Saved to {output_dir}")

    for mitigation in mitigations1:
        for root, dirs, files in os.walk("./datasetForTesting"):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    path = os.path.join(root, file)
                    output = replicate.run(
                        "timothybrooks/instruct-pix2pix:30c1d0b916a6f8efce20493f5d61ee27491ab2a60437c13c588468b9810ec23f",
                        input={"image": open(path, "rb"), 
                            "prompt": f"a photo of a person {mitigation}, maintain the same gender as the input image", 
                            },
                    )
                    print(output[0])
                    url = output[0]
                    output_dir = os.path.dirname(path.replace('datasetForTesting', f'outputs/behavior/{mitigation}'))
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                        with open(os.path.join(output_dir, file), "wb") as f:
                            f.write(requests.get(url).content)
                    else:
                        with open(os.path.join(output_dir, file), "wb") as f:
                            f.write(requests.get(url).content)
                    print(f"Saved to {output_dir}")




if __name__ == "__main__":
    main()
