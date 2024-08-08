# Disk Utilities – fdisk , blkid and lsblk

# For retrieving specific device information

# 1. Using 'fdisk'

# fdisk is useful for displaying partition information but typically requires
# superuser permissions:

"""
O/P: (.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops$ sudo fdisk -l /dev/sda
Disk /dev/sda: 476.94 GiB, 512110190592 bytes, 1000215216 sectors
Disk model: SSD             
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 5D1703C0-1394-4EEE-95B3-EE550B2EE5B0

Device         Start        End   Sectors   Size Type
/dev/sda1       2048    1050623   1048576   512M EFI System
/dev/sda2    1050624  782301183 781250560 372.5G Linux filesystem
/dev/sda3  782301184  782333951     32768    16M Microsoft reserved
/dev/sda4  782333952 1000214527 217880576 103.9G Microsoft basic data

"""

# 2. Using 'blkid'

# 'blkid' provides detailed block device attributes. It is used to find
# UUIDs(Universally Unique Identifiers), filesystem types, and other attributes
# of these device and also requires superuser permissions.


# Here block device refers to any device that provides buffered access to data in
# fixed-size blocks. Block devices include storage devices such as hard drives, SSDs,
# CD-ROMs, and flask drives. They are different from characted devices, which provide
# unbuffered, direct access to data streams(like keyboards or mice).

# Characteristics of Block Devices:
# 1. Buffered Access: Data is read and written in blocks, typically 512 bytes or a
#    multiple thereof.
# 2. Random Access: You can read or write any block without reading the preceding 
#                   block.
# 3. Storage: Used to store and retrieve data from a non-volatile memory.

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops$ blkid
/dev/sda2: UUID="ae21117a-b0bb-45a3-866f-e5f96a681c2f" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="35757ea3-6f55-43ff-9969-45013cf4880b"

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops$ sudo blkid /dev/sda
/dev/sda: PTUUID="5d1703c0-1394-4eee-95b3-ee550b2ee5b0" PTTYPE="gpt"

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops$ sudo blkid -p /dev/sda
/dev/sda: PTUUID="5d1703c0-1394-4eee-95b3-ee550b2ee5b0" PTTYPE="gpt"
"""

# 3. lsblk
# lsblk provides detailed information about block devices without requiring superuser
# permission

"""
O/P:
(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop1    7:1    0     4K  1 loop /snap/bare/5
loop2    7:2    0 172.8M  1 loop /snap/brave/426
loop3    7:3    0   104M  1 loop /snap/core/16928
loop4    7:4    0 104.2M  1 loop /snap/core/17200
loop5    7:5    0  55.7M  1 loop /snap/core18/2823
loop6    7:6    0  55.7M  1 loop /snap/core18/2829
loop7    7:7    0  63.9M  1 loop /snap/core20/2264
loop8    7:8    0  63.9M  1 loop /snap/core20/2318
loop9    7:9    0  74.2M  1 loop /snap/core22/1380
loop10   7:10   0  74.2M  1 loop /snap/core22/1439
loop11   7:11   0  66.2M  1 loop /snap/core24/423
loop12   7:12   0  66.5M  1 loop /snap/cups/1052
loop13   7:13   0  67.8M  1 loop /snap/cups/1058
loop15   7:15   0 268.4M  1 loop /snap/firefox/4650
loop16   7:16   0 515.3M  1 loop /snap/gimp/428
loop17   7:17   0 515.7M  1 loop /snap/gimp/436
loop18   7:18   0 164.8M  1 loop /snap/gnome-3-28-1804/194
loop19   7:19   0 164.8M  1 loop /snap/gnome-3-28-1804/198
loop20   7:20   0 349.7M  1 loop /snap/gnome-3-38-2004/140
loop21   7:21   0 349.7M  1 loop /snap/gnome-3-38-2004/143
loop22   7:22   0 504.2M  1 loop /snap/gnome-42-2204/172
loop23   7:23   0 505.1M  1 loop /snap/gnome-42-2204/176
loop24   7:24   0   140K  1 loop /snap/gtk2-common-themes/13
loop25   7:25   0  91.7M  1 loop /snap/gtk-common-themes/1535
loop26   7:26   0  68.7M  1 loop /snap/notion-snap/16
loop27   7:27   0 175.7M  1 loop /snap/postman/264
loop28   7:28   0 173.1M  1 loop /snap/postman/266
loop29   7:29   0  12.9M  1 loop /snap/snap-store/1113
loop30   7:30   0  12.3M  1 loop /snap/snap-store/959
loop31   7:31   0  38.7M  1 loop /snap/snapd/21465
loop32   7:32   0  38.8M  1 loop /snap/snapd/21759
loop33   7:33   0   476K  1 loop /snap/snapd-desktop-integration/157
loop34   7:34   0   452K  1 loop /snap/snapd-desktop-integration/83
loop35   7:35   0 446.5M  1 loop /snap/telegram-desktop/6088
loop36   7:36   0 446.2M  1 loop /snap/telegram-desktop/6055
loop37   7:37   0  90.8M  1 loop /snap/whatsapp-for-linux/58
loop38   7:38   0  90.8M  1 loop /snap/whatsapp-for-linux/59
loop39   7:39   0 380.5M  1 loop /snap/zoom-client/228
loop40   7:40   0 379.4M  1 loop /snap/zoom-client/230
loop41   7:41   0 172.9M  1 loop /snap/brave/428
loop42   7:42   0 269.8M  1 loop /snap/firefox/4698
sda      8:0    0 476.9G  0 disk 
├─sda1   8:1    0   512M  0 part /boot/efi
├─sda2   8:2    0 372.5G  0 part /var/snap/firefox/common/host-hunspell
│                                /
├─sda3   8:3    0    16M  0 part 
└─sda4   8:4    0 103.9G  0 part 


To retrieve low-level device information:

(.venv) gauravmtwt1@gauravmtwt1-IdeaPad-3-15ADA05:~/Documents/Python for DevOps/github_python_topic_upload/Python-for-Devops$ lsblk -P /dev/sda2
NAME="sda2" MAJ:MIN="8:2" RM="0" SIZE="372.5G" RO="0" TYPE="part" MOUNTPOINTS="/var/snap/firefox/common/host-hunspell\x0a/"

Summary of Important Attributes
NAME: Identifies the partition.
MAJ
: Major and minor device numbers for system-level identification.
RM: Indicates if the device is removable.
SIZE: Size of the partition.
RO: Indicates if the partition is read-only.
TYPE: Confirms this is a partition.
MOUNTPOINTS: Shows where the partition is mounted in the filesystem.

"""

