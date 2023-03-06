# BlackJack Player

## Table of contents

- Description
- Transcript
- Summary

## Description

At its simplest level, a Monte Carlo analysis (or simulation) involves running many scenarios with different random inputs and summarizing the distribution of the results. In this program, we are building an automated blackjack player which bases its decisions on monte-carlo-simulation-derived heuristics contained in a matrix. In this program, we run simulated blackjack games using the hit(), deal() and stand() methods. All these functions make use of randomized decks and cards. In addition, during these simulated games, the actions taken, hit() or stand(), are taken randomly unless the player's hand value is 21. In that case, the player must stand as hitting at 21 would inevitably lead to a bust, which is a loss. Therefore, it is sensible to not randomize that decision as the success rate of hitting in that position is pretty clear. Our approach for the simulation satisfies our random input criterion even though there is one use case where the action taken is not randomized. Then, in order to summarize the results, our second criterion, we populate a matrix organized in the following way: 
- Each column represents a possible dealer face card value
- Each row represents a possible player hand value
- Each address in the matrix contains an array of length 2 containing the number of times the combination [(dealer face card value) x (player hand value)] occurs as well as the number of times hitting was successful. 

In the games played by our independant player, the function hitme() is used to explore the learned matrix. The player feeds its current hand value and current value of the dealer face card to the hitme() function which tells the player whether to hit or stand based on the probability of hitting success derived from the learned matrix. The function hitme() advises to hit when the success rate is greater than 
0.5. The value 0.5 as a hitting success rate threshold seems to be the spot where our automated player is the most successful. Values that were tried ranged from 0.15 to 0.95. The values 0.4, 0.6 and 0.7 did pretty well, but they did not outperform the value 0.5 as a threshold to take the risk of hitting. 

If the combination fed into hitme() was never encountered in the simulations, hitme() advises to hit if the player's hand value is less than 17 and stand otherwise. The latter is a popularized strategy which has proven to work enough and minimizes risks of busting. It is worthy to note that it is not an optimal strategy. However, this strategy is just a precaution in case the number of simulations run is low. If we are running at least 100,000 randomized simulations, this should not occur. 

## Transcript
______________________________________________________________________
1. 100,000 simulations and 100,000 games played 
### Matrix:
*Each column in the matrix is separated by a new line.*

