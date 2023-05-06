def sorting_cheeses(**cheese):
    result = []
    cheese = dict(sorted(cheese.items(), key=lambda x: (-len(x[1]), x[0])))
    for key, value in cheese.items():
        result.append(key)
        value.sort()
        for i in value[::-1]:
            result.append(i)
    return "\n".join([str(i) for i in result])
  
  #test: print(sorting_cheeses(Parmesan=[102, 120, 135],  Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125]))
