import os
import random
def createTrainvalTxt(baseDirDataSet):
    buffer = ''
    baseDir = baseDirDataSet+'/training_images'
    for (idx,folder) in enumerate(os.listdir(baseDir)):
        dataset =  ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        if folder in dataset:
            idx = dataset.index(folder)
        newBase = baseDir + '/' + folder
        print(folder)
        for filename in os.listdir(newBase):
            name, extension = os.path.splitext(filename)
            s = 'training_images/'+ folder +'/'+name+  '.png' + ' ' + str(idx)
            img_file, anno = s.strip("\n").split(" ")
            s += '\n'
            buffer += s
        with open(baseDirDataSet+'/ftrain.txt', 'w') as file:
            file.write(buffer)  
         
        if folder == 'Z':
            break 
    print("Finished creating training val. Now randomizing")
    with open('ftrain.txt','r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open('training_index.txt','w') as target:
        for _, line in data:
            target.write( line )
#Usage

base = os.getcwd()
createTrainvalTxt(base)
