init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="Noises Submod",
        description="Background noises Monika can play to you",
        version="1.0.1"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Noises Submod",
            user_name="my-otter-self",
            repository_name="mas_noises",
            extraction_depth=3
        )
