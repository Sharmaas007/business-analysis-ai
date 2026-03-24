class DocumentationGenerator:
    """
    A class to create Business Requirement Documents (BRD) and Software Requirement Specifications (SRS) from analyzed requirements.
    """

    def __init__(self, requirements):
        """
        Initialize the DocumentationGenerator with the given requirements.
        :param requirements: list of analyzed requirements
        """
        self.requirements = requirements

    def generate_brd(self):
        """
        Generate a Business Requirement Document (BRD).
        :return: str -- A BRD formatted string.
        """
        brd = """
        Business Requirement Document
        ==============================
        
        Overview:
        This document outlines the business requirements based on the analyzed requirements.
        
        Requirements:
        """
        for req in self.requirements:
            brd += f'- {req}\n'
        brd += """
        
        End of Document
        """
        return brd

    def generate_srs(self):
        """
        Generate a Software Requirement Specification (SRS).
        :return: str -- An SRS formatted string.
        """
        srs = """
        Software Requirement Specification
        ================================
        
        Overview:
        This document outlines the software requirements based on the analyzed business requirements.
        
        Requirements:
        """
        for req in self.requirements:
            srs += f'- {req}\n'
        srs += """
        
        End of Document
        """
        return srs
