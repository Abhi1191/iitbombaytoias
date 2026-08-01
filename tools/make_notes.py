"""
Generates two ORIGINAL, copyright-free study PDFs for the site:
  - Vulnerable-Sections-Notes.pdf   (detailed notes, fed to the chatbot)
  - Vulnerable-Sections-MindMap.pdf (one-page revision mind map)

All wording here is original. Facts referenced (Article numbers, Act names,
scheme names) are public information and are not copyrightable.
"""
from fpdf import FPDF
from fpdf.enums import XPos, YPos

BRAND = (17, 24, 39)        # #111827
ACCENT = (37, 99, 235)      # #2563eb
NAVY = (30, 58, 138)        # #1e3a8a
LIGHT = (238, 242, 255)     # #eef2ff
GREY = (85, 85, 85)

SITE = "IIT Bombay To IAS"

# ----------------------------------------------------------------------------
# Notes content: list of (heading, [paragraph|('bullets',[...])])
# ----------------------------------------------------------------------------
NOTES = [
    ("Introduction: Who are the Vulnerable Sections?", [
        "Vulnerable sections are groups that face a higher risk of social, economic, "
        "or political exclusion because of historical discrimination, poverty, lack of "
        "access to resources, or limited social power. Protecting them is a constitutional "
        "goal rooted in the ideals of justice, equality, and dignity.",
        ("bullets", [
            "Common groups: Scheduled Castes (SCs), Scheduled Tribes (STs), Other Backward Classes (OBCs), women, children, the elderly, persons with disabilities, minorities, and transgender persons.",
            "Wider groups also studied: denotified and nomadic tribes, manual scavengers, bonded and migrant workers, internally displaced persons, refugees, and victims of trafficking.",
            "Vulnerability is often intersectional: a poor tribal girl with a disability faces overlapping disadvantages that reinforce one another.",
            "Dimensions of vulnerability: economic (poverty, landlessness), social (caste, stigma), political (weak voice), and physical (disability, age, ill health).",
            "The State's role is both protective (legal safeguards and commissions) and enabling (welfare, empowerment, and affirmative action).",
            "Approach has shifted over time from charity to welfare, and now to a rights-and-empowerment model.",
        ]),
    ]),
    ("Constitutional Safeguards (Overview)", [
        "The Constitution provides a layered framework of fundamental rights, directive "
        "principles, fundamental duties, and dedicated commissions to protect weaker sections.",
        ("bullets", [
            "Preamble: promises social, economic and political justice, equality of status and opportunity, and dignity of the individual.",
            "Article 14: Equality before law and equal protection of the laws.",
            "Article 15: Prohibits discrimination on grounds of religion, race, caste, sex or place of birth; 15(3) allows special provisions for women and children; 15(4)/15(5) for backward classes, SCs and STs.",
            "Article 16: Equality of opportunity in public employment, with reservation provisions in 16(4).",
            "Article 17: Abolition of untouchability, backed by the Protection of Civil Rights Act 1955.",
            "Article 19 and 21: Freedoms and the right to life and personal liberty, read expansively to include dignity, health, shelter and livelihood.",
            "Article 21A: Right to free and compulsory education for children aged 6-14.",
            "Article 23 and 24: Prohibit human trafficking, begar and forced labour, and child labour in hazardous work.",
            "Article 25-28: Freedom of religion; Articles 29-30: cultural and educational rights of minorities.",
            "Directive Principles - Articles 38, 39, 39A, 41, 45, 46, 47: duty of the State to reduce inequality, provide free legal aid, and promote the welfare and education of weaker sections.",
            "Articles 330, 332 and 243D: reservation of seats for SCs and STs in legislatures and local bodies (including for women).",
            "Articles 338, 338A and 338B: National Commissions for SCs, STs and Backward Classes.",
            "Fifth and Sixth Schedules: special administration of scheduled and tribal areas.",
        ]),
    ]),
    ("Scheduled Castes (SCs)", [
        "Scheduled Castes are communities that suffered from untouchability and social "
        "exclusion, notified by the President under Article 341.",
        ("bullets", [
            "Core problems: untouchability, atrocities, landlessness, low literacy, and occupational segregation.",
            "Key laws: Protection of Civil Rights Act 1955 and the SC/ST (Prevention of Atrocities) Act 1989, which defines specific atrocities and sets up special courts.",
            "The 1989 Act was strengthened by amendments in 2015 and 2018 to speed up trials and prevent dilution of arrest provisions.",
            "Reservation: in education, public employment, and legislatures, based on Articles 15(4), 16(4) and 330/332.",
            "Schemes: Post-Matric and Pre-Matric Scholarships, the SC Sub-Plan, and support through the National Scheduled Castes Finance and Development Corporation.",
            "Institution: the National Commission for Scheduled Castes (Article 338).",
        ]),
    ]),
    ("Other Backward Classes (OBCs)", [
        "OBCs are socially and educationally backward classes identified for affirmative action.",
        ("bullets", [
            "Mandal Commission (1980) recommended 27% reservation for OBCs in central services.",
            "Indra Sawhney v. Union of India (1992): upheld 27% OBC reservation, introduced the creamy layer concept, and capped total reservation at 50%.",
            "102nd Constitutional Amendment (2018): gave constitutional status to the National Commission for Backward Classes (Article 338B).",
            "105th Constitutional Amendment (2021): restored the power of states to identify their own OBC lists.",
            "EWS reservation: the 103rd Amendment (2019) added 10% reservation for the economically weaker sections of unreserved categories.",
        ]),
    ]),
    ("Scheduled Tribes and PVTGs", [
        "Scheduled Tribes are communities notified under Article 342, marked by distinctive "
        "culture, geographical isolation and economic backwardness. Particularly Vulnerable "
        "Tribal Groups (PVTGs) are the most disadvantaged tribes and need focused support.",
        ("bullets", [
            "Criteria for ST status (Lokur Committee): indications of primitive traits, distinctive culture, geographical isolation, shyness of contact, and backwardness.",
            "PVTG identification criteria: pre-agricultural level of technology, very low literacy, a stagnant or declining population, and relative geographical isolation.",
            "There are 75 notified PVTGs in India.",
            "Legal and governance safeguards: the Fifth and Sixth Schedules, PESA Act 1996 (self-governance in scheduled areas), and the Forest Rights Act 2006 (recognises individual and community forest rights).",
            "Key schemes: Eklavya Model Residential Schools (EMRS), Vanbandhu Kalyan Yojana, Development Action Plan for STs, Pradhan Mantri Adi Adarsh Gram Yojana, and PM-JANMAN for PVTG welfare.",
            "Minimum Support Price for Minor Forest Produce and the TRIFED Van Dhan Vikas Kendras support tribal livelihoods.",
            "Focus areas: education, healthcare, nutrition, forest rights, livelihood, and basic infrastructure.",
            "Institution: the National Commission for Scheduled Tribes (Article 338A).",
        ]),
    ]),
    ("Denotified, Nomadic and Semi-Nomadic Tribes (DNTs)", [
        "DNTs were wrongly branded as 'criminal tribes' under the colonial Criminal Tribes "
        "Act 1871; they were denotified after independence but still face deep stigma.",
        ("bullets", [
            "The Criminal Tribes Act was repealed in 1952, but the Habitual Offenders Acts continued the stigma in some states.",
            "Idate Commission (2017) studied DNTs and recommended a permanent commission and targeted welfare.",
            "A Development and Welfare Board for DNTs (DWBDNC) and the SEED scheme (education, health, livelihood, housing) support these communities.",
            "Key challenges: lack of documents, no fixed residence, exclusion from welfare schemes, and social prejudice.",
        ]),
    ]),
    ("Manual Scavenging", [
        "Manual scavenging - the manual handling of human excreta - is a dehumanising "
        "practice linked to caste, and is prohibited by law.",
        ("bullets", [
            "Key law: Prohibition of Employment as Manual Scavengers and their Rehabilitation Act 2013, which bans the practice and hazardous cleaning of sewers and septic tanks.",
            "Safai Karamchari Andolan v. Union of India (2014): the Supreme Court directed rehabilitation and compensation for deaths in sewers and septic tanks.",
            "Scheme: the Self Employment Scheme for Rehabilitation of Manual Scavengers (SRMS) and the NAMASTE scheme for safe sanitation work and mechanisation.",
            "Institution: the National Commission for Safai Karamcharis.",
        ]),
    ]),
    ("Bonded and Migrant Labour", [
        "Bonded labour is a form of forced labour where a person works to repay a debt on "
        "unfair terms; migrant workers face insecurity, low wages and poor conditions.",
        ("bullets", [
            "Constitutional basis: Article 23 prohibits forced labour and begar.",
            "Key laws: Bonded Labour System (Abolition) Act 1976 and the Inter-State Migrant Workmen Act 1979.",
            "Bandhua Mukti Morcha v. Union of India (1984): the Supreme Court laid down guidelines for identifying and freeing bonded labourers.",
            "Central Sector Scheme for Rehabilitation of Bonded Labourers provides financial and livelihood support.",
            "The four Labour Codes (Wages; Industrial Relations; Social Security; Occupational Safety, Health and Working Conditions) aim to consolidate and universalise protections.",
            "The e-Shram portal registers unorganised and migrant workers to extend social security.",
        ]),
    ]),
    ("Child Labour", [
        "Child labour is work that deprives children of their childhood, potential, and dignity, "
        "and that harms their physical or mental development.",
        ("bullets", [
            "Scale: As per Census 2011, a significant share of children were engaged as main or marginal workers; the problem is concentrated in a few states.",
            "Demand-side drivers: cheap and docile labour, a large informal economy, and certain industries (for example carpet weaving, bangle-making, plantations).",
            "Supply-side drivers: poverty, indebtedness, lack of nearby schools, poor quality of schooling, and low awareness.",
            "Constitutional basis: Article 24 (no child below 14 in factories, mines, or hazardous work), Article 39(e) and 39(f), Article 45, and Article 21A.",
            "Key laws: Child Labour (Prohibition and Regulation) Act 1986 and its 2016 amendment - a complete ban on employing children below 14, and a ban on adolescents (14-18) in hazardous occupations.",
            "Supporting laws: Factories Act 1948, Mines Act 1952, and the Right to Education Act 2009.",
            "Programmes: National Child Labour Project (NCLP) and the PENCIL online portal for enforcement and rehabilitation.",
            "International: India has ratified ILO Conventions 138 (minimum age) and 182 (worst forms of child labour).",
            "Notable NGOs: Bachpan Bachao Andolan, CRY, and Butterflies.",
        ]),
    ]),
    ("Juvenile Delinquency", [
        "Juvenile delinquency refers to the involvement of minors in unlawful behaviour. "
        "The approach in India emphasises reform and rehabilitation rather than punishment.",
        ("bullets", [
            "Explanatory theories: Strain theory (stress and loss push youth toward crime), Subculture theory (isolated groups develop anti-social norms), Differential Opportunity theory (blocked legitimate opportunities increase delinquency), and Labelling theory (being tagged a 'criminal' reinforces the behaviour).",
            "Contributing factors: poverty, family breakdown, poor neighbourhoods, substance abuse, harmful peer groups, school dropout, and exposure to violent media.",
            "Juvenile Justice (Care and Protection of Children) Act 2015: allows 16-18 year olds accused of heinous offences to be tried as adults after assessment by a Juvenile Justice Board.",
            "Institutions: Juvenile Justice Boards, Child Welfare Committees, observation homes, and special homes.",
            "The Act gives statutory status to the Central Adoption Resource Authority (CARA) and streamlines adoption.",
            "International frameworks: the Beijing Rules, the Riyadh Guidelines, the Havana Rules, and the UN Convention on the Rights of the Child (UNCRC).",
        ]),
    ]),
    ("Child Protection and the POCSO Act", [
        "The Protection of Children from Sexual Offences (POCSO) Act, 2012 is a dedicated, "
        "gender-neutral law to protect children from sexual abuse and exploitation.",
        ("bullets", [
            "Defines a child as any person below 18 years and covers penetrative and non-penetrative assault, sexual harassment, and pornography.",
            "Key features: special courts for speedy trials, in-camera proceedings that protect the child's identity, mandatory reporting, and child-friendly medical examination.",
            "The burden of proof lies on the accused, and there is no time limit for reporting an offence.",
            "POCSO Amendment 2019: stricter minimum punishments, including the death penalty for aggravated penetrative sexual assault, and tighter provisions on child pornography.",
            "POCSO Rules 2020: mandatory police verification of staff in institutions housing children and a child protection policy.",
            "Institutions and tools: the National Commission for Protection of Child Rights (NCPCR), the CHILDLINE 1098 helpline, a cyber-crime reporting portal, and the National Database on Sexual Offenders.",
            "Related: the Prohibition of Child Marriage Act 2006 and Integrated Child Protection Scheme (Mission Vatsalya).",
        ]),
    ]),
    ("Human Trafficking", [
        "Human trafficking is the recruitment or movement of people through force, fraud or "
        "coercion for exploitation, including forced labour, sexual exploitation and organ trade.",
        ("bullets", [
            "Constitutional basis: Article 23 prohibits trafficking in human beings.",
            "Key laws: the Immoral Traffic (Prevention) Act 1956 and provisions of the Bharatiya Nyaya Sanhita (earlier IPC Section 370).",
            "Anti-Human Trafficking Units (AHTUs) operate at the district level, supported by a dedicated online portal.",
            "India has ratified the UN Convention against Transnational Organized Crime and its Palermo Protocol on trafficking.",
            "Ujjawala scheme supports the prevention, rescue, rehabilitation and reintegration of victims of trafficking.",
        ]),
    ]),
    ("Women", [
        "Women face gender-based discrimination, violence, unequal pay, and low workforce "
        "participation despite strong constitutional protection.",
        ("bullets", [
            "Constitutional support: Article 15(3) (special provisions), Article 39(d) (equal pay for equal work), Article 42 (maternity relief), Article 51A(e) (renouncing practices derogatory to women), and Articles 243D/243T (reservation in local bodies).",
            "106th Constitutional Amendment (2023): the Nari Shakti Vandan Adhiniyam provides for 33% reservation for women in the Lok Sabha and state assemblies.",
            "Key laws: Protection of Women from Domestic Violence Act 2005, Sexual Harassment of Women at Workplace (POSH) Act 2013, Dowry Prohibition Act 1961, Prohibition of Child Marriage Act 2006, and the Maternity Benefit (Amendment) Act 2017 (26 weeks leave).",
            "Landmark cases: Vishaka v. State of Rajasthan (1997) on workplace harassment guidelines, and Shah Bano and Shayara Bano (triple talaq) on personal law and equality.",
            "Schemes: Beti Bachao Beti Padhao, One Stop Centre (Sakhi), Ujjwala LPG scheme, Mahila Shakti Kendra, Pradhan Mantri Matru Vandana Yojana, and self-help groups under the National Rural Livelihoods Mission.",
            "Institution: the National Commission for Women.",
        ]),
    ]),
    ("Senior Citizens (Elderly)", [
        "India's elderly population is rising rapidly, creating needs around income security, "
        "health care, and protection from neglect and abuse.",
        ("bullets", [
            "Key law: Maintenance and Welfare of Parents and Senior Citizens Act 2007, which makes maintenance of parents and senior citizens a legal obligation and provides for tribunals.",
            "Constitutional basis: Article 41 (right to assistance in old age) and Article 21.",
            "Policy: the National Policy for Older Persons 1999 and the National Programme for the Health Care of the Elderly.",
            "Schemes: Indira Gandhi National Old Age Pension Scheme, the Integrated Programme for Senior Citizens, Rashtriya Vayoshri Yojana (aids and appliances), SACRED portal for elderly employment, and the SAGE initiative for elder-care start-ups.",
            "Support services: helplines such as Elderline (14567) and welfare programmes for care and dignity.",
        ]),
    ]),
    ("Persons with Disabilities (PwD)", [
        "The approach to disability has shifted from a medical and charity view to a social "
        "and rights-based model that removes barriers to participation.",
        ("bullets", [
            "Key law: Rights of Persons with Disabilities (RPwD) Act 2016, which recognises 21 disabilities and provides 4% reservation in government jobs and 5% in higher education.",
            "The Act mandates accessibility, non-discrimination, and additional benefits for persons with benchmark disabilities (40% or more).",
            "Other laws: the National Trust Act 1999 (for autism, cerebral palsy, intellectual disability and multiple disabilities) and the Mental Healthcare Act 2017.",
            "Programme: the Accessible India Campaign (Sugamya Bharat Abhiyan) for barrier-free built environment, transport and information.",
            "Support: the ADIP scheme for aids and appliances, Unique Disability ID (UDID) card, and scholarships.",
            "Institution: the Office of the Chief Commissioner for Persons with Disabilities; India has ratified the UN Convention on the Rights of Persons with Disabilities (UNCRPD).",
        ]),
    ]),
    ("Transgender Persons", [
        "Transgender persons face social exclusion, discrimination in employment and health "
        "care, and violence; recent law and judgments affirm their dignity and rights.",
        ("bullets", [
            "NALSA v. Union of India (2014): the Supreme Court recognised transgender persons as a third gender and affirmed their fundamental rights and self-identification.",
            "Navtej Singh Johar v. Union of India (2018): decriminalised consensual same-sex relations by reading down Section 377.",
            "Key law: Transgender Persons (Protection of Rights) Act 2019, which prohibits discrimination and provides for identity certificates, welfare, and a National Council for Transgender Persons.",
            "Support: Garima Greh shelter homes and the SMILE scheme (Support for Marginalised Individuals for Livelihood and Enterprise).",
        ]),
    ]),
    ("Minorities", [
        "Religious and linguistic minorities are protected against discrimination and are "
        "guaranteed cultural and educational rights.",
        ("bullets", [
            "Notified religious minorities: Muslims, Christians, Sikhs, Buddhists, Jains and Parsis (Zoroastrians).",
            "Constitutional basis: Articles 29 and 30 (cultural and educational rights, including the right to establish and administer institutions), and Articles 25-28 (freedom of religion).",
            "Law and institution: the National Commission for Minorities Act 1992 and the National Commission for Minorities.",
            "Sachar Committee (2006) highlighted the socio-economic backwardness of the Muslim community.",
            "Schemes: scholarships (Pre-Matric, Post-Matric, Merit-cum-Means), Nai Roshni (leadership for women), and skilling programmes.",
        ]),
    ]),
    ("Beggary and Destitution", [
        "Destitute persons and beggars are among the most invisible vulnerable groups, often "
        "criminalised rather than rehabilitated.",
        ("bullets", [
            "Many state anti-beggary laws (based on the Bombay Prevention of Begging Act 1959) treat begging as an offence.",
            "In Harsh Mander v. Union of India (2018), the Delhi High Court struck down provisions criminalising begging in Delhi as unconstitutional.",
            "The policy direction is towards rehabilitation, shelter, and livelihood rather than punishment.",
            "The SMILE scheme includes a component for the comprehensive rehabilitation of persons engaged in begging.",
        ]),
    ]),
    ("Key Committees and Commissions", [
        ("bullets", [
            "Lokur Committee (1965): advised on the revision of SC/ST lists and criteria for ST status.",
            "Mandal Commission (1980): recommended 27% reservation for OBCs.",
            "Bhuria Commission: examined tribal issues, self-governance and PESA.",
            "Sachar Committee (2006): studied the social, economic and educational status of Muslims.",
            "Xaxa Committee (2013): reviewed the socio-economic, health, and educational status of tribal communities.",
            "Idate Commission (2017): studied denotified, nomadic and semi-nomadic tribes.",
        ]),
    ]),
    ("Way Forward", [
        ("bullets", [
            "Move from welfare to empowerment: quality education, skilling, and sustainable livelihoods.",
            "Ensure last-mile delivery through better targeting, Aadhaar-linked benefits, technology, and social audits.",
            "Address intersectional disadvantage with convergent, community-based and gender-sensitive schemes.",
            "Strengthen data collection, awareness, legal aid, and grassroots participation of the affected groups.",
            "Fill vacancies and empower statutory commissions so that safeguards are enforced, not just enacted.",
            "Promote social attitude change to tackle stigma, discrimination and exclusion at their roots.",
        ]),
    ]),
]

