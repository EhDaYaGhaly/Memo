from src.memory_scanner import get_process, scan_memory, filter_changed_addresses, modify_memory ## todo : add option to keep filtering or modify all filtered addresses
def main():
    process_name = input("Enter process name: ")
    pm = get_process(process_name)

    if pm:
        initial_value = int(input("Enter initial value: "))
        found_addresses = scan_memory(pm, process_name, initial_value)

        if found_addresses:
            print("\n Found addresses:")
            for i, addr in enumerate(found_addresses):
                print(f"[{i}] {hex(addr)}")

            new_value = int(input("\nEnter the new value to filter addresses: "))
            filtered_addresses = filter_changed_addresses(pm, found_addresses, new_value)

            if filtered_addresses:
                print("\nFiltered addresses:")
                for addr in filtered_addresses:
                    print(f"{hex(addr)}")

                modify_value = int(input("\nEnter value to modify filtered addresses: "))
                modify_memory(pm, filtered_addresses, modify_value)
            else:
                print("No addresses changed to the new value.")
        else:
            print("No matching values found.")
if __name__ == "__main__":
    main()