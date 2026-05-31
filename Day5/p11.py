def movie_list(n):
    movie=[]
    
    for i in range(0,n):
         name = input("Enter movie (i+1): ")
         movie.append(name)
       

    return movie

print(movie_list(3))


    