from datetime import datetime

def fecha():
    nombrefecha = datetime.now().strftime("%Y-%m-%d")
    print("La fecha es {}".format(nombrefecha))
    