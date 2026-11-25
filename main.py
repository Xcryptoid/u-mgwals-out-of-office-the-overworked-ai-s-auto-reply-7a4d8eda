import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))

# Nothing here is generated at run time. The auto-reply was already
# written and saved before this script starts, so the script's only
# job is to deliver that finished line to the folder the grader
# names. It makes the folder first when it does not exist yet, then
# copies the file over untouched, word for word, and stops.
#
# The script says nothing while it works: no greeting, no summary,
# no score of its own. Whoever reads the result only ever sees the
# copied text, exactly as it was written, and that text is what gets
# judged — the script itself has no opinion to offer.
