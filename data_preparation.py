import os
import numpy as np
from pathlib import Path
import pandas as pd

if __name__ == "__main__":
    root = Path('C:/Users/Hi/OneDrive - University of Oulu and Oamk/Documents/EBDS/Python for data statistics') #Path.cwd()
    prime_dir = root / "Persons"
    prime_dir.mkdir(parents=True, exist_ok=True)

    celebrity_names = [
        "Tom Cruise", "Scarlett Johansson", "Brad Pitt", "Angelina Jolie", 
        "Leonardo DiCaprio", "Jennifer Lawrence", "Chris Hemsworth", "Emma Watson", 
        "Johnny Depp", "Natalie Portman", "Dwayne Johnson", "Gal Gadot", 
        "Robert Downey Jr.", "Meryl Streep", "Chris Evans", "Charlize Theron", 
        "Will Smith", "Sandra Bullock", "Ryan Reynolds", "Anne Hathaway", 
        "Keanu Reeves", "Julia Roberts", "Hugh Jackman", "Reese Witherspoon", 
        "Matt Damon", "Nicole Kidman", "George Clooney", "Cameron Diaz", 
        "Mark Wahlberg", "Emma Stone", "Samuel L. Jackson", "Margot Robbie", 
        "Christian Bale", "Amy Adams", "Tom Hanks", "Zendaya", 
        "Morgan Freeman", "Viola Davis", "Ryan Gosling", "Salma Hayek", 
        "Daniel Craig", "Cate Blanchett", "Jake Gyllenhaal", "Rihanna", 
        "Chris Pratt", "Beyoncé", "Henry Cavill", "Ariana Grande", 
        "Timothée Chalamet", "Taylor Swift", "Eddie Redmayne", "Lady Gaga", 
        "Michael B. Jordan", "Billie Eilish", "Benedict Cumberbatch", "Drake", 
        "Jason Momoa", "Ed Sheeran", "Joaquin Phoenix", "The Weeknd", 
        "Idris Elba", "Selena Gomez", "Adam Driver", "Kendrick Lamar", 
        "Liam Neeson", "Shakira", "Paul Rudd", "Dua Lipa", 
        "Harrison Ford", "Katy Perry", "Orlando Bloom", "Justin Bieber", 
        "Hugh Grant", "Camila Cabello", "Javier Bardem", "Adele", 
        "Ben Affleck", "Shawn Mendes", "Jared Leto", "Miley Cyrus", 
        "Steve Carell", "Nicki Minaj", "Jonah Hill", "Post Malone", 
        "Jeff Goldblum", "Gigi Hadid", "Zac Efron", "Bella Hadid", 
        "Robert Pattinson", "Kylie Jenner", "Andrew Garfield", "Kanye West", 
        "Joseph Gordon-Levitt", "Kim Kardashian", "Ashton Kutcher", "Billie Piper", 
        "Sofia Vergara", "Chris Pine", "Eva Longoria", "Christopher Nolan"]
    
    scientist_names = [
        "Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin", 
        "Nikola Tesla", "Galileo Galilei", "Stephen Hawking", "Leonardo da Vinci", 
        "Carl Sagan", "Richard Feynman", "Rosalind Franklin", "James Watson", 
        "Francis Crick", "Gregor Mendel", "Alan Turing", "Niels Bohr", 
        "Alexander Fleming", "Louis Pasteur", "Dmitri Mendeleev", "Michael Faraday", 
        "Johannes Kepler", "Erwin Schrödinger", "Max Planck", "Werner Heisenberg", 
        "John von Neumann", "Ada Lovelace", "Blaise Pascal", "Archimedes", 
        "Aristotle", "Euclid", "Alfred Nobel", "Thomas Edison", 
        "Enrico Fermi", "J. Robert Oppenheimer", "Linus Pauling", "Guglielmo Marconi", 
        "Edward Jenner", "Rachel Carson", "Barbara McClintock", "Jane Goodall", 
        "Emmy Noether", "C.V. Raman", "Srinivasa Ramanujan", "Katherine Johnson", 
        "Benjamin Franklin", "Hans Bethe", "John Dalton", "Michael Servetus", 
        "Henrietta Leavitt", "Carl Linnaeus", "André-Marie Ampère", "Hedy Lamarr", 
        "Lise Meitner", "Al-Khwarizmi", "Avicenna", "Mary Anning", 
        "Rene Descartes", "Johann Wolfgang von Goethe", "Hans Christian Ørsted", "Pierre Curie", 
        "Paul Dirac", "E.O. Wilson", "Edward Teller", "Maurice Wilkins", 
        "Frederick Sanger", "Heike Kamerlingh Onnes", "George Washington Carver", "Jocelyn Bell Burnell", 
        "Hypatia", "Ernest Rutherford", "Christian Doppler", "John Logie Baird", 
        "Tim Berners-Lee", "John Bardeen", "Marie Tharp", "Maxwell Planck", 
        "Nicolaus Copernicus", "Robert Boyle", "Antoine Lavoisier", "Georg Ohm", 
        "Hans Geiger", "Robert Hooke", "Stephen Jay Gould", "Henri Becquerel", 
        "Georges Cuvier", "Friedrich Wohler", "Annie Jump Cannon", "Thomas Hunt Morgan", 
        "Jacques Cousteau", "Alfred Wegener", "James Clerk Maxwell", "Florence Nightingale", 
        "Har Gobind Khorana", "Subrahmanyan Chandrasekhar", "Vera Rubin", "Neil deGrasse Tyson", 
        "Meghnad Saha", "Edward Witten", "Mario Molina", "Ahmed Zewail"
    ]
    
    other_names  = [
        "Aino Virtanen", "James Smith", "Erik Andersson", "Ole Hansen", "Mikkel Jensen",
        "Sean O'Connor", "Olavi Korhonen", "Mary Johnson", "Johan Johansson", "Kari Johansen",
        "Sofie Nielsen", "Siobhan Murphy", "Eero Nieminen", "John Brown", "Karin Karlsson",
        "Lars Olsen", "Jens Pedersen", "Patrick O'Brien", "Liisa Mäkinen", "Patricia Williams",
        "Elin Nilsson", "Ingrid Larsen", "Frederik Christiansen", "Aisling Kelly", "Pekka Hämäläinen",
        "Robert Jones", "Anders Olsson", "Knut Andersen", "Kirsten Nilsen", "Liam Walsh",
        "Marja Laine", "Jennifer Miller", "Sara Larsson", "Anne Nilsen", "Mathilde Andersen",
        "Caitlin Ryan", "Matti Korhonen", "Michael Brown", "Björn Johansson", "Per Hansen",
        "Lotte Christiansen", "Conor O'Connor", "Anna Nieminen", "Linda Jones", "Maja Andersson",
        "Astrid Johansen", "Magnus Pedersen", "Aoife Murphy", "Tapio Virtanen", "Barbara Smith"
    ]
    
    names = celebrity_names + scientist_names

    for i, fullname in enumerate(names):
        if i ** 0.5 == int(i ** 0.5):            
            fullname = prime_dir / f"{fullname}.txt"
            np.savez_compressed(fullname, n=np.array([0, 1, 2]))
            if not os.path.isfile(fullname):
                os.rename(str(fullname) + '.npz', str(fullname))
        else:            
            fullname_split = fullname.split(" ")
            record = {}
            if len(fullname_split) == 1:
                record = {'First name': '', 'Last name': fullname_split[0]}
            elif len(fullname_split) == 2:
                record = {'First name': fullname_split[0], 'Last name': fullname_split[1]}
            else:
                record = {'First name': ' '.join(fullname_split[:-1]), 'Last name': fullname_split[-1]}
            pd.DataFrame([record]).to_csv(prime_dir / f"{fullname}.txt", index=False, header=False)
            # (prime_dir / f"{fullname}.txt").touch()
            
