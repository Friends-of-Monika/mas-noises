init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="Noises Mod",
        description="FILL THIS",
        version="1.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Noises Mod",
            user_name="my-otter-self",
            repository_name="mas_noises",
            submod_dir="/Submods/Noises Mod",
            extraction_depth=3
        )