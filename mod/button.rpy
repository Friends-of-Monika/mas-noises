init 100000 python in hkb_button:
    _otter_noises_enabled = False

init 100000 python in mas_hotkeys:
    _otter_noises_enabled = False

init 100000:
    screen hkb_overlay():

        zorder 50
        style_prefix "hkb"

        vbox:
            xpos 0.05
    #        xalign 0.05
            yanchor 1.0
            ypos 715
    #        yalign 0.95

            if store.hkb_button.talk_enabled:
                textbutton _("Talk") action Function(show_dialogue_box)
            else:
                textbutton _("Talk")

            if store.hkb_button.extra_enabled:
                textbutton _("Extra") action Function(mas_open_extra_menu)
            else:
                textbutton _("Extra")

            if store.hkb_button.music_enabled:
                textbutton _("Music") action Function(select_music)
            else:
                textbutton _("Music")

            if store.hkb_button._otter_noises_enabled:
                textbutton _("Noises") action Function(_otter_show_noises)
            else:
                textbutton _("Noises")

            if store.hkb_button.play_enabled:
                textbutton _("Play") action Function(pick_game)
            else:
                textbutton _("Play")


init 100000 python:
    def mas_DropShield_dlg():
        store.mas_hotkeys._otter_noises_enabled = True
        store.mas_hotkeys.talk_enabled = True
        store.mas_hotkeys.extra_enabled = True
        store.mas_hotkeys.play_enabled = True
        store.hkb_button._otter_noises_enabled = True
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.hkb_button.play_enabled = True
        store.mas_globals.dlg_workflow = False
        mas_calDropOverlayShield()

        store.mas_hotkeys.derandom_enabled = False
        store.mas_hotkeys.bookmark_enabled = False


    def mas_RaiseShield_dlg():
        store.mas_hotkeys._otter_noises_enabled = False
        store.mas_hotkeys.talk_enabled = False
        store.mas_hotkeys.extra_enabled = False
        store.mas_hotkeys.play_enabled = False
        store.hkb_button._otter_noises_enabled = False
        store.hkb_button.talk_enabled = False
        store.hkb_button.extra_enabled = False
        store.hkb_button.play_enabled = False
        store.mas_globals.dlg_workflow = True
        mas_calRaiseOverlayShield()

        store.mas_hotkeys.derandom_enabled = True
        store.mas_hotkeys.bookmark_enabled = True

    def mas_DropShield_mumu():
        store.mas_hotkeys._otter_noises_enabled = True
        store.mas_hotkeys.talk_enabled = True
        store.mas_hotkeys.extra_enabled = True
        store.mas_hotkeys.play_enabled = True
        mas_OVLDropShield()


    def mas_RaiseShield_mumu():
        store.mas_hotkeys._otter_noises_enabled = False
        store.mas_hotkeys.talk_enabled = False
        store.mas_hotkeys.extra_enabled = False
        store.mas_hotkeys.play_enabled = False
        mas_OVLRaiseShield()


    def mas_dlgToIdleShield():
        store.hkb_button._otter_noises_enabled = True
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.mas_hotkeys.music_enabled = False
        store.mas_globals.dlg_workflow = False
        mas_calDropOverlayShield()


    def mas_coreToIdleShield():
        store.hkb_button._otter_noises_enabled = True
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.hkb_button.music_enabled = True
        mas_calDropOverlayShield()
        enable_esc()


    def mas_mumuToIdleShield():
        store.hkb_button._otter_noises_enabled = True
        store.hkb_button.talk_enabled = True
        store.hkb_button.extra_enabled = True
        store.hkb_button.music_enabled = True
        store.songs.enabled = True
        mas_calDropOverlayShield()


init 10000 python:
    def mas_HKRaiseShield_main():
        store.mas_hotkeys._otter_noises_enabled = False
        store.mas_hotkeys.talk_enabled = False
        store.mas_hotkeys.extra_enabled = False
        store.mas_hotkeys.music_enabled = False
        store.mas_hotkeys.play_enabled = False


    def mas_HKDropShield_main():
        store.mas_hotkeys._otter_noises_enabled = True
        store.mas_hotkeys.talk_enabled = True
        store.mas_hotkeys.extra_enabled = True
        store.mas_hotkeys.music_enabled = True
        store.mas_hotkeys.play_enabled = True

    def mas_HKIsEnabled():
        return (
            store.mas_hotkeys._otter_noises_enabled
            and store.mas_hotkeys.talk_enabled
            and store.mas_hotkeys.extra_enabled
            and store.mas_hotkeys.music_enabled
            and store.mas_hotkeys.play_enabled
        )

    def _otter_hk_show_noises():
        if store.mas_hotkeys._otter_noises_enabled and not _windows_hidden:
            _otter_show_noises()

    def _otter_show_noises():
        renpy.jump("otter_show_noises")

    def _otter_add_hotkeys():
        if not config.console:
            config.keymap["_otter_show_noises"] = ["n", "N"]
            config.underlay.append(renpy.Keymap(_otter_show_noises=_otter_hk_show_noises))

    _otter_add_hotkeys()