# ----------------------------------------------------------------------------
# Mind map content: (branch title, [leaves])
# ----------------------------------------------------------------------------
MINDMAP = [
    ("Who & Why", ["Groups at risk of exclusion", "SC / ST / OBC", "Women, Children, Elderly", "PwD, Minorities, Transgender", "Intersectional disadvantage"]),
    ("Constitution", ["Art 14, 15, 16, 17", "Art 21A - Education", "Art 23, 24 - No forced/child labour", "DPSP 38, 39, 45, 46", "Commissions: 338 / 338A / 338B"]),
    ("Tribes & PVTGs", ["Art 342 - ST", "75 PVTGs", "PESA 1996, FRA 2006", "EMRS, Vanbandhu, PM-JANMAN", "5th & 6th Schedules"]),
    ("Child Labour", ["Art 24, 39(e)", "CLPR Act 1986 / 2016", "Factories 1948, Mines 1952", "RTE 2009", "NCLP + PENCIL portal"]),
    ("Juvenile Justice", ["JJ Act 2015", "16-18 heinous = adult trial", "JJ Board, CARA", "Strain / Subculture theory", "Beijing & Riyadh rules"]),
    ("POCSO / Children", ["POCSO Act 2012", "Amendment 2019", "Rules 2020", "NCPCR", "Special child courts"]),
    ("Women", ["Art 15(3), 39(d), 42", "DV Act 2005", "POSH Act 2013", "Dowry Prohibition 1961", "Beti Bachao Beti Padhao"]),
    ("Elderly / PwD / Trans", ["Sr. Citizens Act 2007", "RPwD Act 2016 - 21 types", "Accessible India", "NALSA 2014", "Transgender Act 2019"]),
]