defaultdict({
    1: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [16, 15], 5: [47, 42], 6: [60, 55], 7: [78, 75], 8: [112, 97], 9: [145, 129], 10: [168, 141], 11: [212, 189], 12: [550, 354], 13: [587, 372], 14: [584, 348], 15: [652, 366], 16: [626, 340], 17: [682, 359], 18: [674, 315], 19: [654, 239], 20: [1087, 267], 21: [645, 249]}), 

    2: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [7, 5], 5: [31, 17], 6: [49, 31], 7: [88, 52], 8: [108, 72], 9: [145, 97], 10: [154, 96], 11: [194, 115], 12: [464, 218], 13: [630, 305], 14: [579, 277], 15: [621, 279], 16: [639, 284], 17: [698, 286], 18: [670, 210], 19: [747, 179], 20: [1079, 157], 21: [780, 92]}), 

    3: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [22, 17], 5: [39, 24], 6: [51, 30], 7: [75, 39], 8: [107, 71], 9: [138, 90], 10: [170, 105], 11: [211, 125], 12: [563, 255], 13: [554, 250], 14: [581, 235], 15: [663, 287], 16: [661, 274], 17: [663, 246], 18: [731, 212], 19: [683, 142], 20: [1062, 145], 21: [744, 79]}), 
    
    4: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [19, 10], 5: [50, 31], 6: [47, 23], 7: [104, 57], 8: [117, 70], 9: [133, 82], 10: [168, 83], 11: [188, 105], 12: [541, 256], 13: [598, 260], 14: [610, 224], 15: [600, 234], 16: [660, 268], 17: [712, 257], 18: [665, 189], 19: [699, 149], 20: [1070, 131], 21: [798, 84]}), 
    
    5: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [17, 5], 5: [49, 21], 6: [52, 23], 7: [82, 52], 8: [117, 62], 9: [153, 81], 10: [172, 98], 11: [205, 113], 12: [532, 236], 13: [589, 229], 14: [604, 238], 15: [569, 207], 16: [655, 256], 17: [680, 257], 18: [674, 192], 19: [688, 112], 20: [1049, 104], 21: [733, 73]}), 
    
    6: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [12, 8], 5: [41, 24], 6: [58, 30], 7: [84, 44], 8: [121, 67], 9: [137, 84], 10: [156, 90], 11: [232, 129], 12: [560, 250], 13: [584, 254], 14: [602, 232], 15: [641, 224], 16: [537, 203], 17: [654, 215], 18: [663, 169], 19: [685, 124], 20: [1068, 111], 21: [704, 74]}), 
    
    7: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [17, 10], 5: [49, 35], 6: [63, 42], 7: [102, 68], 8: [115, 81], 9: [144, 107], 10: [175, 125], 11: [210, 154], 12: [555, 296], 13: [603, 333], 14: [675, 346], 15: [654, 321], 16: [603, 310], 17: [648, 297], 18: [673, 136], 19: [717, 100], 20: [1085, 72], 21: [756, 51]}), 
    
    8: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [13, 9], 5: [52, 37], 6: [66, 51], 7: [117, 90], 8: [120, 97], 9: [159, 120], 10: [161, 125], 11: [202, 154], 12: [558, 332], 13: [605, 332], 14: [587, 316], 15: [638, 326], 16: [674, 340], 17: [680, 321], 18: [583, 234], 19: [722, 120], 20: [1089, 92], 21: [770, 52]}), 
    
    9: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [13, 13], 5: [42, 34], 6: [57, 39], 7: [108, 75], 8: [130, 105], 9: [139, 103], 10: [188, 149], 11: [200, 144], 12: [532, 328], 13: [587, 343], 14: [661, 375], 15: [612, 319], 16: [619, 302], 17: [669, 315], 18: [672, 272], 19: [606, 181], 20: [1092, 130], 21: [778, 49]}), 
    
    10: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [72, 52], 5: [201, 160], 6: [244, 193], 7: [405, 322], 8: [501, 400], 9: [574, 448], 10: [675, 526], 11: [845, 674], 12: [2110, 1229], 13: [2434, 1431], 14: [2507, 1405], 15: [2575, 1350], 16: [2571, 1369], 17: [2617, 1271], 18: [2604, 1009], 19: [2766, 884], 20: [3929, 939], 21: [3107, 353]})
})

#### Winning rate
The winning rate is 0.42776 which is about 42.78%. 
______________________________________________________________________

1. 500,000 simulations and 500,000 games played
#### Matrix
*Each column in the matrix is separated by a new line.*

