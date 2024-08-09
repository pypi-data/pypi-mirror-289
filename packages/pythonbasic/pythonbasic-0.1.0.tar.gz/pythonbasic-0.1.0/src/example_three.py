import pythonbasic as pb

def normal_probability():
    pb.ClrHome()
    pb.Disp("Lower bound?")
    pb.Prompt(L)
    pb.Disp("Upper bound?")
    pb.Prompt(U)
    pb.Disp("Mean?")
    pb.Prompt(M)
    pb.Disp("Standard deviation?")
    pb.Prompt(S)
    P = pb.normalcdf(L, U, M, S)
    pb.Disp(P)

pb.setup(globals(), __file__, normal_probability)