import subprocess

# Read domains from bd.txt
try:
    with open('targets.txt', 'r') as f:
        domains = f.read().splitlines()
except FileNotFoundError:
    print("Error: The file 'bd.txt' was not found.")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading 'bd.txt': {e}")
    exit(1)

# Output file for all domains
output_file = 'all_subdomains.txt'

# Run sublist3r for each domain and append the results to the file
with open(output_file, 'w') as out_f:
    for domain in domains:
        print(f"Enumerating subdomains for {domain} ...")
        try:
            result = subprocess.run(['sublist3r', '-d', domain, '-o', 'temp.txt'], check=True)
            if result.returncode == 0:
                with open('temp.txt', 'r') as temp_f:
                    out_f.write(f"Subdomains for {domain}:\n")
                    out_f.write(temp_f.read())
                    out_f.write("\n")
                print(f"Subdomains for {domain} have been appended to {output_file}")
            else:
                print(f"Error: sublist3r returned a non-zero exit code for {domain}.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running sublist3r for {domain}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
