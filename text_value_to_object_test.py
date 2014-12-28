import csvp



test = [
    { 'entry':'#2+3#', 'globals':{'red':5}},
    { 'entry':'The number of the beast is #red+4#', 'globals':{'red':5}},
    { 'entry':'#len(string)# is a really nice number', 'globals':{'red':5,'string':"hello world"}}
    ]
i=0

for assay in test:
    print("test "+ repr(i))
    field=process.Field()
    text=field.text_value_to_object(assay['entry'],assay['globals'])
    if len(field.errors):
        print(field.errors)
    print(text)
    i=i+1
    
