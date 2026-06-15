from elftools.elf.elffile import ELFFile

def parse_elf(path):
    with open(path, "rb") as f:
        elf = ELFFile(f)

        sections = []
        for s in elf.iter_sections():
            sections.append({
                "name": s.name,
                "size": s["sh_size"],
                "addr": hex(s["sh_addr"])
            })

        return {
            "entry": hex(elf.header["e_entry"]),
            "sections": sections
        }