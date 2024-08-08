

# debugging mode
IS_DEBUG = False


# Whether it is debugging mode
def is_debug() -> bool:
    return IS_DEBUG


def debug_log(*kwargs, title='start'):
    if is_debug():
        print('=' * 60, title, '=' * 60)
        print(*kwargs)
        # print('=' * 60, 'end', '=' * 60)
        print("\n")


