$ import character.rpy
label start:
    scene bg beach
    with fade
    # show havana war at right
    h "It’s “She sells seashells on the seashore”."
    # show river war at left
    r '''Nah it's not that. You are saying it wrong!
    “Seas shell sea shells on the seashore” is how it goes.'''
    "And thus the great war between havana and river begins."
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
    play sound "audio/Chuckling Man.mp3"
    gp "Both of you can be right."
    stop sound 
    # hide grandpa chuckle
    # show grandpa serious
    gp "These days the seas are indeed “shelling” our shores."
    # show river shocked at left
    r "What do you mean, gramps?"
    # hide granda serious
    # show grandpa normal
    gp '''Every year our Earth is getting warmer.
Do you remember the flash floods that struck our city in 2019?'''
    play sound "audio/eek.mp3" volume 0.75
    # hide river shocked
    # show river normal at left
    # show havana disgust at right
    h "Oh yes I could locate multiple snakes swimming in that filthy stagnant water."
    stop sound
    # hide havana disgust 
    # show havana normal at right
    gp '''Many coastal regions like our town are threatened by the ever-rising sea levels.
    This is triggered by the rising of temperatures, as I mentioned.'''
    # hide grandpa normal
    # show grandpa sweat_wipe
    gp '''*wipes sweat* You must be familiar with greenhouse gasses, I presume?
They’re responsible for trapping heat.'''
    r  "This reminds me of our lectures from school, how about you, Havana?"
    # hide havana normal
    # show havana bliss right
    h "All I recollect is my craving for melting ice cream…"
    # hide river normal
    # show river disapointed at left
    r "*eye roll* It’s melting ice caps buddy, not ice creams!"
    # hide havana bliss
    # show havana nervous_chuckle at right
    h "It’s frustratingly hot outside, can’t blame me for hallucinating!"
    # hide grandpa sweat_wipe
    # show grandpa dying
    h "Oh no! Is Gramps possessed?"
    # hide havana nervous_chuckle
    # show havana pretending_possessed at right
    h '''As our local shaman would say,
“Has some evil eye looked upon us?”'''
    r '''Not funny Havana,
we have skin rashes too due to this unbearable, unpedictable heat.'''
    # [bubble shows up image of miliaria crystallina]
    play sound "audio/dying-and-asking-for-help.mp3"
    gp "I need an extraction of aloe vera sap but… *pases out*"
    # hide grandpa dying
    # hide havana pretending_possessed
    # hide river disapointed
    # show mil default at left
    # show info kun at right
    stop sound
    i "Miliaria is a skin condition caused by blocked sweat ducts"
    # hide mil default
    # show mil cry at left with fade
    i '''Miliaria crystallina: mildest form, clear blisters, no inflammation'''
    # hide mil cry
    # show mil rub at left with fade
    i '''Miliaria rubra: more severe, red bumps, itching, prickling sensation'''
    # hide mil rub
    # show mil pro at left with fade
    i '''Miliaria profunda: rare,flesh-colored bumps,
deeper skin layers affected'''
    # hide mil pro
    i '''The most serious complications include impaired
thermoregulation and secondary bacterial infection.
High temperatures cause this disorder'''
    "(Havana and River holler drag Gramps to their hut,and grandma comes up)"
    scene bg hut_inside
    with fade
    # hide info kun
    # show grandpa faint
    # show havana worried at left
    # show grandma disapointed at right
    gm '''I told your gramps to be in the shade but will he listen?
Never!'''
    gm "Quick, kids we need to collect Aloe Vera leaves."
    # hide grandma disapointed
    # show grandma tsundere at right
    gm '''I'll go fetch the community doctor.'''
    # hide grandma tsundere
    # hide havana worried
    # hide grandpa faint
    scene bg forest
    with fade
#Havana and River attempted to find these herbs in the forest but they were all attacked by spider mites.
    # show river normal at left
    # show havana normal at right
    # show destoryed alo_vera
    r "Now what do we do?"
    h "Let's keep looking."
    # hide destoryed alo_vera
    # show havana normal
    # hide river normal
    # show river shocked at left
    r  "Oh I hear something."
    play sound "audio/bubbles.mp3" volume 0.05
    h "You must be hallucinating."
    # show wave at right
    r  "Oh no River-"
    h  "Why are you calling your name- *turns around*"
    stop sound

    scene bg ocean
    with fade
    play sound "audio/Waves.mp3"
    "Havana & River" "GYAAAAAAN AAAAAAA....*GLUP GLUP GLUP*"
    # hide havana normal
    # hide river shocked
    stop sound
    
    jump SCENE_2

