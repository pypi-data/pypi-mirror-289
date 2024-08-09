import subprocess
import json

class ValeConfig:
    def __init__(self, config_ini):
        self.config_ini = config_ini

    def check_text(self, text, ext='.md'):
        vale_command = ["vale", "--config", self.config_ini, "--ext", ext, "--output", "JSON"]
        vale_output = subprocess.Popen(vale_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, errors = vale_output.communicate(text.encode())
        output = json.loads(output)
        if output:
            return output["stdin.adoc"]
        else:
            return []
