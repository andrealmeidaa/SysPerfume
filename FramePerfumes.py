"""Subclass of FramePerfumes, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db

# Implementing FramePerfumes
class FramePerfumes( guiperfumes.FramePerfumes ):
	def __init__( self, parent ):
		guiperfumes.FramePerfumes.__init__( self, parent )


		# Virtual event handlers, overide them in your derived class
	def exibirFormPerfumes(self, event):
		marcas = db.listarMarca()
		nome_marcas = []
		for marca in marcas:
			nome_marcas.append(marca[1])
		self.searchMarca.AutoComplete(choices=nome_marcas)
		volumes=db.listarVolume()
		nome_volumes=[]
		for volume in volumes:
			nome_volumes.append(volume[1])
		self.searchVolume.AutoComplete(choices=nome_volumes)
		fixacoes= db.listarFixacao()
		nome_fixacoes = []
		for fixacao in fixacoes:
			nome_fixacoes.append(fixacao[1])
		self.searchFixacao.AutoComplete(choices=nome_fixacoes)