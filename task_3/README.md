<h1 align="center">
      Linux Core Utilities
</h1>
<h2 align="left"> fdisk </h2>
<p>
    This package contains the classic fdisk, sfdisk and cfdisk partitioning utilities from the util-linux suite.

The utilities included in this package allow you to partition your hard disk. The utilities supports both modern and legacy partition tables (eg. GPT, MBR, etc).

The fdisk utility is the classical text-mode utility. The cfdisk utilitity gives a more userfriendly curses based interface. The sfdisk utility is mostly for automation and scripting uses.
</p>
<h3 align="center">1,cfdisk </h3>
  <p align= "center">
         Display or manipulate a disk partition table
      
 
## root@kali:~# cfdisk -h

Usage:
 cfdisk [options] <disk>

Display or manipulate a disk partition table.

Options:
 -L, --color[=<when>]     colorize output (auto, always or never)
                            colors are enabled by default
 -z, --zero               start with zeroed partition table
     --lock[=<mode>]      use exclusive device lock (yes, no or nonblock)
 -r, --read-only          forced open cfdisk in read-only mode

 -h, --help               display this help
 -V, --version            display version

For more details see cfdisk(8).
      
      
      </p>
