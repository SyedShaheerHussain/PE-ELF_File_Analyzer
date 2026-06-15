import pefile

def parse_pe(path):
    pe = pefile.PE(path)

    sections = []
    for s in pe.sections:
        sections.append({
            "name": s.Name.decode(errors="ignore").strip("\x00"),
            "vaddr": hex(s.VirtualAddress),
            "vsize": s.Misc_VirtualSize,
            "rsize": s.SizeOfRawData
        })

    imports = {}
    if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll = entry.dll.decode(errors="ignore")
            funcs = []
            for imp in entry.imports:
                if imp.name:
                    funcs.append(imp.name.decode(errors="ignore"))
            imports[dll] = funcs

    exports = []
    if hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if exp.name:
                exports.append(exp.name.decode(errors="ignore"))

    return {
        "entry": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
        "image_base": hex(pe.OPTIONAL_HEADER.ImageBase),
        "sections": sections,
        "imports": imports,
        "exports": exports
    }