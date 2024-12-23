# Exercise 1: ----------------------------------------------------------------
x: int = 5
y: int = 10
z: int = 15

print(x < 5 and y > x, x < 5 or y > x, x > 3 or y < 10 and z == 15, not(x > 3) and x != z or x + y == z)
# ----------------------------------------------------------------------------



# Exercise 2: ----------------------------------------------------------------
def transform(x: int) -> int:
    if x % 2 == 0:
        return x / 2
    else:
        return (x * 3) - 1
# ----------------------------------------------------------------------------


# Exercise 3: ----------------------------------------------------------------
def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate > 40:
        first_40: int = 400
        return first_40 + (ore_lavorate - 40) * 15
    else:
        return ore_lavorate * 10
# ----------------------------------------------------------------------------



# Exercise 4: ----------------------------------------------------------------
def print_seq(): 
    
    print("Sequenza a):")
    for a in range(1, 8, 1):
        print(a)
    print()

    print("Sequenza b):")
    for a in range(3, 28, 5): # max range is 28 (23 + 5) becouse each cyckle step is 5
        print(a)
    print()

    print("Sequenza c):")
    for a in range(20, -16, -6): # max range is -16 (-10 -6) becouse each cyckle step is -6
        print(a)
    print()

    print("Sequenza d):")
    for a in range(19, 59, 8): # max range is 59 (51 + 8) becouse each cyckle step is 8
        print(a)
    print()
    
    return
# ----------------------------------------------------------------------------



# Exercise 5: ----------------------------------------------------------------
def integerPower(base: int, esponente: int) -> int:
    try:
        risultato: int = base ** esponente

        return risultato
    except Exception as e:
        print(f"Error: {e}")
# ----------------------------------------------------------------------------



# Exercise 6: ----------------------------------------------------------------
def hypotenuse(lato1: float, lato2: float) -> float:
    return ((lato1 ** 2) + (lato2 ** 2)) ** 0.5
# ----------------------------------------------------------------------------



# Exercise 7: ----------------------------------------------------------------
def list_statistics(numbers: list[int]) -> tuple[int, int, float] :
    return (max(numbers), min(numbers), (sum(numbers) / len(numbers)))
# ----------------------------------------------------------------------------


# Exercise 8: ----------------------------------------------------------------
def seconds_since_noon(ore: int, minuti: int, secondi: int) -> int:
    elapsed_seconds = ore * 3600 + minuti * 60 + secondi
    return elapsed_seconds

def time_difference(ora1: int, minuti1: int, secondi1: int, ora2: int, minuti2: int, secondi2: int) -> int:
    seconds1 = seconds_since_noon(ora1, minuti1, secondi1)
    seconds2 = seconds_since_noon(ora2, minuti2, secondi2)
    difference = abs(seconds2 - seconds1)
    return difference if difference <= 43200 else 86400 - difference
# ----------------------------------------------------------------------------


# Exercise 9: ----------------------------------------------------------------
def rimbalzo() -> None:
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    secondi: int = 0

    while rimbalzi < 5:
        if altezza < 0:
            print(f"Tempo: {secondi} Rimbalzo!")
            rimbalzi += 1
            altezza *= -0.5
            velocita *= -0.5
        else:
            print(f"Tempo: {secondi} Altezza: {altezza}")
            altezza += velocita
            velocita -= 96
        secondi += 1
# ----------------------------------------------------------------------------



# Exercise 10: ----------------------------------------------------------------
def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi: int = 1000  # Spazio totale disponibile in blocchi
    space_left: int = spazio_totale_blocchi

    for file_size in files:
        compressed_size: float = file_size * 0.8
        needed_block: int = round(compressed_size / 512)

        if needed_block > space_left:
            print(f"Non è possibile memorizzare il file di {file_size} byte. Spazio insufficiente.")
            break
        else:
            space_left -= needed_block
            print(f"File di {file_size} byte compresso in {compressed_size} byte e memorizzato. Blocchi usati: {needed_block}. Blocchi rimanenti: {space_left}.")
# ----------------------------------------------------------------------------