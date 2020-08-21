BUILDER_STRING = """
<MenuScreen>:
    GridLayout:
        cols: 1
        
        GridLayout:
            cols: 2
            Button:
                text: 'Strength'
                on_press: 
                    root.manager.current = 'strength'
                    root.manager.transition.direction = 'left'
            Button:
                text: 'Strength\\nMaintenance'
                size_hint_x: None
                width: 160
                on_press: 
                    root.manager.current = 'strengthmain'
                    root.manager.transition.direction = 'left'
            
        GridLayout:
            cols: 2
            Button:
                text: 'Power'
                on_press: 
                    root.manager.current = 'power'
                    root.manager.transition.direction = 'left'
                
            Button:
                text: 'Power\\nMaintenance'
                size_hint_x: None
                width: 160
                on_press: 
                    root.manager.current = 'powermain'
                    root.manager.transition.direction = 'left'
            
        GridLayout:
            cols: 2
            Button:
                text: 'Power Endurance'
                on_press: 
                    root.manager.current = 'pe'
                    root.manager.transition.direction = 'left'
                
            Button:
                text: 'Power Endurance\\nMaintenance'
                size_hint_x: None
                width: 160
                on_press: 
                    root.manager.current = 'pemain'
                    root.manager.transition.direction = 'left'
        Button:
            text: 'Prehab'
            on_press: 
                root.manager.current = 'prehab'
                root.manager.transition.direction = 'left'

"""