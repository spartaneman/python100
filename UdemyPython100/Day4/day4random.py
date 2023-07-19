import random 
#importing a module 
import my_module

#get random integer: second parameter inclusive
random_int = random.randint(1,15)

#get random float between 0 and 1 (1 exclusive)
ran_f = random.random()

#if we want a random float that is say between 10 and 20 then we 
#must add the base and multiply the top 
ran_f2 = random.random() * 20 + 10 


print(my_module.paper)

print(ran_f2)