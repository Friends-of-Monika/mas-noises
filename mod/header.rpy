init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="Noises Submod",
        description="Background noises Monika can play to you",
        version="1.1.2",
        version_updates={
            "otter_noises_submod_v1_0_0": "otter_noises_submod_v1_1_0"
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Noises Submod",
            user_name="my-otter-self",
            repository_name="mas_noises",
            extraction_depth=3
        )


## UPDATE SCRIPTS

label otter_noises_submod_v1_0_0(version="v1_0_0"):
    # Initial version (first release.)
    return

label otter_noises_submod_v1_1_0(version="v1_1_0"):
    # Cleanup persistent since no longer persisting noise.
    $ persistent.__dict__.pop("_noMod_current_noise", None)
    return