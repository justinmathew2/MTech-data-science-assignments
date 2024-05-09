class Pharmacy:
    def __init__(self, name, phone, locality, delivery_status):
        self.name = name
        self.phone = phone
        self.locality = locality
        self.delivery_status = delivery_status

    def __str__(self):
        return f"{self.name}: {self.delivery_status}"

class PharmacyHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def HashId(self, key):
        # hash function to convert key into an index in the hash table
        return sum([ord(c) for c in key]) % self.capacity

    def insert(self, pharmacy):
        # Inserts the given pharmacy object into the hash table
        index = self.HashId(pharmacy.name)
        if not self.buckets[index]:
            self.buckets[index] = []
        self.buckets[index].append(pharmacy)
        self.size += 1

    def find_by_delivery_status(self, status):
        # Finds all pharmacies in the hash table with the given delivery status      
        result = []
        for bucket in self.buckets:
            if bucket:
                for pharmacy in bucket:
                    if pharmacy.delivery_status == status:
                        result.append(pharmacy)
        return result

    def find_by_locality(self, locality):
        # Finds all pharmacies in the hash table located in the given locality
        result = []
        for bucket in self.buckets:
            if bucket:
                for pharmacy in bucket:
                    if pharmacy.locality == locality:
                        result.append(pharmacy)  
        # This check is for Invalid Locality Exception                   
        if not result:
          result="Error"           
        return result
        
    def delivery_report(self):
        delivered = 0
        for bucket in self.buckets:
            if bucket:
                for pharmacy in bucket:
                    if pharmacy.delivery_status == "Delivered":
                        delivered += 1
        return delivered

# Read input from file and populate hash table
pharmacy_table = PharmacyHashTable(10)  # choose capacity based on expected size
with open("inputPS04.txt", "r+") as f:
    content = f.read()
    if not content.endswith('\n'):
        f.write('\n')

with open("inputPS04.txt", "r") as f:
    lines = f.readlines()

# Eliminate duplicate rows using set()
unique_lines = set(lines)
with open("inputPS04.txt", "w") as f:
    for line in unique_lines:
        f.write(line)

# Reading the input file and Adding pharmacy names and other details into the system.
with open("inputPS04.txt", "r") as f:
    lines = set(f.readlines())
    for line in lines:
        name, phone, locality, status = line.strip().split(" / ")
        pharmacy = Pharmacy(name, phone, locality, status)
        pharmacy_table.insert(pharmacy)

# Write output to file
with open("outputPS04.txt", "w") as f:
    f.write(f"Successfully inserted {pharmacy_table.size} records into the system.\n")
    # Reading the prompts file to answer the given problem statement 
    with open("promptsPS04.txt", "r") as fil:
      lines=fil.readlines()
      for line in lines:
        # Find a list of pharmacies with different delivery status (yet to deliver, out for delivery)
        if(line.strip()=="Delivery Status"):
          for pharmacy in pharmacy_table.find_by_delivery_status("Yet to Deliver"):
            f.write(str(pharmacy) + "\n")
          for pharmacy in pharmacy_table.find_by_delivery_status("Out for Delivery"):
            f.write(str(pharmacy) + "\n")
        # Generate a report on the number of pharmacies to whom delivery has been done    
        elif(line.strip()=="Delivered"):
          f.write("Number of Pharmacies for which delivery completed: "+str(pharmacy_table.delivery_report())+"\n")
          for pharmacy in pharmacy_table.find_by_delivery_status(line.strip()):
            f.write(pharmacy.name + "\n")
        else:
          # Exception handling in case of Invalid Locality
          if pharmacy_table.find_by_locality(line.strip())=="Error":
              f.write("Invalid Locality: "+ line.strip()+"\n")
          else:
            # Generate a list of pharmacies located in a given locality.
            for pharmacy in pharmacy_table.find_by_locality(line.strip()):
              if pharmacy_table.find_by_locality(line.strip()):
                f.write(pharmacy.name + "\n")

