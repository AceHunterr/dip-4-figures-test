import math
x = [141.40503466129303, 144.28503692150116,
     140.56786358356476, 137.7961403131485]
y = [78.26734668016434, 78.73586314916611,
     82.55131781101227, 82.32149112224579]
mean_x = (x[0]+x[2])/2
mean_y = (y[0]+y[2])/2
print(mean_x, mean_y)
radius = math.sqrt(math.pow(mean_x-x[1], 2)+math.pow(mean_y-y[1], 2))
print(radius)

# point_x = mean_x+radius*math.cos(0.017453)
# point_y = mean_y+radius*math.sin(0.017453)

# print(point_x, point_y)
X = []
Y = []
i = 0
while(i <= 360):
    j = math.radians(i)
    point_x = mean_x+radius*math.cos(j)
    point_y = mean_y+radius*math.sin(j)
    X.append(point_x)
    Y.append(point_y)
    i += 1
# print(X)
# print(Y)
L = len(X)
L1 = len(Y)
print(L, L1)
i = 0
while(i < L):
    print('{ x:', X[i], ', y:', Y[i], '},')
    i = i+1
{x: 144.68525707700948, y: 80.4093322455883},
{x: 144.6846937306424, y: 80.4738853453451},
{x: 144.68300386314198, y: 80.53841878160237},
{x: 144.6801879892582, y: 80.60291289685028},
{x: 144.67624696673354, y: 80.66734804555657},
{x: 144.67118199604164, y: 80.73170460015072},
{x: 144.66499462002162, y: 80.79596295700279},
{x: 144.65768672340815, y: 80.86010354239477},
{x: 144.64926053225736, y: 80.92410681848304},
{x: 144.63971861326868, y: 80.98795328924966},
{x: 144.62906387300308, y: 81.05162350644116},
{x: 144.61729955699764, y: 81.1150980754926},
{x: 144.604429248777, y: 81.17835766143533},
{x: 144.59045686876172, y: 81.24138299478668},
{x: 144.5753866730741, y: 81.30415487741956},
{x: 144.5592232522417, y: 81.36665418841045},
{x: 144.54197152979916, y: 81.42886188986378},
{x: 144.5236367607882, y: 81.49075903271104},
{x: 144.5042245301571, y: 81.55232676248293},
{x: 144.48374075105934, y: 81.61354632505255},
{x: 144.46219166305247, y: 81.67439907234808},
{x: 144.43958383019748, y: 81.73486646803319},
{x: 144.4159241390592, y: 81.79493009315341},
{x: 144.3912197966088, y: 81.85457165174667},
{x: 144.3654783280283, y: 81.91377297641647},
{x: 144.33870757441838, y: 81.97251603386582},
{x: 144.3109156904099, y: 82.03078293039034},
{x: 144.28211114168002, y: 82.08855591732895},
{x: 144.25230270237327, y: 82.14581739647014},
{x: 144.22149945242901, y: 82.20254992541264},
{x: 144.18971077481564, y: 82.2587362228786},
{x: 144.15694635267224, y: 82.31435917397748},
{x: 144.12321616635919, y: 82.36940183541957},
{x: 144.08853049041804, y: 82.42384744067698},
{x: 144.05289989044167, y: 82.47767940509091},
{x: 144.01633521985596, y: 82.53088133092353},
{x: 143.97884761661382, y: 82.58343701235285},
{x: 143.94044849980233, y: 82.63533044040919},
{x: 143.90114956616446, y: 82.68654580785166},
{x: 143.8609627865361, y: 82.73706751398319},
{x: 143.8199004021996, y: 82.7868801694027},
{x: 143.77797492115505, y: 82.8359686006928},
{x: 143.73519911431006, y: 82.88431785504177},
{x: 143.69158601158983, y: 82.93191320479838},
{x: 143.6471488979679, y: 82.97874015195802},
{x: 143.60190130941956, y: 83.02478443257897},
{x: 143.5558570287986, y: 83.0700320211273},
{x: 143.50903008163897, y: 83.11446913474924},
{x: 143.46143473188235, y: 83.15808223746949},
{x: 143.4130854775334, y: 83.20085804431446},
{x: 143.3639970462433, y: 83.24278352535903},
{x: 143.31418439082378, y: 83.28384590969551},
{x: 143.26366268469226, y: 83.32403268932387},
{x: 143.21244731724977, y: 83.36333162296174},
{x: 143.16055388919344, y: 83.40173073977323},
{x: 143.10799820776413, y: 83.43921834301537},
{x: 143.0547962819315, y: 83.47578301360106},
{x: 143.00096431751757, y: 83.51141361357745},
{x: 142.94651871226014, y: 83.54609928951861},
{x: 142.89147605081806, y: 83.57982947583163},
{x: 142.83585309971917, y: 83.61259389797503},
{x: 142.77966680225325, y: 83.64438257558844},
{x: 142.72293427331073, y: 83.67518582553267},
{x: 142.66567279416955, y: 83.70499426483943},
{x: 142.60789980723095, y: 83.73379881356932},
{x: 142.5496329107064, y: 83.76159069757779},
{x: 142.49088985325707, y: 83.78836145118771},
{x: 142.43168852858727, y: 83.81410291976822},
{x: 142.372046969994, y: 83.83880726221861},
{x: 142.3119833448738, y: 83.86246695335687},
{x: 142.25151594918867, y: 83.88507478621189},
{x: 142.19066320189313, y: 83.90662387421875},
{x: 142.12944363932354, y: 83.92710765331651},
{x: 142.06787590955165, y: 83.94651988394762},
{x: 142.00597876670437, y: 83.96485465295856},
{x: 141.94377106525104, y: 83.98210637540112},
{x: 141.88127175426015, y: 83.9982697962335},
{x: 141.81849987162727, y: 84.01333999192111},
{x: 141.75547453827593, y: 84.0273123719364},
{x: 141.6922149523332, y: 84.04018268015705},
{x: 141.62874038328175, y: 84.05194699616248},
{x: 141.56507016609027, y: 84.06260173642809},
{x: 141.50122369532363, y: 84.07214365541677},
{x: 141.43722041923536, y: 84.08056984656756},
{x: 141.37307983384338, y: 84.08787774318102},
{x: 141.3088214769913, y: 84.09406511920105},
{x: 141.24446492239716, y: 84.09913008989295},
{x: 141.18002977369088, y: 84.10307111241762},
{x: 141.11553565844295, y: 84.10588698630139},
{x: 141.0510022221857, y: 84.10757685380182},
{x: 140.9864491224289, y: 84.10814020016888},
{x: 140.9218960226721, y: 84.10757685380182},
{x: 140.85736258641484, y: 84.10588698630139},
{x: 140.7928684711669, y: 84.10307111241762},
{x: 140.72843332246063, y: 84.09913008989295},
{x: 140.66407676786648, y: 84.09406511920105},
{x: 140.5998184110144, y: 84.08787774318102},
{x: 140.53567782562243, y: 84.08056984656756},
{x: 140.47167454953416, y: 84.07214365541677},
{x: 140.40782807876752, y: 84.06260173642809},
{x: 140.34415786157604, y: 84.05194699616248},
{x: 140.2806832925246, y: 84.04018268015705},
{x: 140.21742370658188, y: 84.0273123719364},
{x: 140.15439837323052, y: 84.01333999192111},
{x: 140.09162649059763, y: 83.9982697962335},
{x: 140.02912717960675, y: 83.98210637540112},
{x: 139.96691947815341, y: 83.96485465295856},
{x: 139.90502233530614, y: 83.94651988394762},
{x: 139.84345460553425, y: 83.92710765331651},
{x: 139.78223504296466, y: 83.90662387421875},
{x: 139.72138229566912, y: 83.88507478621189},
{x: 139.66091489998402, y: 83.86246695335687},
{x: 139.6008512748638, y: 83.83880726221861},
{x: 139.54120971627052, y: 83.81410291976822},
{x: 139.48200839160071, y: 83.78836145118771},
{x: 139.42326533415138, y: 83.76159069757779},
{x: 139.36499843762684, y: 83.73379881356932},
{x: 139.30722545068824, y: 83.70499426483943},
{x: 139.24996397154706, y: 83.67518582553267},
{x: 139.19323144260454, y: 83.64438257558844},
{x: 139.13704514513861, y: 83.61259389797503},
{x: 139.08142219403973, y: 83.57982947583163},
{x: 139.02637953259764, y: 83.54609928951861},
{x: 138.97193392734022, y: 83.51141361357745},
{x: 138.9181019629263, y: 83.47578301360106},
{x: 138.86490003709366, y: 83.43921834301537},
{x: 138.81234435566435, y: 83.40173073977323},
{x: 138.76045092760802, y: 83.36333162296174},
{x: 138.70923556016552, y: 83.32403268932387},
{x: 138.658713854034, y: 83.28384590969551},
{x: 138.6089011986145, y: 83.24278352535903},
{x: 138.5598127673244, y: 83.20085804431446},
{x: 138.51146351297544, y: 83.15808223746949},
{x: 138.46386816321882, y: 83.11446913474924},
{x: 138.41704121605918, y: 83.0700320211273},
{x: 138.37099693543823, y: 83.02478443257897},
{x: 138.3257493468899, y: 82.97874015195802},
{x: 138.28131223326795, y: 82.93191320479838},
{x: 138.23769913054772, y: 82.88431785504177},
{x: 138.19492332370274, y: 82.8359686006928},
{x: 138.15299784265818, y: 82.7868801694027},
{x: 138.11193545832168, y: 82.73706751398319},
{x: 138.07174867869333, y: 82.68654580785166},
{x: 138.03244974505546, y: 82.63533044040919},
{x: 137.99405062824397, y: 82.58343701235285},
{x: 137.95656302500183, y: 82.53088133092353},
{x: 137.91999835441612, y: 82.47767940509091},
{x: 137.88436775443975, y: 82.42384744067698},
{x: 137.8496820784986, y: 82.36940183541957},
{x: 137.81595189218555, y: 82.31435917397748},
{x: 137.78318747004215, y: 82.2587362228786},
{x: 137.75139879242877, y: 82.20254992541264},
{x: 137.72059554248452, y: 82.14581739647012},
{x: 137.69078710317777, y: 82.08855591732895},
{x: 137.6619825544479, y: 82.03078293039034},
{x: 137.6341906704394, y: 81.97251603386582},
{x: 137.60741991682949, y: 81.91377297641647},
{x: 137.581678448249, y: 81.85457165174667},
{x: 137.5569741057986, y: 81.79493009315341},
{x: 137.5333144146603, y: 81.73486646803319},
{x: 137.51070658180532, y: 81.67439907234808},
{x: 137.48915749379844, y: 81.61354632505255},
{x: 137.46867371470069, y: 81.55232676248293},
{x: 137.44926148406958, y: 81.49075903271104},
{x: 137.43092671505863, y: 81.42886188986378},
{x: 137.41367499261608, y: 81.36665418841045},
{x: 137.3975115717837, y: 81.30415487741956},
{x: 137.38244137609607, y: 81.24138299478668},
{x: 137.3684689960808, y: 81.17835766143533},
{x: 137.35559868786015, y: 81.1150980754926},
{x: 137.3438343718547, y: 81.05162350644116},
{x: 137.3331796315891, y: 80.98795328924966},
{x: 137.32363771260043, y: 80.92410681848304},
{x: 137.31521152144964, y: 80.86010354239477},
{x: 137.30790362483617, y: 80.79596295700279},
{x: 137.30171624881615, y: 80.73170460015072},
{x: 137.29665127812424, y: 80.66734804555657},
{x: 137.2927102555996, y: 80.60291289685028},
{x: 137.2898943817158, y: 80.53841878160237},
{x: 137.28820451421538, y: 80.4738853453451},
{x: 137.2876411678483, y: 80.4093322455883},
{x: 137.28820451421538, y: 80.34477914583151},
{x: 137.2898943817158, y: 80.28024570957423},
{x: 137.2927102555996, y: 80.21575159432632},
{x: 137.29665127812424, y: 80.15131644562004},
{x: 137.30171624881615, y: 80.08695989102588},
{x: 137.30790362483617, y: 80.02270153417382},
{x: 137.31521152144964, y: 79.95856094878184},
{x: 137.32363771260043, y: 79.89455767269357},
{x: 137.3331796315891, y: 79.83071120192695},
{x: 137.3438343718547, y: 79.76704098473544},
{x: 137.35559868786015, y: 79.70356641568401},
{x: 137.3684689960808, y: 79.64030682974128},
{x: 137.38244137609607, y: 79.57728149638993},
{x: 137.3975115717837, y: 79.51450961375704},
{x: 137.41367499261608, y: 79.45201030276615},
{x: 137.43092671505863, y: 79.38980260131284},
{x: 137.44926148406958, y: 79.32790545846557},
{x: 137.46867371470069, y: 79.26633772869367},
{x: 137.48915749379844, y: 79.20511816612405},
{x: 137.51070658180532, y: 79.14426541882852},
{x: 137.5333144146603, y: 79.08379802314342},
{x: 137.5569741057986, y: 79.0237343980232},
{x: 137.581678448249, y: 78.96409283942994},
{x: 137.60741991682949, y: 78.90489151476014},
{x: 137.6341906704394, y: 78.84614845731079},
{x: 137.6619825544479, y: 78.78788156078626},
{x: 137.69078710317777, y: 78.73010857384766},
{x: 137.72059554248452, y: 78.67284709470647},
{x: 137.75139879242877, y: 78.61611456576397},
{x: 137.78318747004215, y: 78.55992826829801},
{x: 137.81595189218555, y: 78.50430531719913},
{x: 137.8496820784986, y: 78.44926265575704},
{x: 137.88436775443975, y: 78.39481705049963},
{x: 137.91999835441612, y: 78.3409850860857},
{x: 137.95656302500183, y: 78.28778316025307},
{x: 137.99405062824397, y: 78.23522747882376},
{x: 138.03244974505546, y: 78.18333405076741},
{x: 138.07174867869333, y: 78.13211868332495},
{x: 138.11193545832168, y: 78.0815969771934},
{x: 138.15299784265818, y: 78.0317843217739},
{x: 138.19492332370274, y: 77.98269589048381},
{x: 138.23769913054772, y: 77.93434663613483},
{x: 138.28131223326795, y: 77.88675128637823},
{x: 138.3257493468899, y: 77.83992433921858},
{x: 138.37099693543823, y: 77.79388005859764},
{x: 138.41704121605918, y: 77.7486324700493},
{x: 138.46386816321882, y: 77.70419535642736},
{x: 138.51146351297544, y: 77.66058225370712},
{x: 138.5598127673244, y: 77.61780644686215},
{x: 138.6089011986145, y: 77.57588096581757},
{x: 138.658713854034, y: 77.53481858148109},
{x: 138.70923556016552, y: 77.49463180185272},
{x: 138.76045092760802, y: 77.45533286821487},
{x: 138.81234435566435, y: 77.41693375140338},
{x: 138.86490003709366, y: 77.37944614816124},
{x: 138.9181019629263, y: 77.34288147757555},
{x: 138.97193392734022, y: 77.30725087759916},
{x: 139.02637953259762, y: 77.272565201658},
{x: 139.08142219403973, y: 77.23883501534497},
{x: 139.13704514513861, y: 77.20607059320157},
{x: 139.19323144260454, y: 77.17428191558817},
{x: 139.24996397154706, y: 77.14347866564394},
{x: 139.30722545068824, y: 77.11367022633718},
{x: 139.36499843762684, y: 77.08486567760728},
{x: 139.42326533415138, y: 77.05707379359882},
{x: 139.48200839160071, y: 77.0303030399889},
{x: 139.54120971627052, y: 77.00456157140839},
{x: 139.6008512748638, y: 76.979857228958},
{x: 139.660914899984, y: 76.95619753781973},
{x: 139.72138229566912, y: 76.93358970496472},
{x: 139.78223504296466, y: 76.91204061695785},
{x: 139.84345460553425, y: 76.8915568378601},
{x: 139.90502233530614, y: 76.87214460722899},
{x: 139.96691947815341, y: 76.85380983821804},
{x: 140.02912717960675, y: 76.83655811577549},
{x: 140.09162649059763, y: 76.8203946949431},
{x: 140.15439837323052, y: 76.80532449925549},
{x: 140.21742370658185, y: 76.7913521192402},
{x: 140.2806832925246, y: 76.77848181101956},
{x: 140.34415786157604, y: 76.76671749501412},
{x: 140.40782807876752, y: 76.75606275474853},
{x: 140.47167454953416, y: 76.74652083575984},
{x: 140.53567782562243, y: 76.73809464460905},
{x: 140.5998184110144, y: 76.73078674799558},
{x: 140.66407676786648, y: 76.72459937197556},
{x: 140.72843332246063, y: 76.71953440128365},
{x: 140.7928684711669, y: 76.71559337875898},
{x: 140.85736258641484, y: 76.71277750487522},
{x: 140.9218960226721, y: 76.71108763737479},
{x: 140.9864491224289, y: 76.71052429100773},
{x: 141.0510022221857, y: 76.71108763737479},
{x: 141.11553565844295, y: 76.71277750487522},
{x: 141.18002977369088, y: 76.71559337875898},
{x: 141.24446492239716, y: 76.71953440128365},
{x: 141.3088214769913, y: 76.72459937197556},
{x: 141.37307983384338, y: 76.73078674799558},
{x: 141.43722041923536, y: 76.73809464460905},
{x: 141.50122369532363, y: 76.74652083575984},
{x: 141.56507016609027, y: 76.75606275474851},
{x: 141.62874038328175, y: 76.76671749501412},
{x: 141.6922149523332, y: 76.77848181101956},
{x: 141.75547453827593, y: 76.7913521192402},
{x: 141.81849987162727, y: 76.80532449925549},
{x: 141.88127175426015, y: 76.8203946949431},
{x: 141.94377106525104, y: 76.83655811577549},
{x: 142.00597876670437, y: 76.85380983821804},
{x: 142.06787590955165, y: 76.87214460722899},
{x: 142.12944363932354, y: 76.8915568378601},
{x: 142.19066320189313, y: 76.91204061695785},
{x: 142.25151594918867, y: 76.93358970496472},
{x: 142.3119833448738, y: 76.95619753781973},
{x: 142.372046969994, y: 76.979857228958},
{x: 142.43168852858727, y: 77.00456157140839},
{x: 142.49088985325707, y: 77.0303030399889},
{x: 142.5496329107064, y: 77.05707379359883},
{x: 142.60789980723095, y: 77.08486567760728},
{x: 142.66567279416955, y: 77.11367022633718},
{x: 142.72293427331073, y: 77.14347866564393},
{x: 142.77966680225325, y: 77.17428191558817},
{x: 142.83585309971917, y: 77.20607059320157},
{x: 142.89147605081806, y: 77.23883501534497},
{x: 142.94651871226014, y: 77.272565201658},
{x: 143.00096431751757, y: 77.30725087759916},
{x: 143.0547962819315, y: 77.34288147757555},
{x: 143.10799820776413, y: 77.37944614816124},
{x: 143.16055388919344, y: 77.41693375140338},
{x: 143.21244731724977, y: 77.45533286821487},
{x: 143.26366268469226, y: 77.49463180185273},
{x: 143.31418439082378, y: 77.53481858148109},
{x: 143.3639970462433, y: 77.57588096581757},
{x: 143.4130854775334, y: 77.61780644686215},
{x: 143.46143473188235, y: 77.66058225370712},
{x: 143.50903008163897, y: 77.70419535642736},
{x: 143.5558570287986, y: 77.7486324700493},
{x: 143.60190130941956, y: 77.79388005859764},
{x: 143.6471488979679, y: 77.83992433921858},
{x: 143.69158601158983, y: 77.88675128637823},
{x: 143.73519911431006, y: 77.93434663613483},
{x: 143.77797492115505, y: 77.98269589048381},
{x: 143.8199004021996, y: 78.0317843217739},
{x: 143.8609627865361, y: 78.0815969771934},
{x: 143.90114956616446, y: 78.13211868332495},
{x: 143.94044849980233, y: 78.18333405076741},
{x: 143.97884761661382, y: 78.23522747882376},
{x: 144.01633521985596, y: 78.28778316025307},
{x: 144.05289989044167, y: 78.3409850860857},
{x: 144.08853049041804, y: 78.39481705049964},
{x: 144.12321616635919, y: 78.44926265575704},
{x: 144.15694635267224, y: 78.50430531719913},
{x: 144.18971077481564, y: 78.55992826829801},
{x: 144.22149945242901, y: 78.61611456576397},
{x: 144.25230270237327, y: 78.67284709470647},
{x: 144.28211114168002, y: 78.73010857384766},
{x: 144.3109156904099, y: 78.78788156078625},
{x: 144.33870757441838, y: 78.84614845731079},
{x: 144.3654783280283, y: 78.90489151476014},
{x: 144.3912197966088, y: 78.96409283942994},
{x: 144.4159241390592, y: 79.0237343980232},
{x: 144.43958383019748, y: 79.08379802314342},
{x: 144.46219166305247, y: 79.14426541882852},
{x: 144.48374075105934, y: 79.20511816612405},
{x: 144.5042245301571, y: 79.26633772869367},
{x: 144.5236367607882, y: 79.32790545846557},
{x: 144.54197152979916, y: 79.38980260131284},
{x: 144.5592232522417, y: 79.45201030276615},
{x: 144.5753866730741, y: 79.51450961375704},
{x: 144.59045686876172, y: 79.57728149638993},
{x: 144.604429248777, y: 79.64030682974128},
{x: 144.61729955699764, y: 79.70356641568401},
{x: 144.62906387300308, y: 79.76704098473544},
{x: 144.63971861326868, y: 79.83071120192695},
{x: 144.64926053225736, y: 79.89455767269357},
{x: 144.65768672340815, y: 79.95856094878184},
{x: 144.66499462002162, y: 80.02270153417382},
{x: 144.67118199604164, y: 80.08695989102588},
{x: 144.67624696673354, y: 80.15131644562004},
{x: 144.6801879892582, y: 80.21575159432632},
{x: 144.68300386314198, y: 80.28024570957423},
{x: 144.6846937306424, y: 80.34477914583151},
{x: 144.68525707700948, y: 80.4093322455883},
