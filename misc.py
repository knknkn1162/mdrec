from pathlib import Path
import base64
import mimetypes

def src2base64(src):
    src_path = Path(src)

    mimetypes.init()
    minetype = mimetypes.types_map[src_path.suffix]
    # detect file open-mode from minetype
    mode = "rb" if str(minetype).startswith("image") else "rt"
    with open(src, mode) as f:
        asset64_bytes = base64.b64encode(f.read())
    asset64_string = asset64_bytes.decode('ascii')
    return 'data:{0};base64,{1}'.format(minetype, asset64_string)
