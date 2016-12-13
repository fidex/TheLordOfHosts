import markovify

# Get raw text as string.
f = open('parsedBible.txt','r+')
text = f.read()
fi = open('IStestfile.txt','r+')
text2 = fi.read()
# Build the model.
modelHP = markovify.Text(text)
modelIS = markovify.Text(text2)
modelX  = markovify.combine([modelHP, modelIS],[1,1])

# Print five randomly-generated sentences
for i in range(5):
    print(modelX.make_short_sentence(200))

# Print three randomly-generated sentences of no more than 140 characters
#for i in range(3):
#   print(text_model.make_short_sentence(140))
