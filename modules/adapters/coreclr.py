from __future__ import annotations
from ..typecheck import *

from .import adapter
from .. import dap
from .. import core

import shutil

class CoreCLR(adapter.AdapterConfiguration):
	
	type = 'coreclr'
	docs = 'https://github.com/Samsung/netcoredbg#getting-started'

	async def start(self, log: core.Logger, configuration: dap.ConfigurationExpanded):
		command = [
			"netcoredbg",
			"--interpreter=vscode"
		]
		return adapter.StdioTransport(log, command)

	async def install(self, log: core.Logger):
        if not (shutil.which('netcoredbg')):
            log.error('This adapter requires netcoredbg. Please install it and/or add it to your PATH variable.')

	async def installed_status(self, log: core.Logger):
		return None

	@property
	def installed_version(self):
		return "1.0"

	@property
	def configuration_snippets(self):
		return None

	@property
	def configuration_schema(self):
		return None