label SCENE_2 : 
#River and Havana meeting the anthropomorphised villains a.k.a GHG [scene atmosphere]
    scene bg atmosphere
    with fade
    # show co2 at left
    
    "C.A.R.B.O.N.  D.I.O.X.I.D.E"
    # show ch4 at right
    "M.E.T.H.A.N.E"
    # show no2
    "N.I.T.R.O.U.S O.X.I.D.E"
    # hide co2
    # show sf6 at left
    "S.U.L.F.E.R H.E.X.A.F.L.U.O.R.I.D.E"
    # hide ch4 
    # show pfc at right
    "P.E.R.F.L.U.R.O.C.H.E.M.I.C.A.L.S"
    # hide no2
    # show hfc
    "H.Y.D.R.O.F.L.U.R.O.C.A.R.B.O.N"
    # hide sf6
    # show nf3 at left
    "N.I.T.R.O.G.E.N  T.R.I.F.L.U.R.I.D.E"
    # hide pfc
    # hide hfc
    # hide nf3
    # show co2 
    # show ch4 at left
    # show no2 at right
    '''All of them are in a deep squabble of who has got a more
impressive streak of annihilating the human realm.)'''
    CO2 '''As far as the statistics have it,
I believe it’s obvious
that my competency surpasses that of any other gas.'''
    CH4 '''Hey but you get dissolved in water bodies.
Besides my presence is much more enduring than yours,
my families stay for about 12 years in the atmosphere.'''
    NO2 '''You think that’s impressive?'''
    NO2 '''My kind usually lasts for about a century and
we’ve got more GWP than all those present here.'''
    #[bubble shows up GWP definition]

    CO2 "*looks at FC*"
    CO2 "What makes you giggle? Are you not awe-inspired by our abilities?"
    # hide ch4
    # show sf6
    SF6 '''Our percentage presence may be negligible comparatively,
but we don’t need to convince you of our might when our GWP is 20k times higher.'''
    # hide sf6
    # hide no2
    # show havana confused at left
    # show river confused at right
    h "Is this heaven or hell?"
    r "Where are we indeed?"
    #(River and Havana are in the atmosphere of a layer where greenhouse gasses gather .
    #They see themselves as molecules)
    CO2 "Oh what are these human fledgelings doing here?"
    # hide river confused
    # show no2 at right
    NO2 '''This is no human territory and
we are the ones to determine the atmospheric fate.'''
    NO2 '''Quite funny,
if you think about how humans are so self-destructive as to continually summon us.'''
    h "Can you help us stop seas from devouring our islands?"
    play sound "audio/villian-theme.wav"  volume 0.5
    CO2 "You’re asking the wrong folks, kiddos."
    stop sound
    CO2 '''From your perspective,
we very much are the ‘villains’ 
that your people made us out to be because of the mismanagement of resources.'''
    # hide co2 
    # hide no2
    # show havana confused at right
    # show river confused at left
    # show h2o wifu
    H2O "I may or may not have brought them here…."
    # hide river
    # show ch4 at left
    CH4 "On whose command!"
    H2O "*eye roll*\nI thought you asked me for entertainment."
    h '''Who are you all?
I only recognise carbon dioxide, methane and nitrous dioxide.'''

    CO2 "*looks at hfc*\nTold ya we oldies are goldies."
    # hide h20
    # show co2
    # hide ch4
    # show hfc
    HFC '''*eye roll* 
Just because some humans are ignorant our value doesn't diminish''' 
    # show info kun
    i '''Majority of the GHGs think Havanah and River aren't aware of them.
    Can you help them to understand better?'''
    # hide info kun
menu:
    "Yes ": 
        pass
    "No" : 
        jump main_story


label SCENE_2_PART_2:
    # scene co2 form
    # show info kun
    i '''Carbon dioxide enters the atmosphere through burning fossil fuels 
(coal, natural gas, and oil), solid waste, trees and other biological materials
and also as a result of certain chemical reactions like cement production.'''
#   with fade
#   scene co2 elemination 
    i '''Carbon dioxide is removed from the atmosphere
when it is absorbed by plants as part of the biological carbon cycle.'''
#   with fade
#   scene ch4 form
    i '''Methane is formed at the production and transport of coal,natural gas, and oil.'''
    i '''Methane emissions also result from livestock and other agricultural practices,
land use, and by the decay of organic waste in municipal solid waste landfills.'''
#   with fade
#   scene ch4 elemination
    i '''Natural processes in soil and 
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
    i '''It can also be reduced through technological upgrades 
    and use of abatement equipment.
    '''
    # with fade
    # scene fc form
    i '''They are emitted through their use as substitutes 
