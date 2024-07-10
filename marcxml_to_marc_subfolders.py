import os
from pymarc import parse_xml_to_array, MARCWriter
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_marcxml_to_marc(xml_directory, output_directory):
    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Walk through all files in the directory and subdirectories
    for root, _, files in os.walk(xml_directory):
        for filename in files:
            if filename.endswith(".xml"):
                xml_path = os.path.join(root, filename)
                
                # Create corresponding subdirectory structure in output directory
                relative_path = os.path.relpath(root, xml_directory)
                output_subdir = os.path.join(output_directory, relative_path)
                os.makedirs(output_subdir, exist_ok=True)

                marc_path = os.path.join(output_subdir, filename.replace(".xml", ".mrc"))

                try:
                    # Read MARCXML records
                    records = parse_xml_to_array(xml_path)

                    # Write to MARC file
                    with open(marc_path, 'wb') as marc_file:
                        writer = MARCWriter(marc_file)
                        for record in records:
                            writer.write(record)
                        writer.close()
                    logging.info(f"Successfully converted {xml_path} to {marc_path}")
                except Exception as e:
                    logging.error(f"Error processing {xml_path}: {e}")

# Example usage
convert_marcxml_to_marc(r'C:\Users\yvr2\Documents\ACO\marcxml', r'C:\Users\yvr2\Documents\ACO\marcxml')
