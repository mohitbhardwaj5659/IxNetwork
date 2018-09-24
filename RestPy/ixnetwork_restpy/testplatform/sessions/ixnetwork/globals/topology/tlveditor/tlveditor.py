from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class TlvEditor(Base):
	"""The TlvEditor class encapsulates a system managed tlvEditor node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the TlvEditor property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'tlvEditor'

	def __init__(self, parent):
		super(TlvEditor, self).__init__(parent)

	@property
	def Defaults(self):
		"""An instance of the Defaults class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.defaults.Defaults)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.defaults import Defaults
		return Defaults(self)

	@property
	def Template(self):
		"""An instance of the Template class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.template.Template)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.tlveditor.template import Template
		return Template(self)

	def find(self):
		"""Finds and retrieves tlvEditor data from the server.

		All named parameters support regex and can be used to selectively retrieve tlvEditor data from the server.
		By default the find method takes no parameters and will retrieve all tlvEditor data from the server.

		Returns:
			self: This instance with matching tlvEditor data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of tlvEditor data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the tlvEditor data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)