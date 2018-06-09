target = "tu1|\h+&g\OP7@% :BH7M6m3g="
ok = "t "
res = "t"
from subprocess import Popen, PIPE
def call(s):
    proc = Popen(['./Much'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    out, err = proc.communicate(s + '\n')
    return out
assert call(ok) == res

while res != target:
    for i in range(ord('!'), ord('~')):
        r = call(chr(i) + ok)
        if r in target:
            res = r
            ok = chr(i) + ok
            print(ok)
            break

