import csvp



test = [
    { 'entry':'#2+3#', 'globals':{'red':5}},
    { 'entry':'#red+4#', 'globals':{'red':5}},
    { 'entry':'#len(string)#', 'globals':{'red':5,'string':"hello world"}}
    ]
i=0

print("hello world"+repr(7))
for assay in test:
    print("test "+ repr(i))
    field=process.Field()
    text=field.interpret_python(assay['entry'],assay['globals'])
    print(text)
    i=i+1
    