defaultdict({
    1: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [87, 82], 5: [250, 222], 6: [354, 319], 7: [499, 428], 8: [600, 531], 9: [814, 703], 10: [875, 783], 11: [1040, 910], 12: [2732, 1872], 13: [2858, 1847], 14: [3086, 1952], 15: [3136, 1820], 16: [3352, 1910], 17: [3334, 1817], 18: [3372, 1508], 19: [3460, 1202], 20: [5226, 1408], 21: [3294, 1212]}), 
    
    2: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [43, 22], 5: [178, 115], 6: [266, 173], 7: [408, 259], 8: [524, 328], 9: [678, 454], 10: [755, 495], 11: [952, 604], 12: [2544, 1301], 13: [2952, 1373], 14: [3067, 1438], 15: [3373, 1482], 16: [3333, 1468], 17: [3396, 1395], 18: [3382, 1039], 19: [3542, 755], 20: [5477, 793], 21: [3757, 427]}), 
    
    3: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [92, 55], 5: [184, 130], 6: [271, 165], 7: [399, 247], 8: [546, 342], 9: [721, 422], 10: [832, 512], 11: [943, 581], 12: [2661, 1245], 13: [2851, 1349], 14: [2986, 1293], 15: [3405, 1402], 16: [3227, 1270], 17: [3357, 1329], 18: [3475, 1058], 19: [3503, 757], 20: [5253, 744], 21: [3784, 453]}), 
    
    4: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [87, 57], 5: [234, 138], 6: [254, 159], 7: [444, 285], 8: [573, 315], 9: [705, 415], 10: [818, 491], 11: [960, 575], 12: [2656, 1193], 13: [2954, 1315], 14: [2757, 1163], 15: [3168, 1257], 16: [3184, 1216], 17: [3406, 1296], 18: [3298, 944], 19: [3512, 732], 20: [5182, 623], 21: [3792, 418]}), 
    
    5: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [126, 65], 5: [256, 159], 6: [350, 198], 7: [445, 236], 8: [516, 287], 9: [654, 367], 10: [835, 486], 11: [998, 579], 12: [2679, 1185], 13: [3017, 1226], 14: [3040, 1247], 15: [2862, 1128], 16: [3311, 1205], 17: [3422, 1275], 18: [3369, 985], 19: [3353, 618], 20: [5360, 633], 21: [3854, 428]}), 
    
    6: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [94, 55], 5: [249, 142], 6: [358, 194], 7: [501, 292], 8: [558, 325], 9: [715, 418], 10: [817, 478], 11: [998, 568], 12: [2694, 1215], 13: [3061, 1321], 14: [2995, 1206], 15: [3264, 1269], 16: [2952, 1102], 17: [3234, 1191], 18: [3419, 848], 19: [3536, 600], 20: [5291, 579], 21: [3776, 358]}), 
    
    7: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [103, 85], 5: [243, 181], 6: [334, 239], 7: [491, 354], 8: [613, 459], 9: [745, 551], 10: [835, 628], 11: [989, 726], 12: [2723, 1560], 13: [3006, 1599], 14: [3097, 1633], 15: [3170, 1608], 16: [3219, 1519], 17: [3109, 1431], 18: [3358, 733], 19: [3496, 465], 20: [5349, 449], 21: [3886, 271]}), 
    
    8: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [98, 77], 5: [253, 201], 6: [319, 243], 7: [518, 403], 8: [564, 427], 9: [795, 608], 10: [815, 620], 11: [975, 746], 12: [2757, 1588], 13: [3063, 1688], 14: [2938, 1582], 15: [3210, 1665], 16: [3233, 1652], 17: [3360, 1621], 18: [2905, 1148], 19: [3438, 511], 20: [5365, 433], 21: [3778, 274]}), 
    
    9: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [101, 67], 5: [224, 171], 6: [348, 259], 7: [499, 372], 8: [637, 494], 9: [739, 566], 10: [853, 667], 11: [1002, 767], 12: [2696, 1540], 13: [2976, 1760], 14: [3076, 1744], 15: [3337, 1749], 16: [3224, 1656], 17: [3393, 1614], 18: [3440, 1378], 19: [3122, 1045], 20: [5274, 541], 21: [3779, 240]}), 
    
    10: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [367, 285], 5: [910, 717], 6: [1326, 1042], 7: [1990, 1603], 8: [2394, 1894], 9: [3205, 2499], 10: [3520, 2811], 11: [4231, 3320], 12: [10765, 6545], 13: [11885, 6909], 14: [12319, 7075], 15: [12850, 6854], 16: [12672, 6509], 17: [13387, 6646], 18: [13305, 5391], 19: [13782, 4531], 20: [19759, 4721], 21: [15034, 1541]})
})

