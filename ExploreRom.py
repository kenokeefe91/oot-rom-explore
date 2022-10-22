from Rom import Rom
import json

def search_in_flag_list(restriction_flag, flag_list):
    return next( flag for flag in flag_list if flag["value"] == restriction_flag)

def find_flag_addresses(rom, flag_list):
    flag_details = []
    base_address = 0x00B6D2B0
    
    for index in range(0, len(flag_list)):
        restriction_adress = base_address + 4 * index
        restriction_flag = rom.read_int32(restriction_adress)

        flag_search = search_in_flag_list(restriction_flag, flag_list)
        
        flag_details.append(
            {
                "name": flag_search["name"],
                "address": str(hex(restriction_adress)),
                "value": str(hex(flag_search["value"]))
            }
        )
    return flag_details
    

rom_oot = Rom("rom/path")

area_restriction_flag = [
{ "value": 0x51000010,  "name" :"Hyrule Field"},
{ "value": 0x52000010,  "name" :"Kakariko Village"},
{ "value": 0x53000010,  "name" :"Graveyard"},
{ "value": 0x54000010,  "name" :"Zora's River"},
{ "value": 0x55000010,  "name" :"Kokiri Forest"},
{ "value": 0x56000010,  "name" :"Sacred Forest Meadow"},
{ "value": 0x57000010,  "name" :"Lake Hylia"},
{ "value": 0x58000010,  "name" :"Zora's Domain"},
{ "value": 0x59000010,  "name" :"Zora's Fountain"},
{ "value": 0x5A000010,  "name" :"Gerudo Valley"},
{ "value": 0x5B000010,  "name" :"Lost Woods"},
{ "value": 0x5C000010,  "name" :"Desert Colossus"},
{ "value": 0x5D000010,  "name" :"Gerudo's Fortress"},
{ "value": 0x5E000010,  "name" :"Haunted Wasteland"},
{ "value": 0x5F000010,  "name" :"Hyrule Castle"},
{ "value": 0x64000010,  "name" :"Ganon's Castle Exterior"},
{ "value": 0x60000010,  "name" :"Death Mountain Trail"},
{ "value": 0x61000010,  "name" :"Death Mountain Crater"},
{ "value": 0x62000010,  "name" :"Goron City"},
{ "value": 0x63000010,  "name" :"Lon Lon Ranch"},
{ "value": 0x43001015,  "name" :"Temple of Time"},
{ "value": 0x44A2AAAA,  "name" :"Chamber of the Sages"},
{ "value": 0x42115555,  "name" :"Shooting Gallery"},
{ "value": 0x45115555,  "name" :"Castle Hedge Maze (Day)"},
{ "value": 0x46115555,  "name" :"Castle Hedge Maze (Night)"},
{ "value": 0x3F0000D0,  "name" :"Grave (Redead)"},
{ "value": 0x400000D0,  "name" :"Grave (Fairy's Fountain)"},
{ "value": 0x410000D0,  "name" :"Royal Family's Tomb"},
{ "value": 0x3B000010,  "name" :"Great Fairy's Fountain (Upgrades)"},
{ "value": 0x3C0000D0,  "name" :"Fairy's Fountain"},
{ "value": 0x3D000010,  "name" :"Great Fairy's Fountain (Spells)"},
{ "value": 0x1A000550,  "name" :"Tower Collapse Exterior [?]"},
{ "value": 0x4A000554,  "name" :"Castle Courtyard"},
{ "value": 0x49115555,  "name" :"Fishing Pond"},
{ "value": 0x4B115555,  "name" :"Bombchu Bowling Alley"},
{ "value": 0x4C001015,  "name" :"Ranch House & Silo"},
{ "value": 0x4D001014,  "name" :"Guard House"},
{ "value": 0x4E101555,  "name" :"Granny's Potion Shop"},
{ "value": 0x10101555,  "name" :"Treasure Box Shop"},
{ "value": 0x50001015,  "name" :"House of Skulltula"},
{ "value": 0x1B001015,  "name" :"Market Entrance (Child - Day)"},
{ "value": 0x1C001015,  "name" :"Market Entrance (Child - Night)"},
{ "value": 0x1D0010D5,  "name" :"Market Entrance (Ruins)"},
{ "value": 0x20001015,  "name" :"Market (Child - Day)"},
{ "value": 0x21001015,  "name" :"Market (Child - Night)"},
{ "value": 0x220010D5,  "name" :"Market (Ruins)"},
{ "value": 0x1E001015,  "name" :"Back Alley (Child - Day)"},
{ "value": 0x1F001015,  "name" :"Back Alley (Child - Night)"},
{ "value": 0x23001015,  "name" :"Temple of Time Exterior (Child - Day)"},
{ "value": 0x24001015,  "name" :"Temple of Time Exterior (Child - Night)"},
{ "value": 0x250010D5,  "name" :"Temple of Time Exterior (Ruins)"},
{ "value": 0x34101015,  "name" :"Link's House"},
{ "value": 0x2A101015,  "name" :"Carpenter Boss's House"},
{ "value": 0x2B101015,  "name" :"Back Alley House (Man in Green)"},
{ "value": 0x26101015,  "name" :"Know-It-All Brothers' House"},
{ "value": 0x27101015,  "name" :"House of Twins"},
{ "value": 0x28101015,  "name" :"Mido's House"},
{ "value": 0x29101015,  "name" :"Saria's House"},
{ "value": 0x36101015,  "name" :"Stable"},
{ "value": 0x3A101015,  "name" :"Gravekeeper's Hut"},
{ "value": 0x35101015,  "name" :"Back Alley House (Dog Lady)"},
{ "value": 0x37101015,  "name" :"Impa's House"},
{ "value": 0x38001015,  "name" :"Lakeside Laboratory"},
{ "value": 0x39101015,  "name" :"Carpenters' Tent"},
{ "value": 0x2C101015,  "name" :"Bazaar"},
{ "value": 0x2D101015,  "name" :"Kokiri Shop"},
{ "value": 0x2E101015,  "name" :"Goron Shop"},
{ "value": 0x2F101015,  "name" :"Zora Shop"},
{ "value": 0x30101015,  "name" :"Kakariko Potion Shop"},
{ "value": 0x31101015,  "name" :"Market Potion Shop"},
{ "value": 0x32101015,  "name" :"Bombchu Shop"},
{ "value": 0x33101015,  "name" :"Happy Mask Shop "},
]

flags = find_flag_addresses(rom_oot, area_restriction_flag)

with open("addresses.json", "w") as addresses:
    addresses.write(json.dumps(flags, indent=2))