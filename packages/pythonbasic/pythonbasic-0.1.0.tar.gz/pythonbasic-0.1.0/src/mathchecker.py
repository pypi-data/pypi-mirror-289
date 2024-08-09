import math
import numpy
import re
import pythonbasic as pb
import sys


def APStatistics(option): # Where option is any menuOption in the AP Stats Menu
    if option == "Formula Sheet":
        X = pb.dayOfWk(2024,6, 13)
        pb.disp(X)
    if option == "Z-Score":
        pb.goToLabel(zscore_menu.getLabel())
    if option == "Quit":
        pb.Stop()


def ZScore(option):
    D = 0
    M = 0
    S = 0
    Z = 0
    if (option == "Z-Score"):
        pb.clrHome()
        pb.disp("Data Point?")
        pb.Prompt(D)
        pb.disp("Mean?")
        pb.Prompt(M)
        pb.disp("SD?")
        pb.Prompt(S)
        pb.clrHome()
        pb.output(5,1,"Z-Score:")
        pb.output(6,1,(D - M) / S)
        pb.pause()
        pb.goToMenu(main_menu)
    if(option == "Data Point"):
        pb.clrHome()
        pb.disp("Z-Score?")
        pb.Prompt(Z)
        pb.disp("Mean?")
        pb.Prompt(M)
        pb.disp("SD?")
        pb.Prompt(S)
        pb.clrHome()
        pb.output(5,1,"Data Point:")
        pb.output(6,1,(Z * S) + M)
        pb.pause()
        pb.goToMenu(main_menu)
    if(option == "Mean"):
        pb.clrHome()
        pb.disp("Data Point?")
        pb.Prompt(D)
        pb.disp("Z-Score?")
        pb.Prompt(Z)
        pb.disp("SD?")
        pb.Prompt(S)
        pb.clrHome()
        pb.output(5,1,"Mean:")
        pb.output(6,1,math.sqrt(((Z * S) - D) / -1))
        pb.pause()
        pb.goToMenu(main_menu)
    if option=="Standard Deviation":
        X = 0
        pb.fMax(pb.sin(X) * pb.cos(X),X,0,3)

        pb.disp(pb.abs(-4))
        pb.clrHome()
        pb.output(5,1, pb.dayOfWk(2024, pb.dayOfWk(2024, pb.abs(-6), 15), pb.dayOfWk(2024, 8, 4)))
        pb.pause()
        pb.goToMenuTitle(main_menu.getTitle())
    if(option =="Back"):
        pb.PlotScatter(1, pb.L1, pb.L2, "▫")
        pb.goToMenuTitle(main_menu.getTitle())



main_menu = pb.Menu("AP Statistics", APStatistics, 
                    [pb.MenuOption("Formula Sheet"), pb.MenuOption("Z-Score"), pb.MenuOption("Quit")])

zscore_menu = pb.Menu("Z-Score", ZScore,
                      [pb.MenuOption("Z-Score"), pb.MenuOption("Data Point"), pb.MenuOption("Mean"), 
                       pb.MenuOption("Standard Deviation"), pb.MenuOption("Back")])

pb.setup(globals(), __file__)