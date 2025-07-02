from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML
from pathlib import Path
import uuid

TEMPLATE_DIR = Path(__file__).parent.parent / "templates"
OUTPUT_DIR = Path(__file__).parent.parent / "generated"
OUTPUT_DIR.mkdir(exist_ok=True)

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape(['html'])
)

def generate_pdf(data: dict) -> str:
    template = env.get_template("proposal_template.html")
    html_content = template.render(data=data)


    safe_name = data["client_name"].strip().replace(" ", "_")
    unique_id = uuid.uuid4().hex[:8]
    pdf_filename = f"proposal_{safe_name}_{unique_id}.pdf"

    pdf_path = OUTPUT_DIR / pdf_filename
    HTML(string=html_content).write_pdf(str(pdf_path))
    return str(pdf_path)
