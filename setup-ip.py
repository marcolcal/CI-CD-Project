import commands

def main(target):
    with open("hosts") as f:
        lines = f.readlines()
    edit_next_line = False
    for line in lines:
        line = line.rstrip('\n')
        if edit_next_line:
            ip = commands.getoutput(''' vagrant ssh %s -c "ip addr show | grep -o inet.10.*/" ''' % target)
            ip = [line.strip() for line in ip.strip().split('\n') if '10.' in line]
            import pdb; pdb.set_trace()
            ip = ip[-1].replace("inet ", "").replace("/", "")
            line = line.split()
            line = [ip] + line[1:]
            line = " ".join(line)
            edit_next_line = False
        elif target in line:
            edit_next_line = True
        print line

if __name__ == "__main__":
    import sys
    main(sys.argv[-1])
