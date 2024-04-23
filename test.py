STRANGE_STRING = 'foo'

up_and_down = STRANGE_STRING.upper().lower()
orig_len = len(STRANGE_STRING)
up_down_len = len(up_and_down)

print(up_down_len > orig_len)
