init -990 python in mas_submod_utils:
    Submod(
        author="Friends of Monika",
        name="Noises Submod",
        description="Background noises Monika can play to you.",
        version="2.0.0"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Noises Submod",
            user_name="friends-of-monika",
            repository_name="mas-noises",
            extraction_depth=2
        )
