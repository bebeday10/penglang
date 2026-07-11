def convert_to_lyrics(lyrics: dict[str, float]) -> list[dict[str, str | float]]:
    song: dict[str, list] = {"song": []}

    for lyric, delay in lyrics.items():
        lyric: str = lyric.split("|")[0]
        song["song"].append(
            {
                "lyric": lyric,
                "delay": delay
            }
        )

    return song

def merge(*lyrics: list[dict[str, str, float]] | dict[str, str, float]) -> dict[str. list]:
    """
    merge multiple lyrics

    # Args:
        *lyrics (list[dict[str, str, float]] | dict[str, str, float]): pieces of the song

    Returns:
        dict: the merged song
    """ 
    song: dict[str, list] = {"song": []}

    for piece in lyrics:
        if isinstance(piece, list):
            song["song"].extend(piece)
        
        if isinstance(piece, dict):
            song["song"].append(piece)

    return song