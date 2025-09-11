# LV 2nd Crew Shares

total_money = float(input("How much money does the crew have:"))
crew_members = float(input("How many crew members are there (not including captain and first mate):"))

# Total shares:
# Captain: 7
# First mate: 3
# Crew members: 1 each
total_shares = 7 + 3 + crew_members

# How much one share is worth
share_value = total_money / total_shares

# Calculate earnings
captain_earnings = round(share_value * 7,2)
first_mate_earnings = round(share_value * 3,2)
crew_member_earnings = round(share_value * 1,2)

# Each crew member already got $500
crew_member_needs = round(crew_member_earnings - 500,2)

# Print output
print("\n--- Final Share Report ---")
print(f"The captain gets: ${captain_earnings:.2f}")
print(f"The first mate gets: ${first_mate_earnings:.2f}")
print(f"Crew still needs: ${crew_member_needs:.2f}")