#### Winning Rate
The winning rate is 0.429272 which is about 42.93%.
______________________________________________________________________

1. 5,000,000 simulations and 5,000,000 games played
#### Matrix
*Each column in the matrix is separated by a new line.*
defaultdict({
    1: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [932, 831], 5: [2445, 2161], 6: [3328, 2957], 7: [4968, 4374], 8: [6064, 5355], 9: [7725, 6776], 10: [8710, 7696], 11: [10588, 9326], 12: [26766, 18044], 13: [30035, 19480], 14: [30398, 18676], 15: [32240, 19014], 16: [32452, 18473], 17: [33245, 17937], 18: [33225, 14816], 19: [34577, 12241], 20: [53150, 14122], 21: [33310, 12044]}), 

    2: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [466, 324], 5: [1759, 1153], 6: [2759, 1841], 7: [4246, 2722], 8: [5303, 3389], 9: [6786, 4364], 10: [8179, 5189], 11: [9807, 6219], 12: [24504, 11969], 13: [29943, 14137], 14: [31284, 14163], 15: [32590, 14081], 16: [32855, 13728], 17: [34115, 13727], 18: [34040, 10273], 19: [35225, 7674], 20: [53017, 7273], 21: [38306, 4568]}), 
    
    3: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [943, 586], 5: [1780, 1091], 6: [2939, 1795], 7: [4400, 2751], 8: [5344, 3290], 9: [6972, 4281], 10: [8101, 4989], 11: [9797, 6025], 12: [27045, 12921], 13: [27721, 12692], 14: [30447, 13255], 15: [32766, 13599], 16: [33088, 13402], 17: [34214, 13297], 18: [33899, 10133], 19: [34410, 7483], 20: [53347, 7174], 21: [38427, 4499]}), 
    
    4: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [934, 529], 5: [2397, 1392], 6: [2673, 1558], 7: [4246, 2464], 8: [5581, 3258], 9: [7029, 4070], 10: [8118, 4724], 11: [9777, 5729], 12: [26940, 12373], 13: [30121, 13057], 14: [27479, 11440], 15: [32352, 12830], 16: [32912, 12749], 17: [33982, 12658], 18: [33726, 9566], 19: [34406, 7094], 20: [53433, 7054], 21: [38656, 4387]}), 
    
    5: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [897, 492], 5: [2425, 1349], 6: [3255, 1775], 7: [4343, 2373], 8: [5267, 2936], 9: [7087, 3928], 10: [8214, 4540], 11: [9826, 5483], 12: [27000, 11790], 13: [29927, 12497], 14: [30659, 12158], 15: [29484, 11247], 16: [32461, 11836], 17: [33586, 12117], 18: [33750, 9330], 19: [34594, 6640], 20: [53278, 6427], 21: [38563, 3989]}), 
    
    6: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [939, 546], 5: [2501, 1421], 6: [3373, 1852], 7: [4885, 2767], 8: [5320, 2990], 9: [7104, 4019], 10: [8189, 4696], 11: [9903, 5700], 12: [27178, 11952], 13: [29791, 12733], 14: [30434, 12373], 15: [31905, 12465], 16: [28887, 10944], 17: [33307, 11878], 18: [33521, 8418], 19: [34506, 6248], 20: [53334, 5856], 21: [38256, 3817]}), 
    
    7: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [906, 664], 5: [2370, 1719], 6: [3390, 2479], 7: [4798, 3514], 8: [6021, 4454], 9: [7050, 5219], 10: [8260, 6077], 11: [9991, 7391], 12: [27343, 15445], 13: [30177, 16368], 14: [30933, 15967], 15: [31781, 15824], 16: [32152, 15823], 17: [30130, 14166], 18: [33492, 7324], 19: [34866, 4702], 20: [52949, 4593], 21: [38479, 2897]}), 
    
    8: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [868, 653], 5: [2408, 1809], 6: [3367, 2557], 7: [4881, 3740], 8: [5943, 4499], 9: [7731, 5976], 10: [8126, 6299], 11: [9929, 7559], 12: [27053, 15835], 13: [30411, 16974], 14: [30284, 16379], 15: [31928, 16436], 16: [32107, 16102], 17: [33583, 16218], 18: [30170, 11663], 19: [34422, 5385], 20: [52931, 4128], 21: [37912, 2577]}), 
    
    9: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [961, 731], 5: [2357, 1815], 6: [3328, 2554], 7: [4933, 3781], 8: [5973, 4626], 9: [7722, 5886], 10: [8817, 6775], 11: [10001, 7676], 12: [27278, 16021], 13: [29776, 17140], 14: [30440, 16641], 15: [32044, 16823], 16: [32219, 16253], 17: [33365, 16057], 18: [33778, 13314], 19: [31026, 10062], 20: [52354, 5351], 21: [38462, 2449]}), 
    
    10: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [3631, 2859], 5: [9741, 7715], 6: [13322, 10452], 7: [19693, 15679], 8: [23710, 18832], 9: [30818, 24403], 10: [34939, 27588], 11: [42564, 33518], 12: [107265, 65893], 13: [119988, 70630], 14: [121882, 68229], 15: [128391, 68494], 16: [128477, 66303], 17: [134192, 66418], 18: [133970, 54220], 19: [137530, 44828], 20: [197583, 47752], 21: [150635, 16162]})
})


