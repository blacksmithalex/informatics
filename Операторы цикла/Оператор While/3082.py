limit = 10000
Amax, Bmax, N = int(input()), int(input()), int(input())
Acur, Bcur, iter = 0, 0, 0
commands = []
while iter < limit:
    iter += 1
    Acur = Amax
    commands.append('>A')
    if Acur == N:
        print('\n'.join(commands))
        quit()
    else:
        if Bcur + Acur <= Bmax:
            commands.append('A>B')
            Bcur += Acur
            Acur = 0
            if Bcur == N:
                print('\n'.join(commands))
                quit()
        else:
            while Acur > Bmax - Bcur:
                commands.append('A>B')
                Acur -= (Bmax - Bcur)
                Bcur = Bmax
                if Acur == N or Bcur == N:
                    print('\n'.join(commands))
                    quit()
                commands.append('B>')
                Bcur = 0
            commands.append('A>B')
            Acur, Bcur = 0, Acur
            if Bcur == N:
                print('\n'.join(commands))
                quit()
print('Impossible')