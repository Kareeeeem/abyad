def join(*ws):
    return ('').join(ws)


visible_ws = {
    ' ': '[SPACE]',
    '\t': '[TAB]',
    '\n': '[LF]',
}


def print_ws(ws):
    visible = (' ').join([visible_ws[char] for char in ws])
    print visible
