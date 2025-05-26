import flet as ft


class Controller:
    def __init__(self, view, model):
        self._albumScelto = None
        self._view = view
        self._model = model

    def handleCreaGrafo(self, e):
        durata = self._view._txtInDurata.value
        try:
            durata = int(durata)
        except ValueError:
            self._view.create_alert("Devi inserire un valore numerico per la durata!")
            return
        self._model.buildGraph(durata)
        nodi, archi = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato!"))
        self._view.txt_result.controls.append(ft.Text(f"#Vertici: {nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"#Archi: {archi}"))
        nodes = self._model.getNodi()
        for n in nodes:
            self._view._ddAlbum.options.append(ft.dropdown.Option(key = n.Title, data = n, on_click=self.getSelectedAlbum))
        self._view.update_page()

    def getSelectedAlbum(self, e):
        self._albumScelto = e.control.data
        print(f"Selezionato {self._albumScelto}")

    def handleAnalisiComp(self, e):
        if self._albumScelto is None:
            self._view.create_alert("devi prima scegliere un album!")
            return
        dimensione, durata = self._model.getComponenteConnessa(self._albumScelto)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Componente connessa - {self._albumScelto}"))
        self._view.txt_result.controls.append(ft.Text(f"Dimensione componente = {dimensione}"))
        self._view.txt_result.controls.append(ft.Text(f"Durata componente = {durata}"))
        self._view.update_page()

    def handleGetSetAlbum(self, e):
        pass