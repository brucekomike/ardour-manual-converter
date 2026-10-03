# Getting More Plugins
The following list shows a few [plugin packages]{.dfn}. In some cases, a
package contains just one or two plugins; in other cases, dozens.

This list does not aim at being exhaustive.

## Plugins by Standard:

### LV2
{#LV2}

-   SWH <http://plugin.org.uk/lv2/> \[GNU GPLv3\]
-   ll-plugins <http://ll-plugins.nongnu.org/> \[GNU GPLv3\]
-   ZynAddSubFX <http://zynaddsubfx.sourceforge.net/> \[GNU GPLv2+\]
-   OvertoneDSP <https://www.overtonedsp.co.uk/> \[Proprietary\]
-   Invada Studio <https://launchpad.net/invada-studio/> \[GNU GPLv2\]
-   Pianoteq <https://www.pianoteq.com/> \[Proprietary\]

### LADSPA
{#LADSPA}

-   Kokkini Zita <http://kokkinizita.linuxaudio.org/linuxaudio/> \[GNU
    GPL/GNU GPLv3\]
-   Blepvco
    [http://www.smbolton.com/linux.html](http://smbolton.com/linux.html)
    \[GNU GPLv2+\]
-   Blop <http://blop.sourceforge.net/> \[GNU GPLv2\]
-   CAPS <http://quitte.de/dsp/caps.html> \[GNU GPLv3\]
-   CMT <http://www.ladspa.org/cmt/overview.html> \[GNU GPLv2\]
-   FOO <https://github.com/sampov2/foo-plugins> \[GNU GPLv2\]
-   NJL <https://github.com/tialaramex/njl-plugins> \[GNU GPLv2\]
-   Omins <http://www.nongnu.org/om-synth/omins.html> \[GNU GPLv3\]
-   SWH <http://plugin.org.uk/> \[GNU GPLv3\]
-   TAP <http://tap-plugins.sourceforge.net/> \[GNU GPLv2\]
-   VCF
    [http://www.suse.de/\~mana/ladspa.html](http://users.suse.com/~mana/ladspa.html)
    \[GNU LGPL\]
-   VLevel
    [http://vlevel.sourceforge.net/](http://vlevel.sourceforge.net/about/)
    \[GNU GPLv2\]
-   Vocoder <http://www.sirlab.de/linux/download_vocoder.html> \[GNU
    GPLv2+\]
-   WASP <http://linux01.gwdg.de/~nlissne/wasp/index.html> \[GNU GPLv3\]
-   Nova
    <http://chuck.stanford.edu/planetccrma/mirror/fedora/linux/planetccrma/10/i386/repoview/ladspa-nova-plugins.html>
    \[GNU GPLv2+\]
-   Socal's LEET Plugins <http://code.google.com/p/leetplugins/> \[GNU
    GPLv2\]

### Linux VST (LXVST)
{#LinuxVST}

-   Loomer <http://www.loomer.co.uk/> \[Proprietary\]
-   Distrho <http://distrho.sourceforge.net/ports.php> \[GNU GPLv3\]
-   Argotlunar <http://mourednik.github.io/argotlunar/> \[GNU GPLv2\]
-   U-he <https://u-he.com/> \[Proprietary\]

## How to install plugins?

### Linux

[Installation]{.dfn} will vary a little depending on how the plugins
have been obtained. If a particular plugin package appears in the local
repository, installing it using is done by using the normal software
package management tool for the system. Most Linux distributions that
are good for audio work will have most of the LADSPA and LV2 plugins
mentioned above available in ready-to-use form.

Finding them will typically require *searching* the distribution\'s
repository to find the name of the package. The tools for doing this
vary from distribution to distribution. A good place to start searching
is with the name of the package (e.g. \"caps\" or \"cmt\"). There are no
fixed rules about what different Linux distributions call their packages
for a given set of plugins.

If the package isn\'t available, then the plugins can be built from
source (plugins are generally fairly easy to compile and
well-documented).

LADSPA plugins are shared library files. They need to be installed in
either /usr/lib/ladspa, /usr/local/lib/ladspa or in a directory
mentioned in the local LADSPA_PATH environment variable.

LV2 plugins are folders/directories. They need to be installed in either
/usr/lib/lv2, /usr/local/lib/lv2 or a directory mentioned in the local
LV2_PATH environment variable.

Linux VST (LXVST) plugins are distributed as shared library files. They
are typically installed in /usr/lib/lxvst, /usr/local/lib/lxvst or a
directory mentioned in the local LXVST_PATH environment variable.

### OS X

Except for the particularly technical computer user, building and
installing plugins in the LV2 (or LADSPA) format is probably not
something worth planning on.

Most of the plugins likely to be used on OS X will be in Apple\'s
AudioUnit format. These have their own installation process that tends
to just work.
