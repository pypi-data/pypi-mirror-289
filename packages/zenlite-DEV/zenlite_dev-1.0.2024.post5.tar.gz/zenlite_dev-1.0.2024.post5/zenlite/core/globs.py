import os, sys;    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = str(True)
import glm, glfw
import pygame as pg, numpy as np
from numba import njit as bytec

ZEN_ASSET_DIR:str=f"assets/"
