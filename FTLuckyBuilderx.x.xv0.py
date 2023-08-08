# Create helper class
class Helper:

  def __init__(self):
    self.name = "Clippy"
    self.personality = "friendly"
  
  def greet(self):
    print(f"{self.name}: Hi there! How can I help you edit the ROM today?")

  def check_in(self):
    print(f"{self.name}: Just checking in! How is the hex editing going?")
  
  def assist(self):
    # Scan ROM for issues
    issues = scan_rom_issues(rom)
    
    if issues:
      print(f"{self.name}: I noticed some potential issues in the ROM:")
      for issue in issues:
        print(f"- {issue['description']} at {hex(issue['offset'])}")
      # Offer to fix
      if input(f"{self.name}: Would you like me to try fixing these automatically? (y/n)") == "y":
        fixes = auto_fix_issues(issues)
        print(f"{self.name}: Applied {len(fixes)} fixes to the ROM.")
    else:
      print(f"{self.name}: The ROM is looking good!")
        
  def encourage(self):
    print(f"{self.name}: You're doing great! Keep up the good work.")
    
  def farewell(self):
    print(f"{self.name}: All done hex editing? Have a nice day! I'm always here if you need me.")

# Create instance    
helper = Helper()

# Call periodically  
helper.greet()
helper.check_in()
helper.encourage()
helper.assist()
helper.farewell()