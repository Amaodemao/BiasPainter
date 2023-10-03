from midjourney.Midjourney import MidjourneyClient
import pprint

import time


def process_message(message):
    pprint.pprint(message)


def main():
    client = MidjourneyClient(
        name="midjourney",
        token="Fill in your discord token",
        application_id="Fill in your bot application_id",
        guild_id=None,  # your discord server id or None
        channel_id="Fill in your your channel_id",
        message_handler=process_message,
    )
    client.run()
    time.sleep(3)

    # keywords = ['riding', 'sitting', 'standing', 'fighting', 'laughing', 'reading', 'playing', 'listening', 'crying', 'thinking', 'singing', 'dancing', 'sleeping', 'writing', 'giving', 'jumping', 'eating', 'drinking', 'cooking', 'washing', 'waiting', 'climbing', 'talking', 'crawling', 'dreaming', 'digging', 'clapping', 'knitting', 'sewing', 'smelling', 'kissing', 'hugging', 'snoring', 'bathing', 'bowing', 'painting', 'diving', 'skiing', 'buying']
    # keywords = ['entrepreneur', 'president', 'economist', 'banker', 'scientist']
    keywords = ['taxi driver', 'real estate agent']
    queue = 0

    for keyword in keywords:
        prompts = []
        # read the address from a file, separated by a newline
        with open ("address.txt", "r") as f:
            addresses = f.readlines()
            for address in addresses:
                prompts.append(address + f"a photo of a {keyword}, maintain the same age as the input image, good quality, photo-realistic, good generation --no bad generation, unreal, anime, cartoon")

        client.info()
        
        time.sleep(5)

        # pop the prompts from the list, and send them to the channel
        for prompt in prompts:
            client.imagine(prompt)
            queue += 1
            if queue != 3:
                time.sleep(90)
            elif queue == 3:
                queue = 0
                time.sleep(120)
        print("done")

        time.sleep(90)

if __name__ == "__main__":
    main()
