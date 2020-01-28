    def _getLineEndingsFromStyleSheet(self,):
        """Experimental function to get line endings from an SBML file.  Makes
        use of Python's ElementTree.

        Args: None

        Returns: dictionary, keys=line endings id, values=string of XML line
            ending block
        """
        line_endings = {}

        stylesheet_file_name = "LineEnding_styles.xml"
        stylesheet_file = Path(pkg_resources.resource_filename("libsbml_draw",
                               "model/libs/" + stylesheet_file_name))

        tree = ET.parse(stylesheet_file)

        nns_le = "lineEnding"

        root = tree.getroot()

        for le in root.findall(nns_le):
            line_endings[le.attrib["id"]] = ET.tostring(le, encoding="unicode")

        return line_endings
