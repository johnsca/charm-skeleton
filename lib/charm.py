#!/usr/bin/env python3

from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus


class SkeletonCharm(CharmBase):

    state = StoredState()

    def __init__(self, parent, key):
        super().__init__(parent, key)
        self.framework.observe(self.on.install, self.on_install)

    def on_install(self, event):
        self.state.installed = True
        self.framework.model.unit.status = ActiveStatus('ready')


if __name__ == '__main__':
    main(SkeletonCharm)
