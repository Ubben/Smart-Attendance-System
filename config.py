import os

class Config:
    SECRET_KEY = "smartattendance2026"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DATABASE = os.path.join(BASE_DIR, "database.db")

    DATASET_PATH = os.path.join(BASE_DIR, "dataset")

    TRAINER_PATH = os.path.join(BASE_DIR, "trainer")