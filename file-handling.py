def file_read_write_challenge():
    """
    File Read & Write Challenge with Error Handling
    Reads a file, modifies its content, and writes to a new file
    """
    
    print("📁 File Read & Write Challenge 🖋️")
    print("=" * 40)
    
    while True:
        try:
            # Get input filename from user
            input_filename = input("\nEnter the input filename (or 'quit' to exit): ").strip()
            
            if input_filename.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            if not input_filename:
                print("❌ Please enter a valid filename.")
                continue
            
            # Try to read the file
            try:
                with open(input_filename, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                print(f"✅ Successfully read: {input_filename}")
                
                # Modify the content (example modifications)
                modified_content = modify_content(content)
                
                # Get output filename
                output_filename = get_output_filename(input_filename)
                
                # Write to new file
                try:
                    with open(output_filename, 'w', encoding='utf-8') as file:
                        file.write(modified_content)
                    
                    print(f"✅ Successfully wrote modified content to: {output_filename}")
                    print(f"📊 Original file size: {len(content)} characters")
                    print(f"📊 Modified file size: {len(modified_content)} characters")
                    
                    # Show preview
                    show_preview(content, modified_content)
                    
                except PermissionError:
                    print(f"❌ Permission denied: Cannot write to {output_filename}")
                except IOError as e:
                    print(f"❌ Error writing to file: {e}")
                
            except FileNotFoundError:
                print(f"❌ File not found: {input_filename}")
                suggest_similar_files(input_filename)
                
            except PermissionError:
                print(f"❌ Permission denied: Cannot read {input_filename}")
                
            except UnicodeDecodeError:
                print(f"❌ Encoding error: Could not read {input_filename} as text file")
                try_binary_mode(input_filename)
                
            except IOError as e:
                print(f"❌ Input/Output error: {e}")
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. 👋")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


def modify_content(content):
    """Modify the file content with various transformations"""
    
    print("\n🔄 Modifying content...")
    
    # Example modifications (customize as needed)
    modifications = [
        ("Original content", "Modified content"),
        ("hello", "HELLO"),
        ("world", "WORLD"),
        ("the", "THE"),
        ("and", "AND")
    ]
    
    modified = content
    
    for old, new in modifications:
        if old in modified:
            modified = modified.replace(old, new)
            print(f"   Replaced '{old}' with '{new}'")
    
    # Add timestamp
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    modified = f"/* Modified on: {timestamp} */\n\n" + modified
    
    return modified


def get_output_filename(input_filename):
    """Generate output filename based on input filename"""
    import os
    
    base_name = os.path.splitext(input_filename)[0]
    extension = os.path.splitext(input_filename)[1] or '.txt'
    
    counter = 1
    while True:
        output_filename = f"{base_name}_modified_{counter}{extension}"
        if not os.path.exists(output_filename):
            return output_filename
        counter += 1


def suggest_similar_files(filename):
    """Suggest similar files if the requested file doesn't exist"""
    import os
    import difflib
    
    if not os.path.exists('.'):
        return
    
    files_in_dir = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    if files_in_dir:
        # Find similar filenames
        similar_files = difflib.get_close_matches(filename, files_in_dir, n=3, cutoff=0.6)
        
        if similar_files:
            print("💡 Did you mean one of these files?")
            for similar_file in similar_files:
                print(f"   - {similar_file}")


def try_binary_mode(filename):
    """Handle binary files differently"""
    print("💡 This might be a binary file. Trying binary mode...")
    
    try:
        with open(filename, 'rb') as file:
            binary_content = file.read(100)  # Read first 100 bytes
        
        print(f"📊 File appears to be binary (first bytes: {binary_content[:10]}...)")
        print("ℹ️ Binary files cannot be modified as text.")
        
    except Exception as e:
        print(f"❌ Error reading binary file: {e}")


def show_preview(original, modified):
    """Show a preview of changes"""
    print("\n📋 Preview of changes:")
    print("-" * 30)
    
    # Show first few lines of original and modified
    original_lines = original.split('\n')[:3]
    modified_lines = modified.split('\n')[:3]
    
    print("Original (first 3 lines):")
    for i, line in enumerate(original_lines, 1):
        print(f"{i}: {line[:50]}{'...' if len(line) > 50 else ''}")
    
    print("\nModified (first 3 lines):")
    for i, line in enumerate(modified_lines, 1):
        print(f"{i}: {line[:50]}{'...' if len(line) > 50 else ''}")
    
    print("-" * 30)


def create_sample_file():
    """Create a sample file for testing"""
    sample_content = """Hello world!
This is a sample text file for testing.
The quick brown fox jumps over the lazy dog.
Python is a great programming language.
File handling is an important skill.
Good luck with your programming journey!"""
    
    with open('sample.txt', 'w') as file:
        file.write(sample_content)
    
    print("✅ Created sample.txt for testing")


# Main program execution
if __name__ == "__main__":
    print("Welcome to the File Read & Write Challenge! 🚀")
    
    # Offer to create a sample file
    create_sample = input("Would you like to create a sample file for testing? (y/n): ").lower()
    if create_sample in ['y', 'yes']:
        create_sample_file()
        print("You can now use 'sample.txt' as input filename.")
    
    # Start the main program
    file_read_write_challenge()