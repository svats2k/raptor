import os
import sys
from pathlib import Path
from rich import print

# module_path = os.path.abspath(os.path.join(".."))
# if module_path not in sys.path:
#    sys.path.append(module_path)
# print(module_path)

FDIR = Path(__file__).resolve().parent
sys.path.append((FDIR / "..").resolve().__str__())

print(sys.path)

from raptor import RetrievalAugmentation

RA = RetrievalAugmentation()

txt = Path("/home/srivatsas/work/data/llm_apps/data/txts/blueant/txt/HF_A00779-001.txt")
RA.add_documents(txt.read_text())
