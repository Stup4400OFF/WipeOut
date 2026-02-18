import subprocess

quotes = [
    '“Two things are infinite: the universe and human stupidity; and I`m not sure about the universe.” ― Albert Einstein',
    '“Be who you are and say what you feel, because those who mind don`t matter, and those who matter don`t mind.” ― Bernard M. Baruch',
    '“You know you`re in love when you can`t fall asleep because reality is finally better than your dreams.” ― Dr. Seuss',
    '“You only live once, but if you do it right, once is enough.” ― Mae West'
]
def help_me(default="core/"):
    with open(f"{default}help.txt", "r") as f:
        new = f.read()
    return new

def get_tree():
    output = subprocess.run("tree DATA/sys /F", capture_output=True, shell=True, text=True)
    return "".join(output.stdout.splitlines(keepends=True)[3:])

num = ["1","2","3","4","5","6","7","8","9","0"]