for ozone-depleting substances like as refrigerants
and through a variety of industrial processes such as aluminum 
and semiconductor manufacturing.'''
    # with fade
    # scene fc elemination
    i '''Industrial fluorinated gases can reduce emissions by 
adopting fluorinated gas capture and destruction processors.'''
    i '''HFCs can be reduced through better system components 
and through the use of alternative refrigerants with
lower global warming potentials than those presently used.'''
    # with fade
    # hide info kun
    # show havana normal at left
    h '''There are natural processes to remove you CO2,
    methane and NO2 from atmosphere while there aren’t for FC.'''
    # show river normal
    r '''That’s about as much difference as there exists between 
you oldies and new gen GHG.
sheesh you all made it seem as if you don’t share a combined purpose.'''
    # show no2 at right
    NO2 "It appears that we underestimated your understanding of the matter at hand."
    # hide havana normal
    # show co2
    CO2 '''*shakes head* You kiddos might not be ignorant 
but we’re responsible for transforming your home into a boiling stew
thanks to mankind’s misplaced ideas of advancement.'''
    # show river confused
    r "Misplaced ideas of advancement?"
    NO2 '''Humans are convinced of their superiority.
As your kind relentlessly pursued socioeconomic and industrial prosperity,
you hastened the degradation of the very environment that sustains you.'''
    # hide river confused
    # show sf6
    SF6 "I’ve come across humans who claim that reports of our GWP are means to achieve fearmongering among the masses."
    SF6 '''It is almost funny how gullibly they continue to shrug off the effects of global warming that they experience first-hand.
    Talk about self-sabotage!'''
    SF6 "You could compare it to letting off a criminal in plain sight."
    CO2 '''Our results are practically rising at a rate greater
than that of any preventive measures 
adopted by humans to curtail our maleffects.'''
    # hide sf6
    # hide co2
    # hide no2

# show data_line_graph ghg_usa
#   show river shocked at left
    "..."
#   show havana shocked at right
    "..."
# hide data_line_graph ghg_usa
#   show ch4 smug
    CH4 '''Oho- It seems you are ignorant of the real time rising trends
we are setting because of the rising human population density.'''

    '''Majority of the GHGs think Havanah and River 
aren't aware of real time consequences of human activities.
Can you Help them to understand better?
Accept the second challenge of GHG or not?'''
menu:
    "Yes ": 
        pass
    "No" : 
        jump main_story


label q_1:
    #scene data_line_graph ghg_usa
    #with fade
    # show info kun
    i '''As the years go from 2005 to 2020
    what trend can be observed in the population density?'''
    # hide info kun
    menu:
        "A)  Slightly increasing trend":
            "Gas army" "Well done kiddo."
        "B)  Decreasing trend":
            "Gas army" '''Over time, we don’t see yellow hue increasing 
    and thus it is not a decreasing trend in population density.'''
            jump q_1
        "C)  Negligible change":
            "Gas army" "It was quite an ambiguous one to detect, not a bad attempt."
    jump q_2

label q_2:
    # scene bg co2_emission_trend
    i '''From the year 2015 to 2020 
    did the trend in CO2 emissions increase or decrease in general overall in India?'''
    menu:
        "Increase":
            "Gas Army" 'Well done.'
            jump main_story
        "Decrease":
            pass
        "No difference":
            pass
    i'''From bluer overall tint it changed to green,
and this according to the key means a rise in CO2 emissions.'''



label main_story:
    r '''There’s got to be something we could do
now that we know about population densities and
greenhouse gas emmissions correlation!'''
    h "Everyone I’ve ever looked up to would probably be disappointed to see us back down."
    play sound "audio/villian-theme.wav"  volume 0.5
    CO2 '''Humans have been ‘trying to do something’
    and has that ever been enough to stop us?'''
    stop sound
    h "Our ozone layer has not yet irreparably been depleted!"
    r "Yeah and—"
    
    jump scene3
