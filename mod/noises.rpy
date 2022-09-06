default persistent._noMod_current_noise = None

init python in noMod:
    import os


    def __get_sounds_dir():
        path = renpy.get_filename_line()[0].replace("\\", "/")
        if os.path.isabs(path):
            path = os.path.relpath(path, renpy.config.renpy_base)

        parts = path.split("/")[:-1]
        parts.append("res")
        parts.append("audio")

        if parts[0] != "game":
            for n in range(1, len(parts)):
                parts_proc = parts[n:]
                parts_proc.insert(0, "game")

                full_abs_path = os.path.join(renpy.config.renpy_base, *parts_proc)
                if os.path.exists(full_abs_path):
                    return full_abs_path

            return os.path.join(renpy.config.gamedir, "Submods", "Noises Submod", "res", "audio")

        else:
            return os.path.join(renpy.config.renpy_base, *parts)


    SOUND_PREFIX = __get_sounds_dir()
    SOUND_PREFIX_REL = os.path.relpath(SOUND_PREFIX, renpy.config.gamedir).replace("\\", "/")


    def play_noise(name, persist=False):
        if name is not None:
            path = store.noMod.SOUND_PREFIX_REL + "/" + name + ".ogg"

            renpy.music.play(
                path,
                channel="background",
                loop=True,
                synchro_start=True,
                fadein=1.2,
                fadeout=1.2,
                if_changed=True
            )

        else:
            renpy.music.stop(channel="background", fadeout=1.2)

        if persist:
            persistent._noMod_current_noise = name


init 10000 python:
    if persistent._noMod_current_noise is not None:
        store.noMod.play_noise(persistent._noMod_current_noise)


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


    m 1eub "What noise do you want to listen to today?"

    show monika at t21
    $ final_args = [("Nevermind", False, False, False, 0)]
    if persistent._noMod_current_noise is not None:
        $ final_args.insert(0, ("No sounds", "silence", False, False, 0))
    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, *final_args)
    show monika at t11

    if not _return:  # _return is False
        m 2eka "Oh, okay..."
        jump otter_show_noises_end

    $ weather = None
    if _return in ("rain", "rainroof"):
        $ weather = mas_weather_rain
    elif _return == "thunder":
        $ weather = mas_weather_thunder
    elif _return == "snowstorm":
        $ weather = mas_weather_snow
    call otter_show_noise(_return, weather)

    # FALLTHROUGH

label otter_show_noises_end:
    $ mas_DropShield_dlg()
    jump ch30_visual_skip

label otter_show_noise(name, weather=None):
    m 1dua "Okay..."
    if weather is not None:
        call mas_change_weather(weather, by_user=False)
    $ store.noMod.play_noise(name, persist=True)
    m 3hub "There you go, [player]!"
    return
