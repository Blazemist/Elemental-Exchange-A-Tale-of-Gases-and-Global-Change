$ import character.rpy
label start:
    # scene bg beach
    # with fade
    # show havana war at right
    h "It’s “she sells seashells on the seashore”."
    # show river war at left
    r '''Nah it's not that. You are saying it wrong!
    “seas shell sea shells on the seashore” is how it goes.'''
    "and thus the great war between havana and river begins"
    # hide havana war 
    # hide river war
    # show river normal at left
    # show havana normal at right
    # show grandpa summon
    gp "What's going on there, my starlings?"
    "**explain explain**"
    # hide grandpa summon
    # hide havana normal
    # show grandpa chuckle
    # play music "audio/tired_chuckle.mp4 fadeout 1.0 volume 0.5
    gp "Both of you can be right."
    # stop music 
    # hide grandpa chuckle
    # show grandpa serious
    gp "These days the seas are indeed “shelling” our shores."
    # show river shocked at left
    r "What do you mean, gramps?"
    # hide granda serious
    # show grandpa normal
    gp '''Every year our Earth is getting warmer.
Do you remember the flash floods that struck our city in 2019 ?'''
    # play music "audio/girl_shreaks.mp4 fadeout 1.0 volume 0.5
    # hide river shocked
    # show river normal at left
    # show havana disgust at right
    h "Oh yes I could locate multiple snakes swimming in that filthy stagnant water."
    # stop music
    # hide havana disgust 
    # show havana normal at right
    gp '''Many coastal regions like our town are threatened by the ever-rising sea levels.
    This is triggered by the rising of temperatures, as I mentioned.'''
    # hide grandpa normal
    # show grandpa sweat_wipe
    gp '''*wipes swear*You must be familiar with greenhouse gasses, I presume?
They’re responsible for trapping heat.'''
    r  "This reminds me of our lectures from school, how about you,Havana?"
    # hide havana normal
    # show havana bliss right
    h "All I recollect is my craving for melting ice cream…"
    # hide river normal
    # show river disapointed at left
    r "*eye roll* It’s melting ice caps buddy, not ice creams!"
    # hide havana bliss
    # show havana nervous_chuckle at right
    h " It’s frustratingly hot outside, can’t blame me for hallucinating! "
    # hide grandpa sweat_wipe
    # show grandpa dying
    h "Oh no! Is Gramps possessed?"
    # hide havana nervous-chuckle
    # show havana pretending_possessed at right
    h'''As our local shaman would say,
“Has some evil eye looked upon us?”'''
    r '''Not funny Havana,
we have skin rashes too due to this unbearable, unpedictable heat.'''
    # [bubble shows up image of miliaria crystallina]
    gp " I need an extraction of aloe vera sap but… *pases out*"
#[separate bubble informs about Miliaria ]
    i "miliaria is a skin condition caused by blocked sweat ducts"
# show mil cry at left with fade
# show mil rub with fade
    i '''miliaria crystallina: mildest form, clear blisters, no inflammation
miliaria rubra: more severe, red bumps, itching, prickling sensation'''
# show mil pro at right with fade
    i '''miliaria profunda: rare,
flesh-colored bumps,
deeper skin layers affected'''
    i '''The most serious complications include impaired
thermoregulation and secondary bacterial infection.
high temperatures cause this disorder'''
#(pictures of the 3 medical types can be shown by ai too)
    "(Havana and River holler drag Gramps to their hut,and grandma comes up)"
    gm '''I told your gramps to be in the shade but will he listen?
Never!'''
    gm "Quick, kids we need to collect Aloe Vera leaves."
    gm '''I'll go fetch the community doctor.'''
#Havana and River attempted to find these herbs in the forest but they were all attacked by spider mites.
    r "Now what do we do"
    h " Let's keep looking"
    r  "Oh I hear something"
