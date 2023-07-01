from translucenttb import blur
from time import sleep
def colorful():
    hexdict = ['#FF0000', '#FF3030', '#FF5656', '#FF7456', '#FFA500', '#FF7438', '#FF8956', '#FFAB56', '#FFB871', '#FFFF00', '#FFCD71', '#FFE071', '#FFF571', '#F4FF71', '#D8FF71', '#C8FF71', '#008000', "#9FF65B", '#00FFFF', '#79F65B', '#5FF65B', '#5BF67D', '#5BF69C', '#5BF67D','#5BF6C5', '#5BF6DC', '#2AFFDC', '#2AFCFF', '#2AC5FF', '#2AADFF', '#2A87FF', '#2A6BFF', '#2A49FF', '#0000FF','#2A35FF', '#3A2AFF', '#502AFF', '#602AFF', '#800080']

    for hexcolor in hexdict:
        blur("noeffect", hexcolor)
        sleep(0.1)
		
colorful()
