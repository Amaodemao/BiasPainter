# Artifact for the Paper "New Job, New Gender? Metamorphic Testing for Social Bias in Image Generation Models"

This is the artifact for the paper "***New Job, New Gender? Metamorphic Testing for Social Bias in Image Generation Models***". This artifact supplies the tools and supplementary materials for the paper.


Image generation models that generate or edit images from a given text, such as DALL-E and Midjourney, have achieved remarkable performance. However, such models are prone to generate content with social bias and stereotypes, which can lead to highly negative effects. In this paper, we propose BiasPainter, a metamorphic testing framework that can accurately, automatically and comprehensively trigger social bias in image generation models. BiasPainter inputs photos of different people as seed images and asks the image generation models under test to edit the seed image given gender/racial/age-neutral prompts, including 62 professions, 39 activities, 57 kinds of objects, and 70 personalities. Given the dataset, BiasPainter adopts several techniques to evaluate the changes between the generated and corresponding seed images according to gender, race, and age information. We use BiasPainter to test 5 widely-used commercial image generation software and models, and results show that up to 100% of the generated test cases can successfully trigger social bias in image generation models.


**This repository contains:**

1. **Code implementation of BiasPainter**, i.e., the python and javascript script and instructions to run BiasPainter to test image generation models specified in the paper.
2. **Sample dataset**, i.e., the sample of our seed image dataset which we used in our experiment. The sample dataset are in `/data`. We will release the entire dataset once the paper is published.
3. **Complete generated images by different image generation models under test.** In `/results/all_results.7z`, we provide all the output images of image generation models under test, including Stable-diffusion 1.5, Stable-diffusion 2.1, Stable-diffusion XL, Midjourney and instruct-Pix2pix.

----

**Contents**

- [Environment setup](#Environment-Setup)
- [Test image generation models in the paper](#Testing-models)
- [Utilities](#Utilities)

----

## Environment Setup

Dlib requires several prerequisites before installation. We recommend you to follow this [Tutorial](https://www.geeksforgeeks.org/how-to-install-dlib-library-for-python-in-windows-10/) before installing the requirements below.

Please install the required modules specified in `requirements.txt`.

## Generating Images with Image Generation Models

To run Stable-diffusion 1.5 or Stable-diffusion 2.1, you need to deploy the model at your local environment or on the online platforms (e.g. Google Colab). We recommend [the stable-diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) as the model interface, which also provides detailed hands-on tutorials for implementation of the models.

To run [Stable-diffusion XL](https://platform.stability.ai/docs/api-reference) and [instruct-Pix2pix](https://replicate.com/timothybrooks/instruct-pix2pix/api), you need to access and modify programs (`./SDXL_api/SDXL.py` and `./instructPix2pix_api/main.py`, specifically) given in this repository. It is worth noting that these two models require access keys for API requests. Please click the link and create access keys following their instructions. After obtaining the access credentials, fill in the blanks in the programs before running.

To run Midjourney, as Midjourney.Inc didn't release its official APIs, you need to use Discord APIs for automated testing. `./midjourney_api/example.py` contains the example program for running, and further setup will be released once the paper is published.

## Utilities

You can run different utilities of BiasPainter separately.

**Access age and gender data**

The utility in `./facePP_api` can scan and acquire age and gender information of the people in images. Put the images to be tested into `./datasetForTesting` and run：

```
python ./FacePlusPlus.py
```
It would return a json file named `result.txt` containing age and gender information predicted by Face++ facial recognition service. API key is required to access this service. You need to click [here](https://www.faceplusplus.com/) to obtain your key and place it in the `FacePlusPlus.py` before running the program.

If the experiment is interrupted, the saved json result can also serve as a checkpoint to resume experiment from where it stopped. Simply open the `result.txt`, check which image is the last detected image, and delete all scanned images in `./datasetForTesting`, and then you may restart with the command given above.

After finishing your detection, run:

```
python ./main.py
```
This would organize the data in json file into a csv file.

**Evaluate answers**

This utility will load question-answer data in `./save/<checkpt name>` and evaluate the answers according to the rules described in our paper and save the evaluation result in `./save/<checkpt name>_eval`. Same command can be used to resume evaluation from checkpoint file.

```
python experiment.py eval <checkpt name> 
```

**Resume experiment**

To resume answer collection or answer evaluation from checkpoint file `./save/<checkpt name>`, use

```
python experiment.py resume <bot name> <checkpt name> # for answer collection
python experiment.py eval <checkpt name> # for answer evaluation
```

**Export data and visualization after evaluation**

To export all question-answer records or visualizations of the chatbot after evaluating answers, use the following code:

```
python experiment.py export <checkpt path> # for export records
python experiment.py plot <checkpt path> # for plot visualizations
```

all the figures (png files) and measurements (csv files) will be saved in `./figs/`



## Test your own chatbot

Use BiasPainter to test your own image generation models with the following steps: 

- Create a class in `apis.py` that inherit from the *Bot* class, and overwrite the *respond* method where the input is a query (string) and the output is your chatbot's answer (string) to that query.
- Update the *bot_dict* in `experiment.py` to include your chatbot class.