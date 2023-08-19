from model import DataStructure
from pylatex import LongTable, Document, FlushLeft, NewPage, Command, Package, Math, Tabularx, Center, Figure
from pylatex.utils import NoEscape
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import Draw
import os
import shutil


def generate_individual(data: DataStructure):

    cur_path = Path.cwd()
    logo_dir = cur_path / "pic" / "logo.png"

    first_page_header_footer = NoEscape(r"""
\newgeometry{left=10mm,right=10mm,top=40mm,bottom=40mm}%
\pagestyle{fancy}
\fancyhf{}  % 清除原有设置
\fancyhead[R]{\centerline{\includegraphics[width=3cm]{""" + str(logo_dir) + r"""}}}%
\fancyfoot[L]{\copyright\ 2023 RakeAI LLC. All rights reserved.}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
                                        """)
    other_page_header_footer = NoEscape(r"""
    \newgeometry{left=10mm,right=10mm,top=40mm,bottom=25mm}
    """)

    doc = Document()
    # packages
    doc.packages.append(Package('fancyhdr'))
    doc.packages.append(Package('geometry'))
    doc.packages.append(Package("graphicx"))
    doc.packages.append(Package("newtxmath"))
    doc.packages.append(Package("atbegshi"))

    doc.preamble.append(first_page_header_footer)
    # doc.preamble.append(Command("geometry", arguments="left=15mm,right=15mm,top=20mm,bottom=20mm"))
    doc.preamble.append(
        Command(
            "setlength",
            arguments=NoEscape(r"\headheight"),
            options={},
            extra_arguments="2cm"))

    doc.append(Command("fontsize", arguments=["18", "20"]))
    # title
    doc.append(Math(data="\\mathrm{%s}" % data.title, escape=False))

    doc.append(NoEscape(r'\vspace{0.5cm}'))
    doc.append(NoEscape(r"\noindent\rule{\textwidth}{1pt}"))
    # title information
    with doc.create(Center()) as center:
        doc.append(NoEscape(r"\renewcommand{\arraystretch}{2}"))
        with doc.create(Tabularx(table_spec=r">{\bfseries\normalsize}l X<{\raggedleft\normalsize}", width_argument=NoEscape(r"\linewidth"))) as title_info:
            for k, v in data.base_information.items():
                if k != "title":
                    title_info.add_row((k, v))

    doc.append(NoEscape(r"\renewcommand{\arraystretch}{1.5}"))
    doc.append(NoEscape(r"\noindent\rule{\textwidth}{1pt}"))

    doc.append(NewPage())
    # other pages' header and foot are different
    doc.append(other_page_header_footer)

    with doc.create(FlushLeft()):
        doc.append(NoEscape(
            r"""Table 1. The representative structure of a series of lipid structures predicted by LNPCompassTM. The
        probability of effectiveness stands for the probability of a functional lipid structure that can deliver RNA
        with a formulation of lipid/cholesterol/DSPC/DMG-PEG2000=50/38.5/10/1.5."""))

    with doc.create(Center()):
        doc.append(NoEscape(r"\renewcommand{\arraystretch}{2}"))
        # remember add a } in the end
        doc.append(NoEscape(r"\setlength{\tabcolsep}{5.2mm}{"))
        with doc.create(LongTable(table_spec=r"|>{\centering\arraybackslash}p{5mm}|>{\centering\arraybackslash}p{1cm}|>{\centering\arraybackslash}p{6.5cm}|>{\centering\arraybackslash}p{2cm}|")) as table:
            table.add_hline()
            table.add_row([NoEscape("Top"), "Name", "Structure",
                          "Probability of Effectiveness"])
            doc.append(NoEscape(r"\endfirsthead"))
            table.add_hline()
            table.add_row(["Top", "Name", "Structure",
                          "Probability of Effectiveness"])
            doc.append(NoEscape(r"\endhead"))
            # table.add_hline()

            if os.path.exists("./tmp"):
                shutil.rmtree("./tmp")
            os.mkdir("./tmp")
            for index, d in enumerate(data.data):
                table.add_hline()
                line_data = [index] + [v for _, v in d.model_dump().items()]
                pic_name = f"tmp/{index}.png"
                pic_dir = str(cur_path / pic_name)
                mo = Chem.MolFromSmiles(d.structure)
                Draw.MolToFile(mo, pic_name)
                line_data[2] = NoEscape(
                    r"\raisebox{-0.1cm}[2.5cm]{\includegraphics[height=2.5cm]{" + pic_dir + r"}}")
                # line_data[2] = StandAloneGraphic(image_options="height=2cm", filename=cur_path / line_data[2])
                table.add_row(line_data)
            table.add_hline()
        doc.append(NoEscape("}"))

    doc.generate_pdf(filepath=cur_path / "report", clean_tex=False)
    shutil.rmtree("./tmp")
