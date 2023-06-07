# this code will be executed BEFORE level starts
# do what you want here to prepare computer for level
# USER WON'T SEE ANY OUTPUT FROM THIS FILE
import os
usr=os.environ.get("USER")
string_to_compare = "Bash is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell.[12][13] First released in 1989,[14] it has been used as the default login shell for most Linux distributions.[15] Bash was one of the first programs Linus Torvalds ported to Linux, alongside GCC.[16] A version is also available for Windows 10 and Windows 11 via the Windows Subsystem for Linux.[17][18] It is also the default user shell in Solaris 11.[19] Bash was also the default shell in versions of Apple macOS from 10.3 (originally, the default shell was tcsh) to 10.15 (macOS Catalina), which changed the default shell to zsh, although Bash remains available as an alternative shell."

if __name__ == "__main__":
    f = open(f'/home/{usr}/copy_me.txt', "a")
    f.write(string_to_compare)
    f.close()
    os.mkdir(f'/home/{usr}/copy_here')