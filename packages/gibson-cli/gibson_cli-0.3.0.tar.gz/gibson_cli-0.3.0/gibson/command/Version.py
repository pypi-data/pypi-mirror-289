from gibson.command.BaseCommand import BaseCommand
from gibson.conf.Version import Version as VersionConf


class Version(BaseCommand):
    def execute(self):
        self.conversation.type(f"{VersionConf.num}\n")
        self.conversation.newline()
        return True