#[sfx of water gushing from     r overflow]
    h " You must be hallucinating"
    r  "oh no River-"
    h  "Why are you calling your name-*turns around*"
    "Havana & River" "GYAAAAAAN AAAAAAA....*GLUP GLUP GLUP*"
#(River and Havana scream is heard as they all start to drown due to flooding of the river)
#(bubble sfx)
    jump SCENE_2

label SCENE_2 : 
#River and Havana meeting the anthropomorphised villains a.k.a GHG [scene atmosphere]
    # show co2 at left
    "1"
    # show ch4 at right
    "2"
    # show no2
    "3"
    # hide co2
    # show sf6 at left
    "4"
    # hide ch4 
    # show pfc at right
    "5"
    # hide no2
    # show hfc
    "6"
    # hide sf6
    # show nf3 at left
    ""
    '''all of them are in a deep squabble of who has got a more
impressive streak of annihilating the human realm.)'''
    CO2 '''As far as the statistics have it,
I believe it’s obvious
that my competency surpasses that of any other gas’'''
    CH4 '''Hey but you get dissolved in water bodies.
Besides my presence is much more enduring than yours,
my families stay for about 12 years in the atmosphere'''
    NO2 '''You think that’s impressive?'''
    NO2 '''My kind usually lasts for about a century and
we’ve got more GWPthan all those present here.'''
#[bubble shows up GWP definition]

    CO2 "*looks at FC*"
    CO2 "What makes you giggle?\nAre you not awe-inspired by our abilities? "
    SF6 '''Our percentage presence may be negligible comparatively,
but we don’t need to convince you of our might when our GWP is 20k times higher. '''
    h "Is this heaven or hell?"
    r "Where are we indeed?"
 
#(River and Havana are in the atmosphere of a layer where greenhouse gasses gather .
#They see themselves as molecules)
    CO2 "Oh what are these human fledgelings doing here?"
    NO2 '''This is no human territory and
we are the ones to determine the atmospheric fate.'''
    NO2 '''Quite funny,
if you think about how humans are so self-destructive as to continually summon us. '''
    h "Can you help us stop seas from devouring our islands?"
#   play music audio/evil_laugh.mp3  volume 0.5
    CO2 " You’re asking the wrong folks, kiddos."
#   stop music
    CO2 '''From your perspective,
we very much are the ‘villains’ 
that your people made us out to be because of the mismanagement of resources.'''
#   show havana confused at right
#   show river confused at left


    H2O "I may or may not have brought them here…."
    CH4 "On whose command!"
    H2O "*eye roll*\nI thought you asked me for entertainment"
    h '''Who are you all?
I only recognise carbon dioxide, methane and nitrous dioxide.'''
# turns to fc harem
    CO2 "Told ya we oldies are goldies."
    HFC '''*eye roll* 
Just because some humans are ignorant our value doesn't diminish''' 

    i '''majority of the GHGs think Havanah and River aren't aware of them.
    Can you Help them to understand better?'''
menu:
    "No" : 
        jump main_story
    "Yes ": 
        pass


label SCENE_2_PART_2:
#   scene co2 form
    i '''Carbon dioxide enters the atmosphere through burning fossil fuels 
(coal, natural gas, and oil), solid waste, trees and other biological materials
and also as a result of certain chemical reactions like cement production.'''
#   with fade
#   scene co2 elemination 
    i '''Carbon dioxide is removed from the atmosphere
when it is absorbed by plants as part of the biological carbon cycle.'''
#   with fade
#   scene ch4 form
    i '''methane is formed at the production and transport of coal,natural gas, and oil.'''
    i '''Methane emissions also result from livestock and other agricultural practices,
land use, and by the decay of organic waste in municipal solid waste landfills.'''
#   with fade
#   scene ch4 elemination
    i '''natural processes in soil and 
chemical reactions in the atmosphere help remove CH4 from the atmosphere.'''
#   with fade
#   scene no2 form
    i '''NO2 is emitted during agricultural, land use, and industrial activities,
combustion of fossil fuels and solid waste,
as well as during treatment of wastewater.'''
#   with fade
#   scene no2 elemination
    i '''NO2 Emissions can be reduced by reducing N-based fertilizer applications 
    and applying these fertilizers more efficiently,
    or reducing fuel consumption in motor vehicle.'''
    i '''it can also be reduced through technological upgrades 
    and use of abatement equipment
    '''
