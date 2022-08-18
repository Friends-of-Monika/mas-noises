#show noise button
screen noise_button():
    zorder 12
    style_prefix "hkb"
    vbox:
        xpos 0.05
        yanchor 1.0
        ypos 50

        if renpy.get_screen("hkb_overlay"):
            if store.mas_hotkeys.talk_enabled is False:
                if mas_submod_utils.current_label == "mas_piano_setupstart":
                    text _("")
                else:
                    textbutton _("Noise")
            #code inspired by ZeroFixer
            elif mas_curr_affection == mas_affection.NORMAL or mas_curr_affection == mas_affection.UPSET or mas_curr_affection == mas_affection.DISTRESSED or mas_curr_affection == mas_affection.BROKEN:
                textbutton _("Noise")
            else:
                textbutton _("Noise")

#starts noise button
noise_button()

init python:
    def NoiseButton():
        if not NoiseVisible():
            config.overlay_screens.append("noise_button")
