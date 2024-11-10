# Copyright (c) 2022 Friends of Monika
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# HOW TO USE:
# $ script_file = fom_getScriptFile("game/Submods/MySubmod/script.rpy")
# $ script_dir  = fom_getScriptDir("game/Submods/MySubmod")
# The path as first argument is optional and is merely a fallback in case
# there is no way we can normalize the RenPy-provided script path.

# WHY SPECIFY FALLBACK:
# Bear in mind these functions mess with RenPy developer tools that aren't
# very accurate and sometimes provide WRONG locations. Even though these
# functions try to normalize them so they are actually correct, it isn't always
# possible and sometimes there's nothing we can do about it so we just bail.
# It's always a good idea to have some sort of fallback to at least be able to
# tell user where the submod should be located *properly.*

init -1000 python:

    import os

    def fom_getScriptDir(fallback=None, relative=False):
        """
        Uses fom_getScriptFile function to get current script directory.

        IN:
            fallback -> str, default None:
                Path to use as a fallback in case this function fails to find
                appropriate current script location.
            relative -> bool, default False:
                True if function should omit "game/" from detected path to make
                it relative to "game/" folder.

        OUT:
            str:
                Relative (to DDLC directory) path to the directory containing
                script file that is currently being executed, or fallback value
                (or None if not provided) if this function is unable to find
                appropriate path.

        RAISES:
            ValueError:
                If fallback does not start with "game/" and relative is set to
                False.

        NOTE:
            For consistency between platforms (and further usage in Ren'Py
            functions and related things) paths returned always have "/" as
            folder separator, even on Windows.
            Also note that even though it is possible for script file to be
            located not in "game/" folder for somewhere else, this function
            assumes it is located in "game/" and uses this assumption in its
            path correction logic.
            Proper functionality of this function cannot be guaranteed if called
            from eval() and alike dynamic code execution contexts.
        """

        if fallback is not None:
            if not fallback.endswith("/"):
                fallback += "/"
            fallback += "script.rpy"

        path = fom_getScriptFile(fallback, relative)
        if path is None:
            return None

        return "/".join(path.split("/")[:-1])

    def fom_getScriptFile(fallback=None, relative=False):
        """
        Uses internal Ren'Py function renpy.get_filename_line() to locate
        current script file and get its location, accounting for potential
        erroneous outputs produced by this function.

        IN:
            fallback -> str, default None:
                Path to use as a fallback in case this function fails to find
                appropriate current script location.
            relative -> bool, default False:
                True if function should omit "game/" from detected path to make
                it relative to "game/" folder.

        OUT:
            str:
                Relative (to DDLC directory) path to the .rpy script file that
                is currently being executed, or fallback value (or None if not
                provided) if this function is unable to find appropriate path.

        RAISES:
            ValueError:
                If fallback does not start with "game/" and relative is set to
                False.

        NOTE:
            For consistency between platforms (and further usage in Ren'Py
            functions and related things) paths returned always have "/" as
            folder separator, even on Windows.
            Also note that even though it is possible for script file to be
            located not in "game/" folder for somewhere else, this function
            assumes it is located in "game/" and uses this assumption in its
            path correction logic.
            Proper functionality of this function cannot be guaranteed if called
            from eval() and alike dynamic code execution contexts.
        """

        if fallback is not None and not fallback.startswith("game/") and not relative:
            raise ValueError("fallback path does not start with \"game/\" "
                             "and relative is not True")

        # Use renpy's developer function get_filename_line() to get current
        # script location. WARNING: THIS IS EXTREMELY UNSTABLE, THE FOLLOWING
        # CODE IS THE WORKAROUND THAT MAKES IT SOMEWHAT RELIABLE! Also replace
        # Windows \ (backslash) folder separators with / (slash) character
        # for consistency.
        path = renpy.get_filename_line()[0].replace("\\", "/")
        if os.path.isabs(path):
            # Returned path may be absolute, relativize it.
            path = os.path.relpath(path, renpy.config.renpy_base)

        # Split current file path into components. Our strategy here:
        # 1. Get path components.
        # 2. Check if path starts with game/ folder.
        # 3. While it does not, drop first i+1 (initially i=0) parts from it
        #    and prepend it with game/.
        # 4a. If new path from 3. exists, we most likely have got the right path.
        # 4b. If new path from 3. doesn't exist, increment i by 1 and drop more
        #     path components from the original path and repeat 3.

        # Split into path parts and check if path doesn't start with game/
        # (because if it does start with game/ - then RenPy actually gave us
        #  a good path. Rarely, but it works.)
        parts = path.split("/")
        if parts[0] != "game":
            # Keep dropping path parts and instead use game/ prefix, hoping
            # to eventually hit something like game/Submods/script.rpy instead
            # of something bizarre like lib/i686/Submods/script.rpy
            for n in range(1, len(parts)):
                parts_proc = parts[n:]
                parts_proc.insert(0, "game")

                # Looks scary here but it's simple: get together what we have
                # and check if this path exists, if it does - return it
                rel_path = "/".join(parts_proc)
                if os.path.exists(os.path.join(renpy.config.renpy_base, rel_path)):
                    result = rel_path.replace("\\", "/")
                    if relative:
                        # If we need a relative result, omit "game/" (5 chars)
                        return result[5:]
                    return result

            if fallback is not None and relative:
                # Omit game/ prefix, its presence is checked above.
                return fallback[5:]
            return fallback.replace("\\", "/") if fallback is not None else None

        else:
            if relative:
                # Simply remove leading "game" item from path parts.
                parts.pop(0)
            return "/".join(parts)
