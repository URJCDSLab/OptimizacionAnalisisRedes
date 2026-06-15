import os
import glob

tex_dir = r"C:\Users\vacek\Proyectos\OptimizacionAnalisisRedes\diapositivas_tex"
files = glob.glob(os.path.join(tex_dir, "*.tex"))

for fpath in files:
    filename = os.path.basename(fpath)
    name, ext = os.path.splitext(filename)
    dest_path = os.path.join(tex_dir, name + "_src.qmd")
    
    # Try decoding with utf-8 first, then latin-1
    content = None
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            print(f"Decoded {filename} with UTF-8")
    except UnicodeDecodeError:
        try:
            with open(fpath, "r", encoding="latin-1") as f:
                content = f.read()
                print(f"Decoded {filename} with Latin-1")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            
    if content is not None:
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved {dest_path}")
