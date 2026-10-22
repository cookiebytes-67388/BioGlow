#This is the main menu code for running multiple missions on the Spike Prime Hub.
#This code is taken directly from the Pybricks tutorial
#######

from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5", "6")

# Based on the selection, run a program.
if selected == "1":
    import FlipRock_DroneSurvey_1
elif selected == "2":
    import ReachingRoots_Tangled_ExplodingSeeds_2
elif selected == "3":
    import BiocentricArchitecture_3
elif selected == "4":
    import LeafCutterFrenzy_HumongousFungus_ElderCane_4
elif selected == "5":
    import ForestElder_5
elif selected == "6":
    import KeystoneSpecies_WindowPast_6
