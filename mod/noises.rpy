init python in noMod:
    from store import persistent
    import store
    import os

    SOUND_PREFIX = store.fom_getScriptDir("game/Submods/Noises Submod")
    SOUND_PREFIX_REL = os.path.relpath(SOUND_PREFIX, renpy.config.gamedir).replace("\\", "/")

    if not os.path.exists(SOUND_PREFIX):
        store.mas_submod_utils.submod_log.error("[Noises] Failed to locate SOUND_PREFIX: "
                                                "resolved to {0}, which does not exist"
                                                .format(SOUND_PREFIX))

    current_noise = None
    current_weather = None


    def play_noise(name):
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

        global current_noise
        current_noise = name


label fom_show_noises:
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

        if store.noMod.current_noise is None:
            final_args = [("Nevermind", False, False, False, 4)]

        else:
            final_args = [
                ("No sounds", "silence", False, False, 4),
                ("Nevermind", False, False, False, 0)
            ]

    m 1eub "What noise do you want to listen to today?"

    show monika at t21
    call screen mas_gen_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_TXT_LOW_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, *final_args)
    show monika at t11

    if not _return:  # _return is False
        m 2eka "Oh, okay..."

    else:  # _return is either silence (stop sounds) or actual sound
        m 1dua "Okay..."

        if _return == "silence":
            call fom_hide_noise

        else:
            $ weather = None
            if _return in ("rain", "rainroof"):
                $ weather = mas_weather_rain
            elif _return == "thunder":
                $ weather = mas_weather_thunder
            elif _return == "snowstorm":
                $ weather = mas_weather_snow

            call fom_show_noise(_return, weather)

    $ mas_DropShield_dlg()
    jump ch30_visual_skip

label fom_show_noise(name, weather=None):
    if weather is not None:
        call mas_change_weather(weather)
    $ store.noMod.current_weather = mas_current_weather

    $ store.noMod.play_noise(name)

    m 3hub "There you go, [player]!"
    return

label fom_hide_noise:
    # call mas_change_weather(store.noMod.current_weather)
    # FIXME: ^ This won't work, weather won't reset. As a compromise have this:
    if store.noMod.current_weather is not None:
        call mas_change_weather(mas_weather_def)
        $ store.noMod.current_weather = None

    $ store.noMod.play_noise(None)

    m 3hub "I hope you enjoyed these sounds, [mas_get_player_nickname()]~"
    return