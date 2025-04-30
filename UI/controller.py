import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        """Appende alla lista view tutte le coppie di aeroporto avente almeno una distanza pari a quella inserita dall'utente"""
        name = self._view.txt_name.value
        self._view.txt_name.value=""
        if name is None or name == "":
            self._view.create_alert("Inserisci una distanza minima")
            return
        self._view.txt_result.controls.clear()
        self._model.buildGraph(name)

        if self._model.getNumNodes()!=0:
            self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumEdges()}"))

            for edge in self._model.getEdges():
                a1=str(edge[0])
                a2=str(edge[1])
                weight=self._model.getEdgeWeight(edge)
                self._view.txt_result.controls.append(ft.Text(f"Da {a1} a {a2}, distanza media: {weight["weight"]}"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Non esistono aeroporti con la distanza media indicata."))

        self._view.update_page()
