# Ubuntu Linux
[Ubuntu Linux]{.dfn} is the most popular variety of Linux in use on
desktop and laptop systems. It has the backing of a for-profit
corporation (Canonical Inc.), a defined philosophy and a huge and
worldwide user base. As a result, it is a common platform for people who
want to use Ardour and other tools for music creation and pro-audio
work.

## High Level Recommendations for Ubuntu Users
{#high-level-reqs}

Currently, installing pro audio applications on vanilla Ubuntu requires
some configuration, in order for the user to gain realtime privilege
(read below). Ubuntu Studio, which is an official flavor of Ubuntu, and
thus shares the repositories with Ubuntu, has this already configured.
Other distributions, such as KXStudio, and Dreamstudio are largely based
on Ubuntu, and like Ubuntu Studio, has these settings pre-configured,
while also containing customized versions of Ubuntu packages, which
often are more up to date.

## Installing Ardour
{#install-ardour}

There may be unintended differences, and even bugs in Ubuntu native
packages, as a result of a different building method. For this reason,
Ardour developers highly recommend installing the official ready-to-run
version of the program that can be downloaded from
[ardour.org](https://community.ardour.org/download), as Ubuntu native
packages are not supported in the official Ardour forums or other
support channels.

Follow these steps to install the latest version of Ardour:

1.  Download the latest release from
    [ardour.org](https://community.ardour.org/download).
2.  [Right]{.kbd .mouse}-click the downloaded file and choose
    properties.
3.  Click the Permissions tab and check the option \"Allow this file to
    run as a program\".
4.  Close the dialog and double-click the file.
5.  Follow the prompts.

## Problems with JACK configuration
{#jack-issues}

### What is the problem?
{#-jack-problem}

To function as intended, JACK needs to run with access to two operating
system facilities called [realtime scheduling]{.dfn} and [memory
locking]{.dfn}. This means that the user who starts JACK *must* be
allowed access to these facilities. By default, Ubuntu does create a
user group that has this permission but---it does not put new users into
this group by default. Read more about why
[here](https://wiki.ubuntu.com/Audio/TheAudioGroup). Consequently, the
user will not have permission to run JACK in the way they should.

### Symptoms

A message like `Cannot lock down memory`{.sample} in the output from
JACK as it starts up. This output may be hidden in the Messages window
of QJackCtl (aka JACK Control), so one should check there.

### How to fix

Make sure the file /etc/security/limits.d/audio.conf exists. If it is
named /etc/security/limits.d/audio.conf.disabled, rename it to the
former. Run the command:

[sudo usermod -a -G audio *YOUR-LOGIN-NAME*]{.kbd .cmd .lin}

Then log out and log in again. On Ubuntu Studio the user is a member of
audio group by default, but not on other official flavors.

## Reporting Issues

Given the difficulties in supporting Ubuntu and the limited time and
resources of the Ardour team, the [Ubuntu Studio Project]{.dfn} has
requested that issues and bug reports related to Ubuntu, Ubuntu Studio
and other derivatives be directed to them.

### Contact Information for Ubuntu Studio
{#ubuntu-studio-contacts}

[The Ubuntu Studio Homepage](http://ubuntustudio.org)

[The Ubuntu Studio
Forums.](http://ubuntuforums.org/forumdisplay.php?f=335)

[Information on the Ubuntu Studio Mailing
Lists.](https://help.ubuntu.com/community/UbuntuStudio/MailLists)

[Information on the Ubuntu Studio IRC
channel.](https://help.ubuntu.com/community/UbuntuStudio/IRC)
#ubuntustudio on irc.freenode.net
