"""
utils.py — Validation helpers and UI utilities for the Shopping Cart System
"""


# ── Input Helpers ─────────────────────────────────────────────────────────────

def safe_input(prompt: str) -> str:
    """
    Wrapper around input() that re-raises KeyboardInterrupt cleanly
    (prints a newline first so the console prompt isn't left dangling).
    """
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print()          # move cursor to next line
        raise            # let the caller / main loop handle it

