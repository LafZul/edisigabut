from tkinter import *

ui=Tk()
ui.title('Penentuan Parameter Pandemi COVID-19 Berdasarkan Model Diskrit Sigmoid')


options = ['Afganistan',
        'Arab',
        'Cina',
        'India',
        'Inggris',
        'Itali',
        'Singapura'
        ]

dropname=StringVar()
dropname.set(options[0])

drop= OptionMenu(ui,dropname,*options).grid(row=0,column=0)

Button=Button(ui,text='Generate').grid(row=1,column=0)

labelSeparate_1=Label(ui, text='Separate_1 or Initial Day = Always First Day').grid(row=3,column=0)
labelSeparate_2=Label(ui, text='Separate_2').grid(row=4,column=0)
Separate_2=Entry(ui).grid(row=4,column=1)
labelSeparate_3=Label(ui, text='Separate_3').grid(row=5,column=0)
Separate_3=Entry(ui).grid(row=5,column=1)
labelSeparate_4=Label(ui, text='Separate_4').grid(row=6,column=0)
Separate_4=Entry(ui).grid(row=6,column=1)
labelSeparate_5=Label(ui, text='Separate_5').grid(row=7,column=0)
Separate_5=Entry(ui).grid(row=7,column=1)


labelR0_1=Label(ui, text='R0_1').grid(row=3,column=2)
R0_1=Entry(ui).grid(row=3,column=3)
labelR0_2=Label(ui, text='R0_2').grid(row=4,column=2)
R0_2=Entry(ui).grid(row=4,column=3)
labelR0_3=Label(ui, text='R0_3').grid(row=5,column=2)
R0_3=Entry(ui).grid(row=5,column=3)
labelR0_4=Label(ui, text='R0_4').grid(row=6,column=2)
R0_4=Entry(ui).grid(row=6,column=3)
labelR0_5=Label(ui, text='R0_5').grid(row=7,column=2)
R0_5=Entry(ui).grid(row=7,column=3)

labelD_1=Label(ui, text='D_1').grid(row=3,column=4)
D_1=Entry(ui).grid(row=3,column=5)
labelD_2=Label(ui, text='D_2').grid(row=4,column=4)
D_2=Entry(ui).grid(row=4,column=5)
labelD_3=Label(ui, text='D_3').grid(row=5,column=4)
D_3=Entry(ui).grid(row=5,column=5)
labelD_4=Label(ui, text='D_4').grid(row=6,column=4)
D_4=Entry(ui).grid(row=6,column=5)
labelD_5=Label(ui, text='D_5').grid(row=7,column=4)
D_5=Entry(ui).grid(row=7,column=5)

mainloop()