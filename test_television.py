from television import Television

def test_init():
    tv = Television()
    if not tv._status:
        print("YES")
    else:
        print("NO")

    if not tv._muted:
        print("YES")
    else:
        print("NO")

    if not tv._volume == Television.MIN_VOLUME:
        print("YES")
    else:
        print("NO")

    if not tv._channel == Television.MIN_CHANNEL:
        print("YES")
    else:
        print("NO")

def test_power():
    tv = Television()
    tv.power()
    if tv._status:
        print("YES")
    else:
        print("NO")
def test_channel_up():
    tv = Television()

def test_channel_down():
    tv = Television()

def test_volume_up():
    tv = Television()

def test_volume_down():
    tv = Television()

def test_mute():
    tv = Television()
