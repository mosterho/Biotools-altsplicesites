import sys, argparse

def cheeseshop(kind, *arguments, **keywords):
#def cheeseshop(kind, arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print('arguments: ', arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print('\n within proc, print args and keywords ', arguments, '  ', keywords)


print('The length of arguments is: ', len(sys.argv))

### see argparse
print('\nBegin argparse stuff')
inp_parser = argparse.ArgumentParser(description="learn all kinds of things about arguments and cheeseshop")
inp_parser.add_argument("kind", help="the kind of cheese")
inp_parser.add_argument("-a", "--arguments", help="extra arguments to display", nargs='*')
#inp_parser.add_argument("-v", "--verbose", help="Some kind of verbose thingy", action="store_true")
inp_parser.add_argument("-v", "--verbose", help="Some kind of verbose thingy", action="count", default=0)
rslt_parser = inp_parser.parse_args()
print('arg parser values ', inp_parser, '\nFull rslt_parser ', rslt_parser, '\nindividual ', rslt_parser.kind)


print('\nBegin cheeseshop portion of script')
cheeseshop(rslt_parser.kind, "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

cheeseshop(rslt_parser.kind, rslt_parser.arguments,
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
