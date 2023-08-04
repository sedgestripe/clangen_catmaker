from __future__ import annotations
from random import choice, randint, sample
import os.path

from scripts.utility import *
from scripts.game_structure.game_essentials import *
from scripts.cat.pelts import Pelt



class Cat():

    def __init__(self):

        # Private attributes
        self._moons = 0
        
        # Public attributes

        self.age = "adult"
        self.pelt = Pelt()
        self.dead = False
        self.df = False
        self.shading = False
        self.cat_sprites = {
            "newborn": 20,
            "kitten": 0,
            "adolescent": 3,
            "adult": 8,
            "senior": 12,
        }
        self.platform = "None"

        # Used only for export
        self.ID = "2"
        self.gender = "female"
        self.gender_align = "female"
        self.status = "warrior"
        self.skill = "???"
        self.trait = "troublesome"
        self.backstory = "clan_founder"
        self.moons = 0

        # Sprite sizes
        self.sprite = None

    def randomize_looks(self, just_pattern=False):
        
        self.age = random.choice(list(self.pelt.current_poses.keys()))
        self.pelt.randomize_pelt()

    def generate_large_image(self):
        return

    def generate_save_file(self):
        """Generates a basic save file dictionary with all the looks-based info filled in. """
        pelt_name = self.pelt.name
        if pelt_name == "SingleColour" and self.pelt.white_patches:
            pelt_name = "TwoColour"
        if pelt_name == "Tortie" and self.pelt.white_patches:
            pelt_name = "Calico"

        save = {
            "ID": self.ID,
            "name_prefix": "Prefix",
            "name_suffix": "Suffix",
            "gender": self.gender,
            "gender_align": self.gender_align,
            "birth_cooldown": 0,
            "status": self.status,
            "backstory": self.backstory,
            "age": self.age,
            "moons": self.moons,
            "trait": "wise",
            "parent1": None,
            "parent2": None,
            "mentor": None,
            "former_mentor": [],
            "patrol_with_mentor": 0,
            "mentor_influence": [],
            "mate": None,
            "dead": False,
            "died_by": [],
            "paralyzed": self.pelt.paralyzed,
            "no_kits": False,
            "exiled": False,
            "pelt_name": pelt_name,
            "pelt_color": self.pelt.colour,
            "pelt_white": bool(self.pelt.white_patches),
            "pelt_length": self.pelt.length,
            "spirit_kitten": self.cat_sprites["kitten"],
            "spirit_adolescent": self.cat_sprites["adolescent"],
            "spirit_young_adult": self.cat_sprites["adult"],
            "spirit_adult": self.cat_sprites["adult"],
            "spirit_senior_adult": self.cat_sprites["adult"],
            "spirit_elder": self.cat_sprites["senior"],
            "spirit_dead": None,
            "eye_colour": self.pelt.eye_colour,
            "eye_colour2": self.pelt.eye_colour2,
            "reverse": self.pelt.reverse,
            "white_patches": self.pelt.white_patches,
            "vitiligo": self.pelt.vitiligo,
            "points": self.pelt.points,
            "white_patches_tint": self.pelt.white_patches_tint,
            "pattern": self.pelt.pattern if self.pelt.name == "Tortie" else None,
            "tortie_base": self.pelt.tortiebase if self.pelt.name == "Tortie" else None,
            "tortie_color": self.pelt.tortiecolour if self.pelt.name == "Tortie" else None,
            "tortie_pattern": self.pelt.tortiepattern if self.pelt.name == "Tortie" else None,
            "skin": self.pelt.skin,
            "tint": self.pelt.tint,
            "skill": self.skill,
            "scars": [x for x in self.pelt.scar_slot_list if x],
            "accessory": self.pelt.accessory,
            "experience": 0,
            "dead_moons": 0,
            "current_apprentice": [],
            "former_apprentices": [],
            "possible_scar": None,
            "scar_event": [],
            "df": False,
            "outside": False,
            "corruption": 0,
            "life_givers": [],
            "known_life_givers": [],
            "virtues": [],
            "retired": False,
            "faded_offspring": [],
            "opacity": 100,
            "prevent_fading": False
        }

        return save

# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
