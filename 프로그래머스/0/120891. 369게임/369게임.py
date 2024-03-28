def solution(order):
    order = list(str(order))
    clap = 0
    for o in order:
        if o in '369':
            clap += 1
    return clap