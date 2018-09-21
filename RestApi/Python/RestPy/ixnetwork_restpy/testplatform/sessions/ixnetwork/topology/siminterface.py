from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class SimInterface(Base):
	"""The SimInterface class encapsulates a system managed simInterface node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the SimInterface property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'simInterface'

	def __init__(self, parent):
		super(SimInterface, self).__init__(parent)

	@property
	def IsisL3PseudoInterface(self):
		"""An instance of the IsisL3PseudoInterface class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudointerface.IsisL3PseudoInterface)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudointerface import IsisL3PseudoInterface
		return IsisL3PseudoInterface(self)

	@property
	def IsisPseudoInterface(self):
		"""An instance of the IsisPseudoInterface class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudointerface.IsisPseudoInterface)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudointerface import IsisPseudoInterface
		return IsisPseudoInterface(self)

	@property
	def SimInterfaceEthernetConfig(self):
		"""An instance of the SimInterfaceEthernetConfig class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceethernetconfig.SimInterfaceEthernetConfig)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceethernetconfig import SimInterfaceEthernetConfig
		return SimInterfaceEthernetConfig(self)

	@property
	def SimInterfaceIPv4Config(self):
		"""An instance of the SimInterfaceIPv4Config class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv4config.SimInterfaceIPv4Config)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv4config import SimInterfaceIPv4Config
		return SimInterfaceIPv4Config(self)

	@property
	def SimInterfaceIPv6Config(self):
		"""An instance of the SimInterfaceIPv6Config class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv6config.SimInterfaceIPv6Config)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv6config import SimInterfaceIPv6Config
		return SimInterfaceIPv6Config(self)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	def find(self, Count=None, DescriptiveName=None, Name=None):
		"""Finds and retrieves simInterface data from the server.

		All named parameters support regex and can be used to selectively retrieve simInterface data from the server.
		By default the find method takes no parameters and will retrieve all simInterface data from the server.

		Args:
			Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group
			DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context
			Name (str): Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			self: This instance with matching simInterface data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of simInterface data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the simInterface data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)

	def Start(self):
		"""Executes the start operation on the server.

		Start CPF control plane (equals to promote to negotiated state).

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): The method internally sets Arg1 to the encapsulated list of hrefs for this instance

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self
		return self._execute('Start', payload=locals(), response_object=None)

	def Stop(self):
		"""Executes the stop operation on the server.

		Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

		Args:
			Arg1 (list(str[None|/api/v1/sessions/1/ixnetwork/topology])): The method internally sets Arg1 to the encapsulated list of hrefs for this instance

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self
		return self._execute('Stop', payload=locals(), response_object=None)
