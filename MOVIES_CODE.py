#MAIN CODE
import tkinter as tk
from tkinter import messagebox
import csv

def recommend_movies():
    username = username_entry.get()
    genre_name = genre_entry.get()
    
    # Loading movie data from the CSV file
    movie_recommendations = {}
    with open('movies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            genre = row['GENRE']
            title = row['TITLE']
            year = row['YEAR']
            if genre not in movie_recommendations:
                movie_recommendations[genre] = []
            movie_recommendations[genre].append(f"{title} ({year})")
    
    if genre_name in movie_recommendations:
        movies = ", ".join(movie_recommendations[genre_name])
        messagebox.showinfo("Movie Recommendations", f"Hi {username}, here are some movies in the {genre_name} genre: {movies}")
    else:
        messagebox.showinfo("Movie Recommendations", f"Sorry, we don't have movie recommendations for the {genre_name} genre.")

#main window
window = tk.Tk()
window.title("Movie Recommendation System")
window.geometry("400x200")
window.configure(bg="aquamarine")

#labels , buttons
capital_label = tk.Label(window, text="FILL IN CAPITAL LETTERS",bg="black",fg="white")
capital_label.pack()

username_label = tk.Label(window, text="Enter your username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

genre_label = tk.Label(window, text="Enter genre name:")
genre_label.pack()
genre_entry = tk.Entry(window)
genre_entry.pack()

recommend_button = tk.Button(window, text="Recommend Movies", command=recommend_movies)
recommend_button.pack()

# tkinter main loop
window.mainloop()
