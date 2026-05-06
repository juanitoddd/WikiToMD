from bs4 import Tag


def extract_latex(node: Tag) -> str:
    """Extract a LaTeX expression from a Wikipedia math node.

    Wikipedia exposes the original TeX source in `alttext` on the rendered <math>
    element, and as the `alt` attribute on the fallback image. Prefer those over
    re-deriving LaTeX from MathML.
    """
    tex = node.get("alttext")
    if not tex:
        img = node.find("img")
        if img is not None:
            tex = img.get("alt")
    if not tex:
        annotation = node.find("annotation", {"encoding": "application/x-tex"})
        if annotation is not None:
            tex = annotation.get_text()
    if not tex:
        return node.get_text()

    tex = tex.strip()
    is_block = "mwe-math-fallback-image-display" in (node.get("class") or [])
    return f"$$\n{tex}\n$$" if is_block else f"${tex}$"
