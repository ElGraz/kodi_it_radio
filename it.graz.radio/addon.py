import os
import sys
import urllib
import urlparse
import xbmcaddon
import xbmcgui
import xbmcplugin

cap_live_m3u = "https://radiocapital-lh.akamaihd.net/i/RadioCapital_Live_1@196312/index_96_a-p.m3u8?sd=10&rebase=on"
addon_handle=None


def build_url(query):
    base_url = sys.argv[0]
    return base_url + '?' + urllib.urlencode(query)


def build_song_list(m3us):
    # iterate over the contents of the dictionary songs to build the list
    for m3u in m3us:
        li = xbmcgui.ListItem(label=m3u['title'])
        li.setIsFolder(False)
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), build_url(m3u['url']), li)

    xbmcplugin.setContent(addon_handle, 'songs')
    xbmcplugin.endOfDirectory(addon_handle)


def play_song(url):
    # set the path of the song to a list item
    play_item = xbmcgui.ListItem(path=url)
    # the list item is ready to be played by Kodi
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)


def build_elem(title, url):
    return {"title": title, "url": url}


def main():
    m3us = list()
    args = urlparse.parse_qs(sys.argv[2][1:])
    mode = args.get('mode', None)

    # initial launch of add-on
    if mode is None:
        m3us.append(build_elem("Capital live", cap_live_m3u))
        # display the list of songs in Kodi
        build_song_list(m3us)
        # a song from the list has been selected
    elif mode[0] == 'stream':
        # pass the url of the song to play_song
        play_song(args['url'][0])


if __name__ == '__main__':
    addon_handle = int(sys.argv[1])
    main()
