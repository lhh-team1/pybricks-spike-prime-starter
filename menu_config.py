"""The list of missions your hub menu shows, in the order it shows them.

Each slot is a little dictionary with these keys:

    "display"   (required) What shows on the hub screen for this slot.
                A number 0-99, a single letter like "A", or a 5-row
                pixel pattern (list of 5 strings) — same as pix_display.
    "module"    (required) The name of the .py file to run, with no ".py"
                and no dots.
    "function"  (optional) The name of the function inside that file to
                call, like "run". Leave this key OUT to run the WHOLE
                file top-to-bottom instead (this is how block programs run).
    "blocks"    (optional, default False) Set to True for a function that
                comes from a block program's "My Block".
    "enabled"   (optional, default True) Set to False to hide a slot from
                the menu without deleting it from this list.

The ORDER of the list is the order the slots appear in the menu.

Heads up: the Pybricks Git extension's menu manager rewrites this file —
comments inside the MENU_ITEMS list are not kept.
"""

# ---------------------------------------------------------------------
# Bundle hints — one `import` line per mission file listed below.
#
# These imports NEVER run: _BUNDLE_HINTS is False, so the whole block is
# skipped. They are here because your programs are sent to the hub over
# Bluetooth, and the uploader only sends a file if it sees a real
# `import` line for it somewhere. The menu finds your missions by NAME
# (the "module" text below), which the uploader can't see — so without
# these lines the hub would say "no module named ..." when you press
# CENTER.
#
# Add a matching `import` line here whenever you add a mission below.
# ---------------------------------------------------------------------
_BUNDLE_HINTS = False
if _BUNDLE_HINTS:
    import mission_01_go_out_and_turn
    import mission_02_come_back_home

MENU_ITEMS = [
    {"display": 1, "module": "mission_1", "function": "main"},
]
