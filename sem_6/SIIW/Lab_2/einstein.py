from csp import CSP, Constraint


if __name__ == '__main__':
    VAR = [
        ['green', 'blue', 'yellow', 'white', 'red'],
        ['light', 'fajka', 'ment', 'unfiltered', 'cig'],
        ['horse', 'cat', 'dog', 'bird', 'fish'],
        ['nor', 'ang', 'ger', 'szw', 'dun'],
        ['water', 'tea', 'coffee', 'milk', 'beer']
    ]

    def ein_heuristic(key, doms, vars):
        for subvar in VAR:
            if key in subvar:
                l = list(range(1, 6))
                for elem in subvar:
                    if len(doms[elem]) > 0:
                        try:
                            l.remove(doms[elem][0])
                        except:
                            pass
                return l
        return vars


    csp = CSP(
        list(range(1, 6)), 
        { i: list(range(1, 6)) for i in sum(VAR, []) }, 
        [
            # Constraint(['nor'], lambda x: x['nor'][0] == 1),
            # Constraint(['milk'], lambda x: x['milk'][0] == 3),
            Constraint(['ang', 'red'], lambda x: x['ang'][0] == x['red'][0]),
            Constraint(['green', 'white'], lambda x: x['green'][0] == x['white'][0] + 1),
            Constraint(['dun', 'tea'], lambda x: x['dun'][0] == x['tea'][0]),
            Constraint(['green', 'coffee'], lambda x: x['green'][0] == x['coffee'][0]),
            Constraint(['szw', 'dog'], lambda x: x['szw'][0] == x['dog'][0]),
            Constraint(['yellow', 'cig'], lambda x: x['yellow'][0] == x['cig'][0]),
            Constraint(['ger', 'fajka'], lambda x: x['ger'][0] == x['fajka'][0]),
            Constraint(['ment', 'beer'], lambda x: x['ment'][0] == x['beer'][0]),
            Constraint(['bird', 'unfiltered'], lambda x: x['bird'][0] == x['unfiltered'][0]),
            Constraint(['light', 'cat'], lambda x: x['light'][0] == x['cat'][0] + 1 or x['light'][0] == x['cat'][0] - 1),
            Constraint(['light', 'water'], lambda x: x['light'][0] == x['water'][0] + 1 or x['light'][0] == x['water'][0] - 1),
            Constraint(['nor', 'blue'], lambda x: x['nor'][0] == x['blue'][0] + 1 or x['nor'][0] == x['blue'][0] - 1),
            Constraint(['horse', 'yellow'], lambda x: x['horse'][0] == x['yellow'][0] + 1 or x['horse'][0] == x['yellow'][0] - 1)
        ],
        # ein_heuristic
    )

    # csp.solve_backtracking()
    # csp.solve_forward_checking()
    csp.solve_ac3()

    print(csp.sols)