#   with fade
#   scene fc form
    i '''They are emitted through their use as substitutes 
for ozone-depleting substances like as refrigerants
and through a variety of industrial processes such as aluminum 
and semiconductor manufacturing.'''
#   with fade
#   scene fc elemination
    i '''Industrial fluorinated gases can reduce emissions by 
adopting fluorinated gas capture and destruction processors'''
    i '''HFCs can be reduced through better system components 
and through the use of alternative refrigerants with
lower global warming potentials than those presently used.'''
#   with fade
    h '''There are natural processes to remove you CO2,
    methane and NO2 from atmosphere while there aren’t for FC'''
    r '''That’s about as much difference as there exists between 
you oldies and new gen GHG.
sheesh you all made it seem as if you don’t share a combined purpose'''
    NO2 "It appears that we underestimated your understanding of the matter at hand"
    CO2 '''*shakes head* You kiddos might not be ignorant 
but we’re responsible for transforming your home into a boiling stew
thanks to mankind’s misplaced ideas of advancement.'''
    r "Misplaced ideas of advancement ?"
    NO2 '''Humans are convinced of their superiority.
As your kind relentlessly pursued socioeconomic and industrial prosperity,
you hastened the degradation of the very environment that sustains you.'''
    SF6 "I’ve come across humans who claim that reports of our GWP are means to achieve fearmongering among the masses."
    SF6 '''It is almost funny how gullibly they continue to shrug off the effects of global warming that they experience first-hand.
    Talk about self-sabotage!'''
    SF6 "You could compare it to letting off a criminal in plain sight."
    CO2 '''Our results are practically rising at a rate greater
than that of any preventive measures 
adopted by humans to curtail our maleffects.'''

# show data_line_graph ghg_usa
#   show river shocked at left
    "..."
#   show havana shocked at left
    "..."
# hide data_line_graph ghg_usa
#   show ch4 smug
    CH4 '''Oho- It seems you are ignorant of the real time rising trends
we are setting because of the rising human population density.'''

    '''majority of the GHGs think Havanah and River 
aren't aware of real time consequences of human activities.
Can you Help them to understand better?
Accept the second challenge of GHG or not ?'''
menu:
    "No" : 
        jump main_story
    "Yes ": 
        pass


label q_1:
    #scene data_line_graph ghg_usa
    #with fade
    i '''As the years go from 2005 to 2020
    what trend can be observed in the population density ?'''
    menu:
        "A)  slightly increasing trend":
            "Gas army" "Well done kiddo"
        "B)  decreasing trend":
            "Gas army" '''Over time, we don’t see yellow hue increasing 
    and thus it is not a decreasing trend in population density'''
            jump q_1
        "C)  negligible change":
            "Gas army" "It was quite an ambiguous one to detect, not a bad attempt"
    i '''From the year 2015 to 2020 
    did the trend in CO2 emissions increase or decrease in general overall in India?'''
    menu:
        "Increase ":
            "Gas Army" 'well done'
            jump main_story
        "Decrease":
            pass
        "No difference ":
            pass
    i'''From bluer overall tint it changed to green,
and this according to the key means a rise in CO2 emissions.'''



label main_story:
    r '''There’s got to be something we could do
now that we know about population densities and
greenhouse gas emmissions correlation!'''
    h "Everyone I’ve ever looked up to would probably be disappointed to see us back down."
    #play music audio/evil_laugh.mp3  volume 0.5
    CO2 '''Humans have been ‘trying to do something’
    and has that ever been enough to stop us ?'''
    # stop music
    h "Our ozone layer has not yet irreparably been depleted!"
    r "Yeah and—"
    #jump scene_3