class NotesPDF(FPDF):
    def header(self):
        self.set_fill_color(*BRAND)
        self.rect(0, 0, self.w, 22, "F")
        self.set_xy(12, 6)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, SITE, align="L")
        self.set_font("Helvetica", "", 9)
        self.set_xy(0, 6)
        self.set_x(-90)
        self.cell(78, 10, "Free Study Notes", align="R")
        self.ln(18)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*GREY)
        self.cell(0, 8, f"{SITE}  -  Original notes (facts are public domain)  -  Page {self.page_no()}", align="C")


def build_notes(path):
    pdf = NotesPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_margins(14, 24, 14)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(0, 10, "Vulnerable Sections of Society", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(0, 7, "Concise, exam-oriented notes for UPSC and State PCS. Written originally for "
                         f"{SITE}. Facts such as Article numbers, Act names and scheme names are public information.",
                   new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    for heading, blocks in NOTES:
        if pdf.get_y() > pdf.h - 45:
            pdf.add_page()
        pdf.set_font("Helvetica", "B", 14)
        pdf.set_text_color(*ACCENT)
        pdf.multi_cell(0, 8, heading, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_draw_color(*ACCENT)
        pdf.set_line_width(0.5)
        y = pdf.get_y() + 1
        pdf.line(14, y, pdf.w - 14, y)
        pdf.ln(3)

        for block in blocks:
            if isinstance(block, tuple) and block[0] == "bullets":
                pdf.set_font("Helvetica", "", 11)
                pdf.set_text_color(40, 40, 40)
                for item in block[1]:
                    pdf.set_x(16)
                    pdf.set_text_color(*ACCENT)
                    pdf.cell(5, 6, chr(149), new_x=XPos.RIGHT, new_y=YPos.TOP)
                    pdf.set_text_color(40, 40, 40)
                    pdf.multi_cell(0, 6, item, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    pdf.ln(0.5)
            else:
                pdf.set_font("Helvetica", "", 11)
                pdf.set_text_color(40, 40, 40)
                pdf.multi_cell(0, 6, block, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(1.5)
        pdf.ln(3)

    pdf.output(path)


def build_mindmap(path):
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    W, H = pdf.w, pdf.h

    # Title band
    pdf.set_fill_color(*BRAND)
    pdf.rect(0, 0, W, 20, "F")
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 5)
    pdf.cell(W, 10, "Vulnerable Sections of Society  -  Revision Mind Map", align="C")

    # Central node
    cx, cy = W / 2, H / 2
    node_w, node_h = 70, 20
    pdf.set_fill_color(*NAVY)
    pdf.set_draw_color(*NAVY)
    pdf.rect(cx - node_w / 2, cy - node_h / 2, node_w, node_h, "F", round_corners=True, corner_radius=4)
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(cx - node_w / 2, cy - node_h / 2 + 3)
    pdf.multi_cell(node_w, 6, "VULNERABLE\nSECTIONS", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Branch boxes: 4 left, 4 right
    box_w, box_h = 95, 30
    left_x = 12
    right_x = W - 12 - box_w
    ys = [26, 26 + 42, 26 + 84, 26 + 126]

    palette = [(37, 99, 235), (124, 58, 237), (22, 163, 74), (245, 158, 11)]

    for i, (title, leaves) in enumerate(MINDMAP):
        left = i < 4
        idx = i if left else i - 4
        x = left_x if left else right_x
        y = ys[idx]
        color = palette[idx]

        # connector
        pdf.set_draw_color(*color)
        pdf.set_line_width(0.7)
        start_x = x + box_w if left else x
        pdf.line(start_x, y + box_h / 2, cx - node_w / 2 if left else cx + node_w / 2, cy)

        # box
        pdf.set_fill_color(*color)
        pdf.rect(x, y, box_w, box_h, "F", round_corners=True, corner_radius=3)
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(255, 255, 255)
        pdf.set_xy(x + 3, y + 2)
        pdf.cell(box_w - 6, 6, title, new_x=XPos.LMARGIN, new_y=YPos.TOP)

        pdf.set_font("Helvetica", "", 8)
        pdf.set_xy(x + 3, y + 8.5)
        pdf.multi_cell(box_w - 6, 4.1, "\n".join("- " + leaf for leaf in leaves), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(*GREY)
    pdf.set_xy(0, H - 10)
    pdf.cell(W, 6, f"{SITE}  -  Original revision aid. Underlying facts are public information.", align="C")

    pdf.output(path)


if __name__ == "__main__":
    build_notes("resources/Vulnerable-Sections-Notes.pdf")
    build_mindmap("resources/Vulnerable-Sections-MindMap.pdf")
    print("Generated both PDFs.")
