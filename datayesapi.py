def get_datayes_token():
    file_obj = open("/home/byhankswang/.datayestoken", 'r')
    token = file_obj.readline()
    print(type(token))
    print(token)