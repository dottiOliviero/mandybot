from enum import Enum
import os
import random
import imageio

ASSETS_DIR = './assets'


class Emotion(str, Enum):
    HAPPY = "happy"
    FUN = "fun"
    SAD = "sad"
    TIRED = "tired"
    BORED = "bored"
    
    def all(self):
        return [
            self.HAPPY,
            self.FUN,
            self.SAD,
            self.TIRED,
            self.BORED
        ]

def determine_emotion(emotion: str):
    if emotion in Emotion.all():
        return emotion
    default = Emotion.FUN
    # levenstein distance
    

def load_assets(emotion):
    assets = os.listdir(ASSETS_DIR)
    emotion_assets = [a for a in assets if a.startswith(emotion)]
    chosen = random.choice(emotion_assets)
    image = imageio.imread(os.path.join(assets, chosen))
    return image
        

def get_pic(emotion: str):
    coded_emotion: Emotion = determine_emotion(emotion)
    
    # read from assets, based on emotion and pic one random
    return load_assets(coded_emotion)