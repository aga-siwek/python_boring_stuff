from pathlib import Path
import os
p = Path.cwd() / Path("ch04_list", "list.py")

#os getsize 

print(os.path.getsize(p))
print(os.path.getsize(Path.cwd()))


#os listdir
print(os.listdir(Path.cwd()))