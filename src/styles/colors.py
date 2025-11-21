COLORS = {
    "bg_base":     "#0A0A0A",    
    "bg_panel":    "#0A0A0A",    
    "border":      "#69747C",    
    "text_main":   "#F4F4F9",    
    "text_soft":   "#B8DBD9",    
    "accent":      "#04724D",    
    "accent_hover":"#035539",    
    "input_bg":    "#0f1210",    
    "input_border":"#2d3833",    
}

def setup_theme():
    import customtkinter as ctk
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")