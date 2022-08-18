m "What noise do you want to listen to today?{nw}"
$ _history_list.pop()
menu:
    m "What noise do you want to listen to today?{fast}"
    
    "White noise":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/white.ogg"
        m "There you go, [player]!"

    "Pink noise":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/pink.ogg"
        m "There you go, [player]!"
        
    "Brown noise":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/brown.ogg"
        m "There you go, [player]!"        
        
    "Rain":
        m "Okay..."
        call mas_change_weather (mas_weather_rain, by_user=False)
        play music "mod_assets/sounds/music/sounds/rain.ogg"
        m "There you go, [player]!"

    "Thunderstorm":
        m "Okay..."
        call mas_change_weather (mas_weather_thunder, by_user=False)
        play music "mod_assets/sounds/music/sounds/thunder.ogg"
        m "There you go, [player]!" 
        
    "Rain on roof":
        m "Okay..."
        call mas_change_weather (mas_weather_rain, by_user=False)
        play music "mod_assets/sounds/music/sounds/rainroof.ogg"
        m "There you go, [player]!"  
        
    "Fireplace":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/fire.ogg"
        m "There you go, [player]!"           
        
     "River":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/river.ogg"
        m "There you go, [player]!"  
        
     "Waves":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/waves.ogg"
        m "There you go, [player]!"      
        
     "Fan":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/fan.ogg"
        m "There you go, [player]!"  
        
     "City":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/city.ogg"
        m "There you go, [player]!" 
        
     "Forest":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/forest.ogg"
        m "There you go, [player]!"       
        
     "Train":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/train.ogg"
        m "There you go, [player]!"          
        
     "Crickets":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/crickets.ogg"
        m "There you go, [player]!"  
        
     "Frogs":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/frogs.ogg"
        m "There you go, [player]!"  
        
     "Birds":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/birds.ogg"
        m "There you go, [player]!"  
        
     "Cicadas":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/cicadas.ogg"
        m "There you go, [player]!"
        
     "Seagulls":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/seagulls.ogg"
        m "There you go, [player]!"

     "Owls":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/owls.ogg"
        m "There you go, [player]!"
       
     "Whales":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/whales.ogg"
        m "There you go, [player]!"
        
     "Clock":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/clock.ogg"
        m "There you go, [player]!"  
        
     "Purring":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/purring.ogg"
        m "There you go, [player]!"  
        
     "Wind":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/wind.ogg"
        m "There you go, [player]!"  
        
     "Wind on trees":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/windtrees.ogg"
        m "There you go, [player]!"  
        
     "Shower":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/shower.ogg"
        m "There you go, [player]!"
        
     "Windchime":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/windchime.ogg"
        m "There you go, [player]!"
        
     "Typing":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/typing.ogg"
        m "There you go, [player]!"
        
     "Coffee shop":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/coffeeshop.ogg"
        m "There you go, [player]!"
        
     "Chatter":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/chatter.ogg"
        m "There you go, [player]!"
        
     "Office":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/office.ogg"
        m "There you go, [player]!"
        
     "Highway":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/highway.ogg"
        m "There you go, [player]!"
        
     "Uterus":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/uterus.ogg"
        m "There you go, [player]!"
        
     "Snowstorm":
        m "Okay..."
        call mas_change_weather (mas_weather_snow, by_user=False)
        play music "mod_assets/sounds/music/sounds/snowstorm.ogg"
        m "There you go, [player]!"
        
     "Heartbeat":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/heartbeat.ogg"
        m "There you go, [player]!"
        
     "Waterfall":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/waterfall.ogg"
        m "There you go, [player]!"
        
     "Waterdrops":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/waterdrops.ogg"
        m "There you go, [player]!"
        
     "Machinery":
        m "Okay..."
        play music "mod_assets/sounds/music/sounds/machinery.ogg"
        m "There you go, [player]!"
        
return
