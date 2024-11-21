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

    tv.power()
    if not tv._status:
        print("YES")
    else:
        print("NO")

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    if tv._channel == 1:
        print("YES")
    else:
        print("NO")

    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    if tv._channel == Television.MIN_CHANNEL:
        print("YES")
    else:
        print("NO")

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    if tv._channel == Television.MIN_CHANNEL:
        print("YES")
    else:
        print("NO")

    tv._channel = Television.MAX_CHANNEL
    tv.channel_down()
    if tv._channel == 2:
        print("YES")
    else:
        print("NO")

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    if tv._volume == 1:
        print("YES")
    else:
        print("NO")

    tv._volume = Television.MAX_VOLUME
    tv.volume_up()
    if tv._volume == Television.MAX_VOLUME:
        print("YES")
    else:
        print("NO")

def test_volume_down():
    tv = Television()
    tv.power()
    if tv._volume == 0:
        print("YES")
    else:
        print("NO")

    tv.volume_down()
    if tv._volume == 0:
        print("YES")
    else:
        print("NO")

def test_mute():
    tv = Television()
