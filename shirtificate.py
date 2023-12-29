from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 32)
        self.set_left_margin(60)
        self.cell(90, 10, "CS50 Shirtificate", border=0, align="C")
        self.ln(20)


def main():
    name = input("Name: ")
    create_shirt(name)


def create_shirt(name):
    pdf = PDF()
    pdf.add_page()
    pdf.set_text_color(255,255,255)
    pdf.set_font("helvetica", "B", 20)
    pdf.set_left_margin(10)
    pdf.image("shirtificate.png",w=pdf.epw)
    pdf.cell(0,-230,f"{name} took CS50",align="C")
    pdf.output("shirtificate.pdf")




if __name__ == "__main__":
    main()