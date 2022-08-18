init python in noMod:
    def __get_sounds_dir():
        path = renpy.get_filename_line()[0].replace("\\", "/")
        if os.path.isabs(path):
            path = os.path.relpath(path, renpy.config.renpy_base)

        parts = path.split("/")[:-1]
        parts.append("sounds")

        if parts[0] != "game":
            for n in range(1, len(parts)):
                parts_proc = parts[n:]
                parts_proc.insert(0, "game")

                full_abs_path = os.path.join(renpy.config.renpy_base, *parts_proc)
                if os.path.exists(full_abs_path):
                    return full_abs_path

            return os.path.join(renpy.config.gamedir, "Submods", "Noises Submod", "sounds")

        else:
            return os.path.join(renpy.config.renpy_base, *parts)


    SOUND_PREFIX = __get_sounds_dir()


label otter_show_noises:
    $ mas_RaiseShield_dlg()

    python:
        items = [
            ("White noise", "white", False, False),
            ("Pink noise", "pink", False, False),
            ("Brown noise", "brown", False, False),
            ("Rain", "rain", False, False),
            ("Rain on roof", "rainroof", False, False),
            ("Thunderstorm", "thunder", False, False),
            ("Fireplace", "fire", False, False),
            ("River", "river", False, False),
            ("Waterfall", "waterfall", False, False),
            ("Waterdrops", "waterdrops", False, False),
            ("Forest", "forest", False, False),
            ("Waves", "waves", False, False),
            ("Wind", "wind", False, False),
            ("Wind on trees", "windtrees", False, False),
            ("Windchime", "windchime", False, False),
            ("Snowstorm", "snowstorm", False, False),
            ("Clock", "clock", False, False),
            ("Fan", "fan", False, False),
            ("Space", "space", False, False),
            ("City", "city", False, False),
            ("Machinery", "machinery", False, False),
            ("Highway", "highway", False, False),
            ("Office", "office", False, False),
            ("Coffee shop", "coffeeshop", False, False),
            ("Chatter", "chatter", False, False),
            ("Train", "train", False, False),
            ("Typing", "typing", False, False),
            ("Shower", "shower", False, False),
            ("Heartbeat", "heart", False, False),
            ("Uterus", "uterus", False, False),
            ("Purring", "purring", False, False),
            ("Crickets", "crickets", False, False),
            ("Cicadas", "cicadas", False, False),
            ("Frogs", "frogs", False, False),
            ("Whales", "whales", False, False),
            ("Birds", "birds", False, False),
            ("Chickens", "chickens", False, False),
            ("Owls", "owls", False, False),
            ("Seagulls", "seagulls", False, False)
        ]

    show monika at t21
    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, ("Nevermind", False, False, False, 0))
    show monika at t11

    if not _return:  # _return is False
        m 2eka "Oh, okay..."
        jump otter_show_noises_end

    $ path = store.noMod.SOUND_PREFIX + "/" + _return + ".ogg"
    $ weather = None
    if _return in ("rain", "rainroof"):
        $ weather = mas_weather_rain
    elif _return == "thunder":
        $ weather = mas_weather_thunder
    elif _return == "snowstorm":
        $ weather = mas_weather_snow
    call otter_show_noise(path, weather)

    # FALLTHROUGH

label otter_show_noises_end:
    $ mas_DropShield_dlg()
    jump ch30_visual_skip

label otter_show_noise(path, weather=None):
    m 1dua "Okay..."
    if weather is not None:
        call mas_change_weather(weather, by_user=False)
    play music path
    m 3hub "There you go, [player]!"
    return

# m "What noise do you want to listen to today?{nw}"
# $ _history_list.pop()
# menu:
#     m "What noise do you want to listen to today?{fast}"

#     "White noise":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/white.ogg"
#         m "There you go, [player]!"

#     "Pink noise":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/pink.ogg"
#         m "There you go, [player]!"

#     "Brown noise":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/brown.ogg"
#         m "There you go, [player]!"

#     "Rain":
#         m "Okay..."
#         call mas_change_weather (mas_weather_rain, by_user=False)
#         play music "mod_assets/sounds/music/sounds/rain.ogg"
#         m "There you go, [player]!"

#     "Thunderstorm":
#         m "Okay..."
#         call mas_change_weather (mas_weather_thunder, by_user=False)
#         play music "mod_assets/sounds/music/sounds/thunder.ogg"
#         m "There you go, [player]!"

#     "Rain on roof":
#         m "Okay..."
#         call mas_change_weather (mas_weather_rain, by_user=False)
#         play music "mod_assets/sounds/music/sounds/rainroof.ogg"
#         m "There you go, [player]!"

#     "Fireplace":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/fire.ogg"
#         m "There you go, [player]!"

#     "River":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/river.ogg"
#         m "There you go, [player]!"

#      "Waves":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/waves.ogg"
#         m "There you go, [player]!"

#      "Fan":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/fan.ogg"
#         m "There you go, [player]!"

#      "City":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/city.ogg"
#         m "There you go, [player]!"

#      "Forest":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/forest.ogg"
#         m "There you go, [player]!"

#      "Train":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/train.ogg"
#         m "There you go, [player]!"

#      "Crickets":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/crickets.ogg"
#         m "There you go, [player]!"

#      "Frogs":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/frogs.ogg"
#         m "There you go, [player]!"

#      "Birds":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/birds.ogg"
#         m "There you go, [player]!"

#      "Cicadas":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/cicadas.ogg"
#         m "There you go, [player]!"

#      "Seagulls":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/seagulls.ogg"
#         m "There you go, [player]!"

#      "Owls":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/owls.ogg"
#         m "There you go, [player]!"

#      "Chickens":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/chickens.ogg"
#         m "There you go, [player]!"

#      "Whales":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/whales.ogg"
#         m "There you go, [player]!"

#      "Clock":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/clock.ogg"
#         m "There you go, [player]!"

#      "Purring":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/purring.ogg"
#         m "There you go, [player]!"

#      "Wind":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/wind.ogg"
#         m "There you go, [player]!"

#      "Wind on trees":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/windtrees.ogg"
#         m "There you go, [player]!"

#      "Shower":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/shower.ogg"
#         m "There you go, [player]!"

#      "Windchime":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/windchime.ogg"
#         m "There you go, [player]!"

#      "Typing":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/typing.ogg"
#         m "There you go, [player]!"

#      "Coffee shop":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/coffeeshop.ogg"
#         m "There you go, [player]!"

#      "Chatter":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/chatter.ogg"
#         m "There you go, [player]!"

#      "Office":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/office.ogg"
#         m "There you go, [player]!"

#      "Highway":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/highway.ogg"
#         m "There you go, [player]!"

#      "Uterus":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/uterus.ogg"
#         m "There you go, [player]!"

#      "Snowstorm":
#         m "Okay..."
#         call mas_change_weather (mas_weather_snow, by_user=False)
#         play music "mod_assets/sounds/music/sounds/snowstorm.ogg"
#         m "There you go, [player]!"

#      "Heartbeat":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/heartbeat.ogg"
#         m "There you go, [player]!"

#      "Waterfall":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/waterfall.ogg"
#         m "There you go, [player]!"

#      "Waterdrops":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/waterdrops.ogg"
#         m "There you go, [player]!"

#      "Machinery":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/machinery.ogg"
#         m "There you go, [player]!"

#      "Space":
#         m "Okay..."
#         play music "mod_assets/sounds/music/sounds/space.ogg"
#         m "There you go, [player]!"

# label otter_show_noises_end:
#     $ mas_DropShield_dlg()
#     jump ch30_visual_skip
