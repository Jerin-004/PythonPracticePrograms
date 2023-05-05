## map() = applies a funtion to each item in a iterable (list, tuple, etc.......)

## map(funtion,iterable)

store = [("Shirts",20.00),
        ("PAnts",25.00),
        ("Jacket",50.00),
        ("Socks",10.00)]

to_euros = lambda data : (data[0],round(data[1]*0.82))
to_dollers = lambda data : (data[0],round(data[1]/0.82))


store_euros = list(map(to_euros,store))
store_dollers = list(map(to_dollers,store))

for i in store_dollers:
    print(i)