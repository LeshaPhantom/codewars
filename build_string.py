def build_string(*args):
    return "I like {}!".format(",".join(args))


print(build_string('Cheese','Milk','Chocolate'))
