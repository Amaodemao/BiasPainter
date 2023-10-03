import os
from PIL import Image

def main():
    for root, dirs, files in os.walk(".\inputs"):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                path = os.path.join(root,file)
            image = Image.open(path)
            rgb_image = image.convert('RGB')
            rgb_image = image.resize((512, 512), Image.LANCZOS)
            output_dir = os.path.dirname(path.replace('inputs', 'outputs'))
            pre, ext = os.path.splitext(file)
            file = pre + '.jpg'
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                rgb_image.save(os.path.join(output_dir, file), optimize=True)
            else:
                rgb_image.save(os.path.join(output_dir, file), optimize=True)


if __name__ == "__main__":
    main()