from enum import Enum
from typing import Any
from functools import total_ordering


@total_ordering
class League(Enum):
    bronze = 0,
    silver = 1,
    gold = 2,
    platinum = 3,

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


COLORS: list[str] = [
    "#6A5CFF",
    "#e46e6e",
    "#FFD635",
    "#7EED56",
    "#00CCC0",
    "#51E9F4",
    "#94B3FF",
    "#9C6926",
    "#6D001A",
    "#bf4300",
    "#000000",
    "#FFFFFF"
]

TASKS: list[dict[str, Any]] = [
    {
        'id': "x:notcoin",
        'name': "Notcoin on X.com",
        'type': 'x',
        'reward': 128
    },
    {
        'id': "x:notpixel",
        'name': "Not Pixel on X.com",
        'type': 'x',
        'reward': 128
    },
    {
        'id': "channel:notpixel_channel",
        'name': "Not Pixel Channel",
        'type': 'tg',
        'value': 'https://t.me/notpixel_channel',
        'reward': 128
    },
    {
        'id': "channel:notcoin",
        'name': "Notcoin community",
        'type': 'tg',
        'value': 'https://t.me/notcoin',
        'reward': 128
    },
    {
        'id': "premium",
        'name': "Telegram Premium",
        'type': 'premium',
        'reward': 512
    },
    {
        'id': "paint20pixels",
        'name': "Paint 20 Pixels",
        'type': 'paint',
        'value': 20,
        'reward': 64
    },
    {
        'id': "invite3frens",
        'name': "Invite 3 frens",
        'type': 'invite',
        'value': 3,
        'reward': 64
    },
    {
        'id': "joinSquad",
        'name': "Join Squad",
        'type': 'squad',
        'reward': 64
    },
    {
        'id': "leagueBonusSilver",
        'name': "Silver League Bonus",
        'type': 'league',
        'value': League.silver,
        'reward': 16
    },
    {
        'id': "leagueBonusGold",
        'name': "Gold League Bonus",
        'type': 'league',
        'value': League.gold,
        'reward': 32
    },
    {
        'id': "leagueBonusPlatinum",
        'name': "Platinum League Bonus",
        'type': 'league',
        'value': League.platinum,
        'reward': 64
    }
]

UPGRADE_REPAINT: list[dict[str, Any]] = [
    {
        'level': 2,
        'price': 5,
        'value': 1.5
    },
    {
        'level': 3,
        'price': 100,
        'value': 2
    },
    {
        'level': 4,
        'price': 200,
        'value': 2.5
    },
    {
        'level': 5,
        'price': 300,
        'value': 3
    },
    {
        'level': 6,
        'price': 500,
        'value': 3.5
    },
    {
        'level': 7,
        'price': 600,
        'value': 4
    }
]

UPGRADE_RECHARGE_SPEED: list[dict[str, Any]] = [
    {
        'level': 2,
        'price': 5,
        'value': 570
    },
    {
        'level': 3,
        'price': 100,
        'value': 540
    },
    {
        'level': 4,
        'price': 200,
        'value': 510
    },
    {
        'level': 5,
        'price': 300,
        'value': 480
    },
    {
        'level': 6,
        'price': 400,
        'value': 450
    },
    {
        'level': 7,
        'price': 500,
        'value': 420
    },
    {
        'level': 8,
        'price': 600,
        'value': 390
    },
    {
        'level': 9,
        'price': 700,
        'value': 360
    },
    {
        'level': 10,
        'price': 800,
        'value': 330
    },
    {
        'level': 11,
        'price': 900,
        'value': 300
    }
]

UPGRADE_CHARGE_LIMIT: list[dict[str, Any]] = [
    {
        'level': 2,
        'price': 5,
        'value': 6
    },
    {
        'level': 3,
        'price': 100,
        'value': 7
    },
    {
        'level': 4,
        'price': 200,
        'value': 8
    },
    {
        'level': 5,
        'price': 300,
        'value': 9
    },
    {
        'level': 6,
        'price': 400,
        'value': 10
    }
]

# Author: https://github.com/Desamod
