<h1 align="center">
      Linux Core Utilities
</h1>
<h3 align="left"> 1,fdisk </h3>
<p>
    This package contains the classic fdisk, sfdisk and cfdisk partitioning utilities from the util-linux suite.

The utilities included in this package allow you to partition your hard disk. The utilities supports both modern and legacy partition tables (eg. GPT, MBR, etc).

The fdisk utility is the classical text-mode utility. The cfdisk utilitity gives a more userfriendly curses based interface. The sfdisk utility is mostly for automation and scripting uses.
      <p align="center">the main purpose is :- Display or  manipulate a disk partition table. </p>
</p>


          root@kali:~# fdisk -h
          Usage: fdisk [options] <disk>         change partition table
          fdisk [options] -l [<disk>...] list partition table(s)
          Options:
           -b, --sector-size <size>      physical and logical sector size
           -B, --protect-boot            don't erase bootbits when creating a new label
           -c, --compatibility[=<mode>]  mode is 'dos' or 'nondos' (default)
           -L, --color[=<when>]          colorize output (auto, always or never)
                                 colors are enabled by default
            -l, --list                    display partitions and exit
            -x, --list-details            like --list but with more details
            -n, --noauto-pt               don't create default partition table on empty devices
            -o, --output <list>           output columns
            -t, --type <type>             recognize specified partition table type only
            -u, --units[=<unit>]          display units: 'cylinders' or 'sectors' (default)
            -s, --getsz                   display device size in 512-byte sectors [DEPRECATED]
            --bytes                   print SIZE in bytes rather than in human readable format
            --lock[=<mode>]           use exclusive device lock (yes, no or nonblock)
             -w, --wipe <mode>             wipe signatures (auto, always or never)
             -W, --wipe-partitions <mode>  wipe signatures from new partitions (auto, always or never)

             -C, --cylinders <number>      specify the number of cylinders
             -H, --heads <number>          specify the number of heads
             -S, --sectors <number>        specify the number of sectors per track

             -h, --help                    display this help
             -V, --version                 display version

          Available output columns:
           gpt: Device Start End Sectors Size Type Type-UUID Attrs Name UUID
           dos: Device Start End Sectors Cylinders Size Type Id Attrs Boot End-C/H/S
                  Start-C/H/S
           bsd: Slice Start End Sectors Cylinders Size Type Bsize Cpg Fsize
           sgi: Device Start End Sectors Cylinders Size Type Id Attrs
           sun: Device Start End Sectors Cylinders Size Type Id Flags








<h3 align="left">2,cfdisk </h3>
  <p align= "center">
         Display or manipulate a disk partition table
      
 </p>




      
      
      
      root@kali:~# cfdisk -h
      Usage: cfdisk [options] <disk>
      
      Display or manipulate a disk partition table.
      Options:
      -L, --color[=<when>]     colorize output (auto, always or never)
                               colors are enabled by default 
       -z, --zero               start with zeroed partition table
     --lock[=<mode>]      use exclusive device lock (yes, no or nonblock)
      -r, --read-only          forced open cfdisk in read-only mode
      -h, --help               display this help
      -V, --version            display version

