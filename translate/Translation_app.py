import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
#list of language
Languages={
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Assamese': 'as',
    'Aymara': 'ay',
    'Azerbaijani': 'az',
    'Bambara': 'bm',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bhojpuri': 'bho',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chichewa': 'ny',
    'Chinese (simplified)': 'zh-CN',
    'Chinese (traditional)': 'zh-TW',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dhivehi': 'dv',
    'Dogri': 'doi',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Ewe': 'ee',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Frisian': 'fy',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Guarani': 'gn',
    'Gujarati': 'gu',
    'Haitian creole': 'ht',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Igbo': 'ig',
    'Ilocano': 'ilo',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Kinyarwanda': 'rw',
    'Konkani': 'gom',
    'Korean': 'ko',
    'Krio': 'kri',
    'Kurdish (kurmanji)': 'ku',
    'Kurdish (sorani)': 'ckb',
    'Kyrgyz': 'ky',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lingala': 'ln',
    'Lithuanian': 'lt',
    'Luganda': 'lg',
    'Luxembourgish': 'lb',
    'Macedonian': 'mk',
    'Maithili': 'mai',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Maltese': 'mt',
    'Maori': 'mi',
    'Marathi': 'mr',
    'Meiteilon (manipuri)': 'mni-Mtei',
    'Mizo': 'lus',
    'Mongolian': 'mn',
    'Myanmar': 'my',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Odia (oriya)': 'or',
    'Oromo': 'om',
    'Pashto': 'ps',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Spanish': 'es',
    'Sundanese': 'su',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tajik': 'tg',
    'Tamil': 'ta',
    'Tatar': 'tt',
    'Telugu': 'te',
    'Thai': 'th',
    'Tigrinya': 'ti',
    'Tsonga': 'ts',
    'Turkish': 'tr',
    'Turkmen': 'tk'
}

def translate():
    text=input_text.get("1.0","end").strip()
    target_language=Languages.get(language_var.get())
    
    if not text:
        messagebox.showwarning("Input Error","please enter your text.")
        return
    
    try: 
        translated=GoogleTranslator(source="auto",target=target_language).translate(text)
        output_text.delete("1.0","end")
        output_text.insert("end",translated)
    except Exception as e:
        messagebox.showerror("Translation error",str(e))
        
    


#create window 
window=tk.Tk()
window.title("language translator")
window.geometry("700x700")
#window.resizable(False,False)
window.configure(bg="lightgray")



# input label and text box
tk.Label(window,text="Enter your text to translate:",font=("Cambria",16)).pack(pady=10)
input_text=tk.Text(window,height=6,wrap="word",font=("Cambria",16))
input_text.pack(pady=15)


#language selection dropdown_menu
language_var=tk.StringVar()
language_var.set("Choose your language")
ttk.Label(window,text="Select target language:",font=("Cambria",16)).pack(pady=5)
ttk.Combobox(window,textvariable=language_var ,values=list(Languages.keys()),state="readonly").pack()


tk.Button(window,text="Translate", command=translate ,font=("Cambria",16),bg="green",fg="white").pack(pady=10)

# output label & textbox
tk.Label(window,text="Translated text:",font=("Cambria",16)).pack(pady=10)
output_text=tk.Text(window,height=6,wrap="word",font=("Cambria",16))
output_text.pack(pady=15)


# run the gui
window.mainloop()