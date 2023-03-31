actions = ["explore", "search", "inventory", "quit"]

items = {
  "Courtyard": {
    "item": ["sword"],
    "description": [
      "A gleaming sword you pulled out of stone left untouched" +
      " and exposed to elements for centuries but still razor sharp"
    ],
  },
  "Jail Cells": {
    "item": ["set of shackles"],
    "description": [
      """A set of shackles with not one spot of rust, 
the material is unknown"""
    ],
  },
  "Throne Room": {
    "item": ["crown"],
    "description": [
      """A golden crown found sitting on the throne, 
the crown is studded with gems, the large glowing purple gem 
on the front of the crown catches your attention"""
    ],
  },
  "Lower Dungeons": {
    "item": ["key"],
    "description": [
      """You found a mysterious bronze skeleton key hanging from a wall, 
which door is this for?"""
    ],
  },
  "Guard Hall": {
    "item": ["shield"],
    "description": [
      """This sturdy shield may be useful later on, 
it is lined with the same unbreakable material as the shackles 
and the main body out of a wood as hard as iron"""
    ],
  },
  "Main Hall": {
    "item": ["map"],
    "description": [
      """This map displayed several mysterious caves 
and cliffs with some shadowed area, 
the castle is located in the middle of the map"""
    ],
  },
}
# Rooms list containing possible rooms and directions user can go in
# once in said room
rooms = [
  ["Courtyard", {
    "north": "Main Hall"
  }],
  ["Jail Cells", {
    "east": "Main Hall"
  }],
  ["Throne Room", {
    "south": "Guard Hall",
  }],
  ["Lower Dungeons", {
    "west": "Main Hall"
  }],
  ["Guard Hall", {
    "north": "Throne Room",
    "south": "Main Hall"
  }],
  [
    "Main Hall",
    {
      "north": "Guard Hall",
      "east": "Lower Dungeons",
      "south": "Courtyard",
      "west": "Jail Cells",
    },
  ],
]