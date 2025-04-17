def checkmateBoard(dis=None, low=None):
    if dis is None or low is None:
        return  
    
    for b in range(low):
        string = ''
        for i in range(dis):
            if (i + b) % 2:
                string += 'X'
            else:
                string += '_'
        print(string)
