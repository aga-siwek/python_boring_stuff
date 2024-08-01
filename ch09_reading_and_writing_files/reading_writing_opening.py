from pathlib import Path
# #new file write and read
p = Path.cwd() / Path("ch09_reading_and_writing_files", "out", "spam.txt")
p.write_text("hello world hakunanana")
print(p.exists())
print(p.read_text())

# open(p)

# p = open(Path.cwd() / Path("ch09_reading_and_writing_files", "spam.txt"))
# print(p.read())

pt = (Path.cwd() / Path("ch09_reading_and_writing_files", "out", "spam2.txt"))
pt.write_text("""
3 dogs
3 cats 
0 human""")
print(pt.read_text())

# ks = open(Path.cwd() / Path("ch09_reading_and_writing_files", "spam2.txt", "r")) #read
# print(ks.readline())

becon_path = Path.cwd() / Path("ch09_reading_and_writing_files", "out", "becon.txt")
ks = open(becon_path, "w") #
ks.write("mamamamam mam am amama")

ks.close()
