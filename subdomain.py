import os
import subprocess


def check_tool_availability(tool_name):
    """Check if a tool is available in the system."""
    return subprocess.call(["which", tool_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0


def clean_and_validate_subdomains(input_file, output_file):
    """Clean and validate subdomains from the input file and save them to the output file."""
    cleaned_set = set()
    try:
        with open(input_file, "r") as infile:
            for line in infile:
                subdomain = line.strip()
                # Exclude wildcard subdomains and validate format
                if subdomain.startswith("*") or not "." in subdomain:
                    continue
                cleaned_set.add(subdomain)

        with open(output_file, "w") as outfile:
            for subdomain in sorted(cleaned_set):  # Sort for consistency
                outfile.write(f"{subdomain}\n")

        print(f"Cleaned and validated subdomains saved to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"Unexpected error during cleaning and validation: {e}")


def main():
    print("Starting Subdomain Takeover Finder...\n")

    # Check for required tools
    if not check_tool_availability("assetfinder"):
        print("Error: 'assetfinder' is not installed or not available in the PATH.")
        return

    if not check_tool_availability("subzy"):
        print("Error: 'subzy' is not installed or not available in the PATH.")
        return

    # Get domain input from the user
    domain = input("Enter the domain (e.g., example.com): ").strip()

    # Name of the TXT files
    raw_txt_filename = f"{domain.split('.')[0]}_raw.txt"
    clean_txt_filename = f"{domain.split('.')[0]}_cleaned.txt"

    try:
        print("Running assetfinder...")
        # Run assetfinder to collect subdomains
        with open(raw_txt_filename, "w") as txt_file:
            subprocess.run(["assetfinder", domain], stdout=txt_file, check=True)
        print(f"Assetfinder output saved to {raw_txt_filename}.")

        print("Cleaning and validating subdomains...")
        # Clean and validate subdomains
        clean_and_validate_subdomains(raw_txt_filename, clean_txt_filename)

        print("Running subzy...")
        # Run subzy to check for subdomain takeover
        subprocess.run(["subzy", "run", "--targets", clean_txt_filename], check=True)

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure 'assetfinder' and 'subzy' are installed and available in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error: An issue occurred while running a command. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
