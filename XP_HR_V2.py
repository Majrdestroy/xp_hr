print('This program helps you find out how much XP is needed to meet your current goal!')
print('You must use positive whole numbers as your response or else this program will not work. \nThis program will do the math for you.')

print('')
print('')
print('')

print('WARNING: You will have to find out a couple of inputs for this calculator to work.')

print('')
print('')

print('The first thing you will need to find out is how much time it takes to complete one rotation of your task.')


print("")
print("")

print('The best way to do this is with a timer and a calculator. \nTime yourself for one rotation of your skill. This should be at the speed you plan on doing it. \nIf you want to AFK, then time it like you are afking. This will give you your best average time.')

print('')
print('') 







starting_exp = input("How much XP did you start with in the skill you are training? ")







if(starting_exp.isdigit()):
        
        print("")
else:
        print("")
        print("Please enter a positive numerical value.")
        input('Press ENTER to exit and restart the program.')
        import sys
        sys.exit()


        
        
        
        
print('') 
print('') 

print("The length of your task should be from one point back to the same point.")

print("")
print("")

print('############FOR EXAMPLE: If you are woodcutting, and you start at the tree with \n an empty inventory, your time should stop there also.')










length_rot = input('How long did it take to do one rotation of your task (in seconds)? ')

if(length_rot.isdigit()):
        
        print("")
else:
        print("")
        print("Please enter a positive numerical value.")
        input('Press ENTER to exit and restart the program.')
        import sys
        sys.exit()    
            
print("")
print("")






final_exp = input('What was your final XP count after one rotation? ')

print("")

if(final_exp.isdigit()):
        
        print("")
else:
        print("")
        print("")
        print("Please enter a positive numerical value.")
        input('Press ENTER to exit and restart the program.')
        import sys
        sys.exit()

xpgoal = input('How much XP until you reach your goal? ')

    
if(xpgoal.isdigit()):
        
        print("")
else:
        print("")
        print("")
        print("Please enter a positive numerical value.")
        input('Press ENTER to exit and restart the program.')
        import sys
        sys.exit()
        
        

        
exp_rot = (float(final_exp)-float(starting_exp))  

rot_hr = ((216000/float(length_rot))/60)

xp_hr = (float(rot_hr)*float(exp_rot))

xp_min = (float(xp_hr)/60)

time_to_goal = (float(xpgoal)/float(xp_hr))

                
print("This is your XP per hour: %s XP/hr." % float(xp_hr))
                
print("This is your time to goal: %s hours." % float(time_to_goal))
                

    
input('Thank you! Press ENTER to exit.')
import sys
sys.exit()