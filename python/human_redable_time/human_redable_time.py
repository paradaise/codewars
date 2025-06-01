def make_readable(seconds:int)->str: 
    hours = seconds // 3600
    remaning_after_hours = seconds % 3600
    minutes = remaning_after_hours // 60
    seconds = remaning_after_hours % 60

    return ( f"{hours:02d}:{minutes:02d}:{seconds:02d}")


make_readable(0)
make_readable(59)
make_readable(3599)
make_readable(3600)
make_readable(86399)
make_readable(86400)
make_readable(359999)