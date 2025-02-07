import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))
from debug_script_with_vscode.script import entry
entry()