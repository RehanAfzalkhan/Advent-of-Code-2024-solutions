from re import findall
a, b, c, *prog = [int(n) for n in findall("(\d+)", open("inputs/d17input.txt").read())]

def run(prog, a):
    ip, b, c, out = 0, 0, 0, []
    while ip>=0 and ip<len(prog):
        lit, combo = prog[ip+1], [0,1,2,3,a,b,c,99999][prog[ip+1]]
        match prog[ip]:
            case 0: a = int(a / 2**combo)       # adv
            case 1: b = b ^ lit                 # bxl
            case 2: b = combo % 8               # bst
            case 3: ip = ip if a==0 else lit-2  # jnz
            case 4: b = b ^ c                   # bxc
            case 5: out.append(combo % 8)       # out
            case 6: b = int(a / 2**combo)       # bdv
            case 7: c = int(a / 2**combo)       # cdv
        ip+=2
    return out
print("Part 1:", ",".join(str(n) for n in run(prog, a)))

target = prog[::-1]
def find_a(a=0, depth=0):
    if depth == len(target):
        return a
    for i in range(8):
        output = run(prog, a*8 + i)
        if output and output[0] == target[depth]:
            if result := find_a((a*8 + i), depth+1): 
                return result
    return 0
print("Part 2:", find_a())