"""Subclass of FrameVolumes, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db

# Implementing FrameVolumes
class FrameVolumes( guiperfumes.FrameVolumes ):
	def __init__( self, parent ):
		guiperfumes.FrameVolumes.__init__( self, parent )
		self.atualizarGrid()

	def adicionarVolume(self, event):
		nome = self.txtNome.GetValue()
		db.inserirVolume(nome)
		wx.MessageBox(message="Volume Inserido com Sucesso", caption="SysPerfumes", style=wx.OK, parent=self)
		self.atualizarGrid()

	def fecharFrame(self, event):
		self.Show(False)

	def atualizarVolume(self, event):
		nome_volume = self.gridVolumes.GetCellValue(event.GetRow(), event.GetCol())
		if nome_volume:
			id_volume = int(self.gridVolumes.GetCellValue(event.GetRow(), 0))
			db.atualizarVolume(id_volume, nome_volume)
			wx.MessageBox(message="Volume Atualizado com Sucesso", caption="SysPerfumes", style=wx.OK, parent=self)

	def atualizarGrid(self):
		if self.gridVolumes.GetNumberRows() > 0:
			self.gridVolumes.DeleteRows(0, self.gridVolumes.GetNumberRows())  # Limpa a tabela
		volumes = db.listarVolume()
		for volume in volumes:
			self.gridVolumes.AppendRows(1)
			self.gridVolumes.SetCellValue(self.gridVolumes.GetNumberRows() - 1, 0, str(volume[0]))
			self.gridVolumes.SetCellValue(self.gridVolumes.GetNumberRows() - 1, 1, volume[1])
			self.gridVolumes.SetReadOnly(self.gridVolumes.GetNumberRows() - 1, 0, True)


