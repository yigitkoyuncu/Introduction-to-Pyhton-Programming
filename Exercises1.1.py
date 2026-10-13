#1.1 Exercises (Your First Program)

# 1st Question
# Modify useargument.py to compose a program that takes three names and writes a proper sentence with the names in the
# reverse of the order they are given, so that, for example, python usethree.py Alice Bob Carol writes the string
# 'Hi Carol, Bob, and Alice'.

import stdio
import sys
stdio.write("Hi, ")
stdio.write(sys.argv[3])
stdio.write(", ")
stdio.write(sys.argv[2])
stdio.write(" and ")
stdio.write(sys.argv[1])

#I give input in anaconda prompt.And code is worked on there.

# 2nd Question
#Compose a program that writes your initials using nine rows of asterisks like the one below.
# **        ***    **********      **             *             **
# **      ***      **        **     **           ***           **
# **    ***        **         **     **         ** **         **
# **  ***          **          **     **       **   **       **
# *****            **          **      **     **     **     **
# **  ***          **          **       **   **       **   **
# **    ***        **         **         ** **         ** **
# **      ***      **        **           ***           ***
# **        ***    **********              *             *

stdio.writeln('**        ***    **********      **             *             **')
stdio.writeln('**      ***      **        **     **           ***           ** ')
stdio.writeln('**    ***        **         **     **         ** **         **  ')
stdio.writeln('**  ***          **          **     **       **   **       **   ')
stdio.writeln('*****            **          **      **     **     **     **    ')
stdio.writeln('**  ***          **          **       **   **       **   **     ')
stdio.writeln('**    ***        **         **         ** **         ** **      ')
stdio.writeln('**      ***      **        **           ***           ***       ')
stdio.writeln('**        ***    **********              *             *        ')