#### Winning Rate
The winning rate is 0.4275974 which is about 42.76%.
______________________________________________________________________

1. 10,000,000 simulations and 10,000,000 games played
#### Matrix
*Each column in the matrix is separated by a new line.*
defaultdict({
    1: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1791, 1558], 5: [4773, 4256], 6: [6735, 5971], 7: [9757, 8642], 8: [11781, 10332], 9: [15112, 13315], 10: [17491, 15444], 11: [21340, 18784], 12: [54347, 36478], 13: [59705, 38477], 14: [61269, 37842], 15: [64102, 37717], 16: [64027, 36388], 17: [67192, 36436], 18: [66783, 29769], 19: [69324, 24687], 20: [106264, 27840], 21: [66388, 24098]}),

    2: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [914, 611], 5: [3580, 2303], 6: [5337, 3470], 7: [8466, 5369], 8: [10515, 6806], 9: [13763, 8782], 10: [15956, 10190], 11: [19460, 12409], 12: [48730, 23963], 13: [59671, 28353], 14: [62024, 28326], 15: [65374, 28264], 16: [64882, 26859], 17: [68464, 27456], 18: [67914, 20666], 19: [70024, 15350], 20: [106740, 14694], 21: [76583, 9196]}), 
    
    3: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1831, 1146], 5: [3588, 2243], 6: [5856, 3573], 7: [8710, 5366], 8: [10641, 6570], 9: [13909, 8427], 10: [16182, 9875], 11: [19494, 12010], 12: [53853, 25942], 13: [54691, 25264], 14: [61030, 26446], 15: [65313, 27024], 16: [65521, 26263], 17: [68448, 26676], 18: [67807, 20083], 19: [69612, 14518], 20: [107030, 14432], 21: [76137, 8886]}), 
    
    4: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1779, 1056], 5: [4956, 2948], 6: [5520, 3217], 7: [8714, 5109], 8: [11054, 6444], 9: [14023, 8183], 10: [16205, 9515], 11: [19935, 11586], 12: [53804, 24606], 13: [59863, 26399], 14: [55553, 23182], 15: [63986, 25374], 16: [65330, 25145], 17: [68295, 25185], 18: [67615, 19078], 19: [69664, 14410], 20: [106103, 13683], 21: [76331, 8709]}), 
    
    5: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1752, 976], 5: [4782, 2633], 6: [6719, 3683], 7: [8543, 4652], 8: [10663, 5935], 9: [14139, 7756], 10: [16795, 9338], 11: [19868, 11278], 12: [53848, 23500], 13: [60265, 24986], 14: [60821, 24398], 15: [58533, 22418], 16: [64825, 23744], 17: [67254, 24270], 18: [67059, 18573], 19: [69432, 13536], 20: [106005, 12578], 21: [76959, 8222]}), 
    
    6: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1788, 978], 5: [4846, 2727], 6: [6717, 3721], 7: [9773, 5355], 8: [10770, 6037], 9: [14164, 8099], 10: [16192, 9066], 11: [19974, 11470], 12: [54397, 23942], 13: [60133, 25625], 14: [60882, 24444], 15: [64066, 24614], 16: [58146, 22144], 17: [66729, 24408], 18: [67971, 17319], 19: [69470, 12652], 20: [106358, 11818], 21: [77176, 7613]}), 
    
    7: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1717, 1269], 5: [4862, 3626], 6: [6510, 4798], 7: [10056, 7438], 8: [12203, 8954], 9: [14104, 10385], 10: [16516, 12231], 11: [20395, 15159], 12: [53863, 30413], 13: [60185, 32876], 14: [61722, 32103], 15: [63669, 32046], 16: [63720, 30848], 17: [60503, 28330], 18: [66750, 14632], 19: [70064, 9354], 20: [106987, 9273], 21: [76573, 5560]}), 
    
    8: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1787, 1342], 5: [4816, 3706], 6: [6746, 5066], 7: [9809, 7427], 8: [12019, 9033], 9: [15227, 11560], 10: [16479, 12627], 11: [19892, 15223], 12: [54424, 31882], 13: [60242, 33698], 14: [60465, 32859], 15: [64211, 33557], 16: [64097, 32063], 17: [66762, 32206], 18: [60221, 23295], 19: [69105, 10907], 20: [105882, 8200], 21: [76784, 5369]}), 
    
    9: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [1829, 1420], 5: [4983, 3807], 6: [6651, 5072], 7: [9848, 7533], 8: [11944, 9160], 9: [15227, 11793], 10: [17621, 13650], 11: [20047, 15427], 12: [54236, 31855], 13: [59526, 34273], 14: [60876, 33181], 15: [63868, 33209], 16: [63961, 32206], 17: [66836, 32517], 18: [67195, 26565], 19: [62010, 20022], 20: [106500, 11194], 21: [77079, 4749]}), 
    
    10: defaultdict(None, {2: [0, 0], 3: [0, 0], 4: [7093, 5686], 5: [19293, 15263], 6: [26839, 21175], 7: [39935, 31640], 8: [48192, 38119], 9: [61354, 48519], 10: [70483, 55709], 11: [84492, 66671], 12: [215523, 131949], 13: [240358, 141738], 14: [244732, 136725], 15: [256412, 137361], 16: [257034, 132809], 17: [269578, 133107], 18: [266340, 108587], 19: [274013, 89079], 20: [395650, 95605], 21: [300300, 32201]})
})

#### Winning Rate
The winning rate is 0.4283583 which is about 42.83%.

______________________________________________________________________

## Summary

In summary, from our transcript, it seems like our player has a winning rate ranging from roughly 42.76% to 42.93%. The average blackjack player wins 42.2% of the time. This average can be a good point of reference even though our blackjack game is a simplified version of the real game. Taking the average as a reference, our independent player does a pretty good job (beats the average), and the learning strategy for our matrix seems to be satisfactory as it leads to quite a high winning rate for the game of blackjack where the odds are against the player. The monte carlo simulation supplemented by our strategy of always standing when the player's hand value is 21 seems to have a consistent success rate of 42.7% and above as the input sizes (number of simulations and the number of games played) grow. Assuming we run at least 100,000 simulations, using the learned matrix we can assume the odds of winning will range from roughly 42.7% to 42.9%. 
