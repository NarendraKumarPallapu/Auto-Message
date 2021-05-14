kv="""
RelativeLayout:
    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        MDToolbar:
            elevation: 11
            title: "   Auto Message"
            font_style:'H3'
            right_action_items: [["share", lambda x: app.name_mean()]]
        ScrollView:
    MDTextField:
        id: message
        hint_text: "Enter the Message"
        mode:"rectangle"
        pos_hint: {"center_x":.5,"center_y": .6}
        size_hint:0.600,0.120
        font_size:30
        multiline:True
        helper_text: "Message needed"
        helper_text_mode: "on_focus"
    MDTextField:
        id: number
        hint_text: "Enter the Phone Number"
        mode:"rectangle"
        pos_hint: {"center_x":.5,"center_y": .8}
        size_hint:0.600,0.120
        font_size:30
        helper_text: "Numbers should be 10"
        helper_text_mode: "on_error"
        max_text_length: 10
        
    
        

    
    MDFillRoundFlatButton:
        id:check
        text:"OK"
        pos_hint: {"center_x":.5,"center_y": .4}
        padding:"10dp"
        theme_text_color: 'Custom'
        text_color: (1,1,1,1)
        on_press:app.data()
    MDRaisedButton:
        text: "Change Theme"
        md_bg_color: 1, 0, 1, 1
        pos_hint: {"center_x":.5,"center_y": .1}
        padding:"10dp"
        on_release:app.show_theme_picker()
    MDFloatLayout:

        MDRaisedButton:
            id:time
            text: "Set the Time"
            pos_hint: {'center_x': .5, 'center_y':.2}
            on_release: app.show_time_picker()

"""