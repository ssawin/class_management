import process



test = [
    { 'entry':'steve.run.bike', 'name':'steve','actions':['run','bike'], 'input_type':'TEXT'},
    { 'entry':'oliver;.game.read', 'name':'oliver','actions':['game','read'], 'input_type':'LIST'},
    { 'entry':'will:.math.geek', 'name':'will','actions':['math','geek'], 'input_type':'DICT'},
    { 'entry':'emma@', 'name':'emma','actions':[], 'input_type':'DATE'},
    { 'entry':'lisa,;,*^', 'error':' "lisa,;,*^" is not a valid header'},
i=0
for assay in test:
    field=process.Field()
    field.entry_to_header(assay['entry'])
    header=field.header
    print("test "+ repr(i))
    for key in keys(header):
       if header[key] == assay[key]:
          print (key+" is good!")
       else:
          print("problem with "+key)
