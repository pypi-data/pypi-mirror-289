import pythonbasic as pb

factors = pb.List("FTR", "{0}")

N = 0
def get_factors():
    
    pb.Disp("Integer?")
    pb.Prompt(N)

    I = 1
    while I < pb.abs(N)/2:
        R = N/I

        if factors.contains_number(R):
            I = pb.abs(N)

        if pb.fPart(R) == 0 and pb.Not(factors.contains_number(R)):
            factors.append(R)
            factors.append(I)
            factors.append(R*-1)
            factors.append(I*-1)
        
        I += 1

    pb.ClrHome()
    factors.remove_index(1)

    M = pb.dim(factors.get_list())
    I = 1

    # P represents the "page" of factors being displayed to the user. Each page holds 32 factors, in 16 pairs of 2.
    # U represents the final page of factors. If we have 70 factors, U will be 2, as pages 0 and 1 will be filled
    # with the first 64 factors, and the remaining 6 will be on page 2.
    P = 0
    U = M/32
    if pb.fPart(U) == 0:
        U -= 1
    U = pb.floor(U)

    pb.Lbl("AA")
    pb.ClrHome()

    pb.Output(1, 1, "FACTORS OF")
    pb.Output(1, 12, N)
    pb.Output(10, 1, "ENTER TO CLOSE")
    if M > 32:
        if P != 0:
            pb.Output(1, 22, "PRV ^")
        if P != U:
            pb.Output(10, 22, "NXT v")

    if P < 0:
        P = 0
    if M < U:
        P = U
    
    I = P*32+1
    R = 2

    if M-I > 32:
        # This means more than 32 factors are still left to be displayed, so we will put 32 onto this page
        while I < P*32+32:
            # Display this page of factors
            pb.Output(R,1,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
            I += 2

            if M-I >= 1:
                pb.Output(R,14,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
                I += 2
                R += 1
            
        K = 0   
        while K == 0:
            Q = pb.getKey()
            if Q == 25 and P != 0:
                # 25 corresponds to the up arrow key
                P -= 1
                K = Q
                pb.goto_label("AA")
            if Q == 34 and P != U:
                # down arrow pressed
                P += 1
                K = Q
                pb.goto_label("AA")
            if Q == 105:
                # enter key pressed
                K = Q
                pb.ClrHome()
                pb.Stop()
    else:
        while I < M:
            pb.Output(R,1,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
            I += 2

            if M - I >= 1:
                pb.Output(R,14,"("+pb.toString(factors.get_index(I))+", "+pb.toString(factors.get_index(I+1))+")")
                I += 2
                R += 1
        
        if P != 0:
            K = 0   
            while K == 0:
                Q = pb.getKey()
                if Q == 25 and P != 0:
                    # 25 corresponds to the up arrow key
                    P -= 1
                    K = Q
                    pb.goto_label("AA")
                if Q == 34 and P != U:
                    # down arrow pressed
                    P += 1
                    K = Q
                    pb.goto_label("AA")
                if Q == 105:
                    # enter key pressed
                    K = Q
                    pb.ClrHome()
                    pb.Stop()
            
        pb.Pause()
        pb.ClrHome()
        pb.Stop()

pb.setup(globals(), __file__, get_factors)