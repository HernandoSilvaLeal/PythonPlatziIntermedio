def run():
    my_list = []
    my_dict = {"firstname":"hernando", "lastname":"Silva"  }

    super_liston = [
        {"firstname":"hernando", "lastname":"Silva"  },
        {"firstname":"Julian", "lastname":"Jimenez"  },
        {"firstname":"Fernando", "lastname":"Gonzalez"  },
        {"firstname":"Marcos", "lastname":"Murcia"  },
        {"firstname":"Ben", "lastname":"Lopez"  }
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "floating_nums": [1,2,3,4,5]
    }

    for key, value in super_dict.items():
        print(key,"-",value)

    for i in super_liston:
        print(i.items())


if __name__=='__main__': # Aqui esta el entry point de python
    run()
