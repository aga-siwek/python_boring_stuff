from pathlib import Path
import os
p = Path.cwd() / Path("ch04_list")

print(p.glob("*")) #if we want see the catalogue we have to list 
print(list(p.glob("*")))

print(list(p.glob("task*"))) #* 0 or more
print(list(p.glob("task?"))) # ? 0 or 1 in this case nothing
print(list(p.glob("task_tic_tac_toe_aga_version_?.py")))
print(list(p.glob("task_*_version_?.py"))) #we can connect * and ? 

#we can conect with for to see a better data print 


for text_file_path in p.glob("*.py"):
    print(text_file_path)