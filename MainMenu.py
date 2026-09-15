#This is the main menu code for running multiple missions on the Spike Prime Hub.
#This code is taken directly from the Pybricks tutorial

from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3")

# Based on the selection, run a program.
if selected == "1":
    import T1
elif selected == "2":
    import hello_world
elif selected == "3":
    import T1

