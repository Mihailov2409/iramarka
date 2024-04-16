def colora_metall(self, x):
        self.d = x
        self.dп.md_bg_color = "red"

    def open_list_product(self):
        with open("List_ingridient.txt", "r", encoding="utf-8") as f:
            i_list = f.read()
        i_list = i_list.split(" ")
        win = ModalView(size_hint=(0.8, 0.8), background="image/bg1.png")
        scroll = ScrollView()
        listok = MDList(radius=[25, 0, 0, 0])
        for i in i_list:
            self.i = MDFillRoundFlatIconButton(text=i, text_color="black", icon="food")
            self.i.bind(on_press=lambda x: self.colora_metall(self.i))
            listok.add_widget(self.i)
        scroll.add_widget(listok)
        win.add_widget(scroll)
        win.open()