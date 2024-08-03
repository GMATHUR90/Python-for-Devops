#Using Disk Utilities: It is crucial for managing and assessing the performance
#                      of storage devices in a system.

# Disk Utilities

#1. fdisk: An interactive utility for partitioning disks. It allows you to create, delete,
#          and manage partitions on a hard disk.
#2. parted: Another powerful interactive tool for disk partitioning. It can handle more
#           complex partitioning schemes and larger disks compared to fdisk.
#3. lsblk: Lists information about all available or specified block devices.
#4. blkid: Identifies or prints block device attributes.
#5. df: Report file system disk space usage.
#6. du: Estimate file space usage.

#Measuring Disk Performance

#Throughput: Throughput is a measurement of bits or bytes per second that can be processed 
#            by a storage device. .

#Input/Output Operations per second(IOPS): IOPS refers to the number of read/write 
#                                          operations per second.

# 1. Using 'dd': It is to perform low-level copying and can be used to measure disk performance

# Example for measuring throughput:

#sudo dd if=/dev/zero of=/dev/sdc count=10 bs=100M

# This commands write 10 records fo 100MB each, giving you throughput rate.

"""
10+0 records in
10+0 records out
1048576000 bytes (1.0 GB, 1000 MiB) copied, 1.01127 s, 1.0 GB/s
"""
# Here, it writes data at a rate of 1 GB/s, indicating throughput.

# 2. Using 'iostat'
# sudo apt install sysstat
# The 'iostat' command provides statistics on CPU and I/O devices.It can be used alongside
# 'dd' to measure IOPS.

# Example for measuring IOPS:

# iostat -d /dev/sdc 1

# This command gives you detailed I/O statistics for the specified device per sec.

"""
O/P: Device tps kB_read/s kB_wrtn/s kB_read kB_wrtn
sdc 6813.00 0.00 1498640.00 0 1498640
sdc 6711.00 0.00 1476420.00 0 1476420

"""
# 'tps': (transaction per sec) is equivalent to IOPS.
# 'kB_read/s' and kB_wrtn/s' : show the read and write throughput respectively.

#Combining 'dd' and 'iostat':

#clear terminal output for easier reading:
# while true; do clear && iostat -d /dev/sdc && sleep 1; done

# Best practice:
# 1. Verify the device
# 2. Backup Important data
# 3. Use a Test Environment
 # Be careful to avoid data loss




