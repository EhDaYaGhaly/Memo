import pymem
import pymem.process
import struct
import time

def get_process(name): #process class
    try:
        return pymem.Pymem(name)
    except Exception as e:
        print(f"Error: {e}")
        return None

def scan_memory(pm:pymem.Pymem, process_name, value):
    value_bytes = struct.pack("i", value)
    module = pymem.process.module_from_name(pm.process_handle, process_name)
    base_address = module.lpBaseOfDll
    size = module.SizeOfImage

    found_addresses = []
    try:
        memory = pm.read_bytes(base_address, size)
        for i in range(size - 4):
            if memory[i:i+4] == value_bytes:
                found_addresses.append(base_address + i)
    except:
        pass
    return found_addresses

def filter_changed_addresses(pm:pymem.Pymem, addresses, new_value):
    """ Filter only addresses that changed to the new value. """
    filtered_addresses = []
    new_value_bytes = struct.pack("i", new_value)

    print("\n📡 Waiting for values to change...\n")

    while True:
        for addr in addresses:
            try:
                if new_value_bytes == pm.read_bytes(addr, 4):
                    print(f"Address {hex(addr)} changed to {new_value}")
                    filtered_addresses.append(addr)

            except:
                print(f"Could not read memory at {hex(addr)}")

        if filtered_addresses:
            return filtered_addresses

        time.sleep(0.5) 

def modify_memory(pm, addresses, new_value):

    new_bytes = struct.pack("i", new_value) 
    for addr in addresses:
        try:
            pm.write_bytes(addr, new_bytes, 4)
            print(f"Modified value at {hex(addr)} to {new_value}")
        except:
            print(f"Failed to modify memory at {hex(addr)}")

