import psutil as p

def size(byte):

  for x in ["B","KB","MB","GB","TB"]:
    if byte<1024:
      return f"{byte:.2f}{x}"
    byte=byte/1024

def disk():
  file_disk = open("disk_usage.txt","a")
  file_disk.truncate(0)
  file_disk.write("")
  file_disk.write("Partitions on Drive:\n")


  par = p.disk_partitions()

  for x in par:
    file_disk.write("Drive: %s\n" %x.device)
    file_disk.write("  File system type: %s\n" %x.fstype)

    dsk = p.disk_usage(x.mountpoint)
    file_disk.write("  Total Size: %s \n" %size(dsk.total))
    file_disk.write("  Used:       %s  \n" %size(dsk.used))
    file_disk.write("  Free:       %s  \n" %size(dsk.free))
    file_disk.write("  Percentage: %s \n" %dsk.percent)
    file_disk.close()
  main()

def memory():
  file_ram = open("ram_usage.txt","a")
  file_ram.truncate(0)
  file_ram.write("")

  mem = p.virtual_memory()
  file_ram.write("Total Memory:    %s\n"%size(mem.total))
  file_ram.write("Available Memory:%s\n" %size(mem.available))
  file_ram.write("Used Memory:     %s\nexit" %size(mem.used))
  file_ram.write("Percentage:      %s\n"%mem.percent)

  swmem = p.swap_memory()
  file_ram.write("Total Memory:    %s\n" %size(swmem.total))
  file_ram.write("Available Memory:%s\n" %size(swmem.free))
  file_ram.write("Used Memory:     %s\n" %size(swmem.used))
  file_ram.write("Percentage:      %s\n" %swmem.percent)
  file_ram.close()
  main()


def cpu():

  file_cpu = open("cpu_usage.txt","w")
  file_cpu.truncate(0)
  
  file_cpu.write("Logical/Total Core Count: %s\n" %p.cpu_count(logical=True) )
  file_cpu.write("Physical Core Count: %s\n" %p.cpu_count(logical=False))

  
  fre=p.cpu_freq()
  file_cpu.write("Maximum Frequency:%s MHz\n" %fre.max)
  file_cpu.write("Minimum Frequency:%s MHz\n" %fre.min)
  file_cpu.write("Current Frequency: %s MHz\n"%fre.current)


  for x, percentage_usage in enumerate(p.cpu_percent(percpu=True)):
      file_cpu.write("Core" +str(x)+":" +str(percentage_usage)+"%\n")
  file_cpu.write("Total CPU Usage:%s\n" %p.cpu_percent())
  file_cpu.close()
  main()


def main():
  print("\nPress 1 for Disk Info. \nPress 2 for Memory/Ram Info. \nPress 3 for CPU Info. \nPress 0 to exit.")
  choice=int(input(">>> "))
  
  if choice==1: 
    disk()
  elif choice==2:
    memory()
  elif choice==3:
    cpu()
  elif choice==0:
    pass
  else:
    print("Please provide a valid input")


if __name__ == "__main__":
  main()
